import pandas as pd
import csv
import os
from datetime import datetime, timedelta


def extract_data(group):
    """Extract data based on Timestamp range."""
    start_time = group['Timestamp'].iloc[0]
    end_time = group['Timestamp'].iloc[-1]
    time_range = pd.date_range(start=start_time, end=end_time, freq='5S')
    return group[group['Timestamp'].isin(time_range)]


def process_study1(filename, file_path):
    split_csv_name = filename.split("_")
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if reader.line_num == 7:  # 第七行
                break
        datetime_str = f"{row[0]} {row[1]}"
        start_timestamp = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S %p')
        start_timestamp_24h = start_timestamp.strftime('%d/%m/%Y %H:%M:%S')
        start_timestamp_dt = datetime.strptime(start_timestamp_24h, '%d/%m/%Y %H:%M:%S')
        new_timestamp_dt = start_timestamp_dt - timedelta(seconds=5)
        df = pd.read_csv(file_path, skiprows=8, sep=',')
        df = df.drop(df.index[0])
        df['Participant_ID'] = split_csv_name[1]
        df['Trail_ID'] = split_csv_name[2]
        df['Timestamp'] = new_timestamp_dt + pd.to_timedelta(df['Sample Time'])

        df = df.drop("Sample Time", axis=1)  # 删除"Sample Time"列

        return df


# 处理cbr目录
def server_process_CBR(study1_csv_files_path, directory):
    dataframes = []
    for file_path in study1_csv_files_path:
        file_name_with_extension = os.path.basename(file_path)
        df = process_study1(file_name_with_extension, file_path)
        dataframes.append(df)

    study1_df = pd.concat(dataframes, axis=0)
    study1_df = study1_df.drop(study1_df.columns[study1_df.columns.str.contains('Unnamed', case=False)], axis=1)
    only_columns = ['Timestamp', 'Participant_ID', 'Trail_ID']
    df_columns = study1_df.columns.tolist()
    df_columns = list(set(df_columns) - set(only_columns))

    for column in df_columns:
        change_column = column[0] + column[1:].lower()
        new_column = "Temperature_" + change_column
        study1_df.rename(columns={column: new_column}, inplace=True)

    study1_df = study1_df.reindex(columns=only_columns + list(study1_df.columns.difference(only_columns)))
    study1_df['Timestamp'] = pd.to_datetime(study1_df['Timestamp']).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    res = directory + ".csv"
    study1_df.to_csv(res, index=False)


def process_csv_HR(csv_filename, hr_data, file_path):
    """Process HR data from CSV."""
    split_csv_name = csv_filename.split("_")
    resultData = pd.DataFrame(columns=['Timestamp', 'Participant_ID', 'HR (bpm)'])

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        row = next(csv_reader)
        datetime_str = f"{row[2]} {row[3]}"
        start_timestamp = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')

        df = pd.read_csv(file_path, skiprows=2, sep=',')
        df['Timestamp'] = start_timestamp + pd.to_timedelta(df['Time'])
        resultData['HR (bpm)'] = df['HR (bpm)']
        resultData['Timestamp'] = df['Timestamp']
        resultData['Participant_ID'] = split_csv_name[1]
        resultData['Trail_ID'] = split_csv_name[2]

    return pd.concat([hr_data, resultData], axis=0)


def process_csv_TSk(csv_filename, tsk_data, file_path):
    """Process Tsk data from CSV."""
    split_csv_name = csv_filename.split("_")
    resultData = pd.DataFrame(columns=['Timestamp'])

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        df = pd.read_csv(file_path, skiprows=20, sep=',', names=['Date/Time', 'Unit', 'Value', 'value1'])
        df['Timestamp'] = pd.to_datetime(df['Date/Time'] + ' ' + df['Unit'], format="%d/%m/%y %I:%M:%S %p")

        resultData['Timestamp'] = df['Timestamp']
        task_value_name = "Temperature_" + split_csv_name[4]
        resultData[task_value_name] = df['value1']
        resultData['Participant_ID'] = split_csv_name[1]
        resultData['Trail_ID'] = split_csv_name[2]

    return pd.concat([tsk_data, resultData], axis=0)


def merge_csv_files_in_directory(directory, result_name):
    csv_files = [f for f in os.listdir(directory) if f.endswith(".csv")]

    if not csv_files:
        return

    first_file = os.path.join(directory, csv_files[0])
    merged_data = pd.read_csv(first_file)
    merged_data['Participant_ID'] = merged_data['Participant_ID'].astype(str)
    for csv_file in csv_files[1:]:
        file_path = os.path.join(directory, csv_file)
        df2 = pd.read_csv(file_path)
        df2['Participant_ID'] = df2['Participant_ID'].astype(str)

        df1_columns = merged_data.columns.tolist()
        df2_columns = df2.columns.tolist()
        intersection = list(set(df1_columns).intersection(df2_columns))

        merged_data = pd.merge(merged_data, df2, on=intersection, how='outer')

    merged_data = merged_data.sort_values(by='Timestamp', ascending=True)
    merged_data.to_csv(result_name, index=False)


# 处理tsk和hr
def server_process_tsk_hr(study2_csv_files_path, directory):
    hr_data = pd.DataFrame()
    tsk_data = pd.DataFrame()

    for file_path in study2_csv_files_path:

        file_name_with_extension = os.path.basename(file_path)
        split_result = file_name_with_extension.split("_")

        if len(split_result) >= 3:
            if split_result[3] == "HR":
                hr_data = process_csv_HR(file_name_with_extension, hr_data, file_path)
            elif split_result[3] == "Tsk":
                tsk_data = process_csv_TSk(file_name_with_extension, tsk_data, file_path)

    tsk_data = tsk_data.groupby("Timestamp").first().reset_index()

    # Merge dataframes
    merged_data = pd.merge(hr_data, tsk_data, on=['Timestamp', 'Trail_ID', 'Participant_ID'], how='outer')
    merged_data = merged_data.sort_values('Timestamp', ascending=True)

    # Save to temporary excel file and then read it again to process 5s data
    result_5sData = merged_data.groupby('Trail_ID').apply(extract_data).reset_index(drop=True)

    # Reorder columns
    result_5sData['Timestamp'] = pd.to_datetime(result_5sData['Timestamp']).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    cols = result_5sData.columns.tolist()
    if 'HR (bpm)' in cols:
        cols.remove('HR (bpm)')
        idx_trail_id = cols.index('Trail_ID')
        cols.insert(idx_trail_id + 1, 'HR (bpm)')
        result_5sData = result_5sData[cols]
    res = directory + ".csv"
    result_5sData.to_csv(res, index=False)


def create_directory_csv_dict(root_dir="."):
    directory_csv_dict = {}

    items = os.listdir(root_dir)

    for item in items:
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            csv_files = []
            for file in os.listdir(item_path):
                if file.endswith(".csv"):
                    csv_files.append(file)
            directory_csv_dict[item] = csv_files

    return directory_csv_dict


def main():
    """Main execution function."""

    """
     dir = os.getcwd()
    study1 = "Study 1 - Rugby League"
    study2 = "Study 2 - Acclimation"

    study1_folder_path= os.path.join(dir, study1)
    study2_folder_path= os.path.join(dir, study2)


    study1_csv_files_path = []
    for root, dirs, files in os.walk(study1_folder_path):
        for file in files:
            if file.endswith(".csv"):
                study1_csv_files_path.append(os.path.join(root, file))

    study2_csv_files_path = []
    for root, dirs, files in os.walk(study2_folder_path):
        for file in files:
            if file.endswith(".csv"):
                study2_csv_files_path.append(os.path.join(root, file))


    study2_df = server_process_tsk_hr(study2_csv_files_path)
    study1_df = server_process_CBR(study1_csv_files_path)

    study1_df.to_csv("1.csv")
    study2_df.to_csv("2.csv")

    merge_csv_files("1.csv","2.csv","result.csv")


    """


dir = os.getcwd()
directory_csv_dict = create_directory_csv_dict()

for directory, csv_files in directory_csv_dict.items():
    folder_path = os.path.join(dir, directory)
    file_path = []
    for csv_file in csv_files:
        file_path.append(os.path.join(folder_path, csv_file))
    # print(csv_files[0])
    if len(csv_files) != 0:
        if 'HR' in csv_files[0] or 'TSk' in csv_files[0]:
            # 调用server_process_tsk_hr
            server_process_tsk_hr(file_path, directory)
        else:
            # 调用server_process_CBR
            server_process_CBR(file_path, directory)

merge_csv_files_in_directory(dir, "result.csv")
if __name__ == "__main__":
    main()