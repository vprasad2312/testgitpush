import pymongo
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://vprasad2312:Mongodb123@cluster0.1wymaq4.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


d = {
    "name":"vivek",
    "email" : "vprasad2312@gmail.com",
    "surname" : "prasad"
}
db1 =client["mongotest"]
coll= db1['test']
coll.insert_one(d)