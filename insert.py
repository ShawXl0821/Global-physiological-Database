import pandas as pd
from pymongo import MongoClient

# Connect to the database
client = MongoClient("mongodb://localhost:27017")

# Select database and collection
db = client["Project5703"]
collection = db["test"]

# extract data from csv
csv_file = "D:\COMP5703\Study 1 - Rugby League\CBR_02_E1C_Tre.csv"  # 替换为你的CSV文件路径
data = pd.read_csv(csv_file)

# trun csv file into a dictionary 
data_dict = data.to_dict(orient="records")

# insert data into collection
collection.insert_many(data_dict)

client.close()





