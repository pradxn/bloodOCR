import pymongo
from bson.objectid import ObjectId
from dataParser import dataParsed, rowStr

output = dataParsed(rowStr)

client = pymongo.MongoClient('mongodb+srv://pradeep:zmkoxDl2NEoPCPFT@cluster1.fewx6mu.mongodb.net/?retryWrites=true&w=majority')
db = client["OpenAI_database_name"]
collection = db["OpenAI_collection_name"]

keyInput = input('Document name: \n')
key = keyInput
value = output #from openai prompt

document = {key : value}
collection.insert_one(document)
object_id = str(document['_id'])
print("Save this id for future reference: "+ object_id)
print('\n')

object_id_str = input('Enter reference id: ')
object_id = ObjectId(object_id_str)
# retrieve the document with the given object id
document = collection.find_one({'_id': object_id})

# print the retrieved document
#print(document)
#print('\n')
#print(document[key])
client.close()