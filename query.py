from pymongo import MongoClient

# Connect to the database
client = MongoClient("mongodb://localhost:27017")

# Select database and collection
db = client["Project5703"]
collection = db["Comfort_data"]

# define your pipeline
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

client.close()

