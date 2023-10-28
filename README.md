# Global-physiological-Database
The aim of this project is to address the challenge of inaccessible physiological data collected from various laboratory studies. These studies have generated valuable data on participants' physiological responses under diverse environmental conditions, activity levels, and clothing settings. However, due to the lack of data publication, the potential for reusing this data to answer new research questions remains untapped. To overcome this limitation, we collaborate on defining the best database architecture to store and organize these physiological datasets.

<br>

This is a guidance for general users to deploy the MongoDB database locally and manipulate the database to manage the large dataset.

<br>

## Table of contents
-   [Database structure](#database-structure)
-   [Getting Started](#getting-started)
    -   [Data Cleaning](#data-cleaning)
    -   [Installation of MongoDB](#installation-of-mongodb)
    -   [Deploy the database](#deploy-the-database)
-   [Database Manipulation](#database-manipulation)
    -   [Import data](#import-data-into-database)
    -   [Delete data](#delete-data-in-the-collection)
    -   [Modify data](#modify-data-in-the-collection)
    -   [Export data](#export-data)
    -   [Query data](#query-data)
    -   [Work with Python](#work-with-python)
-   [Advanced Configuration](#advanced-configuration)
    -   [Add index for a collection](#add-index-for-a-collection)
    -   [Add validation rules for a collection](#add-validation-rules-for-a-collection)
    -   [Trigger](#trigger)    
-   [Data transfer](#data-transfer)
    -   [Prerequisite](#prerequisite)
    -   [Instruction](#instruction)

<br>

## Database structure
The database structure designed by us divided the large dataset into four parts: data (storing most of the experimental data), participant (contain information of the participants of experiments), experiment (include the information of different experiments) and trial (information of each trial of the experiment). 

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/structure.png>

## Getting started  

### Data Cleaning  
Before storing data into the database, you need to clean the dataset to a certain format. We have provided a sample data cleaning script and an explanation at https://github.com/ShawXl0821/Global-physiological-Database/tree/main/Data. The result of the data cleaning must contain timestamp, Participant_ID, Trial_ID and paramameters of the experiment data. A sample cleaned dataset should be like this:  

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/result.png>

Then, you are good to go with the database.  

### Installation of MongoDB  
1. For this project, we selected MongoDB Community Server to store and manage the database on local environment. You can search 'mongodb community server' and click the first result.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/search1.png>

2. Click 'select package' to select the installer that suits your environment. We used Windows x64 for the demonstration.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/download1.png>

3. You can also visit https://www.mongodb.com/try/download/community

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/install1.png>

4. Execute the installer, you should choose the complete installation option and install the MongoDB Compass (which will be used in the next phase) as well.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/install2.png>
   
5. Install Mongod as a service and custom your direcory setting (recommend using the default direcory to avoid errors)

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/install3.png>

6. Install and open the MongoDB Compass

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/newCompass1.png>

7. Click 'New connection' on the left and the interface will automatically generate a connection string for you. Click 'Connect' to connect to your localhost. You can also click 'Save & Connect' to save your connection information.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/newCompass2.png>

<br>

### Deploy the database
1. Create a database and collection for storing experimental dataset  
On your Compass interface, click 'new database' on the left. Name your database and first collection. Here we named it 'Project 5703' and 'Comfort_data'. This collection will be used for storing our experimental dataset.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/createdb1.png>

2. Create a collection for storing experiment information  
You can click 'Create collection' by the database you just created and name it 'Experiment'. This collection is for storing experiment information.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/createexp.png>

3. Create a collection for storing trial information  
You can click 'Create collection' by the database you just created and name it 'Trial'. This collection is for storing trial information.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/createtrial.png>

4. Create a collection for storing participant information  
You can click 'Create collection' by the database you just created and name it 'Participant'. This collection is for storing participant information.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/createparticipant.png>

Then, you need to import corresponding data into different collections (will be explained next)

<br>

## Database Manipulation

### Import data into database
1. Import csv file into the collection.  
   In the Comfort_data collection, click 'ADD DATA' and select 'import JSON or csv'.  

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/insert1.png>

Then, confirm the inserted result. You'd better tick 'Ignore empty strings' to filter empty values.  

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/insert2.png>

After that, you should see the inserted documents:  

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/insert3.png>

2. Import a single document  
   You can also import a single document. For exmaple, in the collection 'Particpant', click 'ADD DATA' and select 'Insert a document'.
   Then, edit the document information following the default format:

  <img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/insertSingle.png> 

<br>

### Delete data in the collection

You can remove a data record. First, you need to move you cursor on a record. It will show options: 
 <img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/delete1.png> 

Then, click the bin icon and click 'Delete'.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/delete2.png> 

A record has been removed now.

<br>

### Modify data in the collection 

You can directly modify a record on the Compass interface.  
First, move your cursor on the record you want to edit.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/modify1.png> 

Then, click the pencil icon to start modification.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/modify2.png> 

At last, click 'update' to save your change. A record has been updated.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/modify3.png> 

<br>

### Export data 
You can export data into a csv file as well.  
First, click 'EXPORT DATA' and select 'Export query results' to export part of the dataset of 'Export full collection' to export the entire collection of data.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/export1.png> 

Then, select JSON or CSV as the output format (here I select CSV). Click 'Export'.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/export2.png> 

The exported file looks like this:

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/export3.png> 

<br>

### Query data
You can use the filter or aggregation pipeline to query the data you want  
For detailed filter guidance, please visit https://www.mongodb.com/docs/compass/current/query/filter/  
For detailed aggregation guidance, please visit https://www.mongodb.com/docs/manual/aggregation/
For example query, please visit https://github.com/ShawXl0821/Global-physiological-Database/tree/main/Aggregation%20pipeline%20example

1. filter on the Compass
Edit directly in the filter field, then click 'find'. In this case, I returned the participants over 20.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/filter1.png> 

2. Aggregation pipeline
For more complex query, you have to use aggregation pipeline. Click' Aggregation' and it will lead you to the aggregation pipeline page.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/aggregation1.png>

You can start by clicking 'Add stage'

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/stage1.png>

You can also edit the text field directly to write your pipeline 

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/aggregation2.png>

The aggregation pipeline is useful for operations among multiple collections. For example, I want to get the average heart rate of participants over 20. In this case, I need to use Comfort_data collection as well as Participant collection. The pipeline can be written as:

```
[
  {
    $lookup:
      /**
       * from: The target collection.
       * localField: The local join field.
       * foreignField: The target join field.
       * as: The name for the results.
       */
      {
        from: "Participant",
        localField: "Participant_ID",
        foreignField: "Participant_ID",
        as: "participants",
      },
  },
  {
    $unwind:
      /**
       * path: Path to the array field.
       */
      {
        path: "$participants",
      },
  },
  {
    $match:
      /**
       */
      {
        "participants.Age": {
          $gt: 20,
        },
        "HR (bpm)": {
          $exists: true,
        },
      },
  },
  {
    $group:
      /**
       * _id: The id of the group.
       */
      {
        _id: null,
        averageHeartRate: {
          $avg: "$HR (bpm)",
        },
      },
  },
]
```
The result looks like this:  
<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/avg_hr.png>

<br>

### Work with Python
You can also write Python scripts to manipulate with your data.

#### Connect to the MongoDB client
```
from pymongo import MongoClient

# Connect to the database
client = MongoClient("mongodb://localhost:27017")
```
<br>

#### Insert data from csv files
After connecting to the MongoDB client, you can insert data from csv into the database. Here's how you can do this (details in the : 
```
# extract data from csv
csv_file = "D:\COMP5703\Study 1 - Rugby League\CBR_02_E1C_Tre.csv"  # replace the path with your own
data = pd.read_csv(csv_file)

# trun csv file into a dictionary 
data_dict = data.to_dict(orient="records")

# insert data into collection
collection.insert_many(data_dict)

```
You can also insert data line by line, but it is not recommended for large dataset
```
# Insert data of csv file line by line
with open(csv_file, "r") as file:
    lines = file.readlines()
    headers = lines[0].strip().split(",")
    
    for line in lines[1:]:
        data = line.strip().split(",")
        doc = {}
        for i in range(len(headers)):
            doc[headers[i]] = data[i]
        collection.insert_one(doc)
```  
Then you can check if it works in MongoDB Compass:
<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/python1.png>

<br>

Of course, the data is hard to read because the CSV has not been cleaned yet. To learn about how we cleanded the dataset, please visit https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Data/Instruction.md

<br>

#### Query data with Python
You can also query data with Python as we did in the 'Query data' part using the following script (Details in the .
```
pipeline = [   
    {
        '$project': {
            'fields': {
                '$objectToArray': '$$ROOT'
            }
        }
    }, {
        '$unwind': {
            'path': '$fields'
        }
    }, {
        '$match': {
            'fields.k': {
                '$ne': '_id'
            }
        }
    }, {
        '$group': {
            '_id': None, 
            'keys': {
                '$addToSet': '$fields.k'
            }
        }
    }, {
        '$project': {
            '_id': 0, 
            'keys': 1
        }
    }

]

# execute the pipeline
result = list(collection.aggregate(pipeline))

# print the result
print(result)

```
The results will be printed in the terminal: 
<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/python2.png>

<br>

Tips: You can easily get the Python version of pipeline from MongoDB Compass by following procedures:  
1. Click into 'Aggregations' page and select one of your queries:
<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/python3.png>

2. Click 'EXPORT TO LANGUAGE' and select 'Python'
<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/python4.png>

You now have the Python version of pipeline query.

<br>

## Advanced configuration 

### Add index for a collection
Indexes support efficient execution of queries in MongoDB. If an appropriate index exists for a query, MongoDB uses the index to limit the number of documents it must scan and thus improve the query performance. For more details about index, please visit https://www.mongodb.com/docs/manual/indexes/

<br>

Click 'Indexes' and it will lead you to the index information page. Please note that MongoDB will automatically generate an id for each record. This is the default index. 

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/index1.png>

To add a custom index, click 'Create index' and select fileds and types. You can also tick 'Create unique index' to avoid having data with duplicate indexes.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/index2.png>

After that, you will see the created indexes in the current page.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/index3.png>

For this project, we recommend you to create indexes for Partcipant_ID of Participant, Experiment_ID of Experiment and Trial_ID of Trial to avoid duplicate ids for data validation.

<br>

### Add validation rules for a collection
Validation rules are an important tool in MongoDB for ensuring data integrity and consistency within documents. By creating validation rules on a collection, you can enforce specific data structures and constraints besides indexes mentioned before.

<br>

In the collection view, click on the "validation" tab at the top. This will display the current validations on the collection.  
Click 'Add rule' to add a new validation rule 

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/validation1.png>

At this page, you can adjust validation action (error or warning) and validation level (off, moderate or strict). Then, you can edit your validation rule.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/validation2.png>

Here's an example: 
```
{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'name'
    ],
    properties: {
      name: {
        bsonType: 'string',
        description: 'Must be of string type'
      }
    }
  }
}
```
In the example above, we define validation rules that require documents to contain the `name` fields. The `name` field must be of string type.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/validation3.png>

<br>

### Trigger

Unfortunately, MongoDB only supports trigger function on Atlas cloud server. So, we will run a Javascript file in Node.js to act as a trigger to valid data with specific requirements.

#### Pre-requisite
1. Node.js environment with npm package manager
2. Mongoose library

<br>

#### Environment set up
1. Download Node.js installer on https://nodejs.org/en/download/current

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/node2.png>

2. Execute the installer and install all related items automatically

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/nodejs1.png>

3. Open your terminal, direct to your directory, run 'npm install mongoose' to install mongoose library

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/npm1.png>

5. Download app.js file in the repository to your directory that installed mongoose in the previous steps. This script can scans the whole data to check if Experiment_ID of a Trial record exists in the Experiment collection.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/trigger1.png>

6. If the data does not meet the reqirement, you would see an error messaage

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/wrongData.png>

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/trigger2.png>

<br>

#### Notes
You can edit the js script by yourself to add more functions such as deleting invalid data. However, this "trigger script" requires you to run this script each time you want to validate your dataset.

<br>

## Data transfer
You can use a tool 'mongodump' from MongoDB Community Serverthat can extract data from the database into BSON files. Then it will be easy for you to send the copy of the data to someone else. Then, the receiver can use the tool 'mongorestore' to restore the data to his own MongoDB server. This enables the data transfer among multiple users.

<br>

### Prerequisite 
1. Make sure you have installed MongoDB Command Line Database Tools. If not, you can just google 'MongoDB Command Line Database Tools download' and click into the first item, or visit https://www.mongodb.com/try/download/database-tools

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/tool0.png>
   
<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/tool1.png>

<br>

2. Make sure your MongoDB service is running

<br>

### Instruction
1. Direct to the folder where you installed your MongoDB Command Line tools, enter 'cmd' to enter the Command Prompt.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/transfer0.png>

2. Run the following command to dump your data from your database into BSON files to the folder

```
mongodump --db <Your database name> --out <folder where you want to dump your data to>
```
<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/transfer1.png>

4. To restore your data, run the command:
```
mongorestore --db <your database name> <the path of the folder that contains data>
```
<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/restore2.png>

6. Now you can see the data transferred on your server
<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/transfer2.png>
