
from pymongo import MongoClient

client = MongoClient("mongodb+srv://testmongo:<password>@cluster0.oalfel9.mongodb.net/?retryWrites=true&w=majority")

db = client.user_db
collection_name = db["user_collection"]

# Add a log to confirm a successful connection
try:
    client.admin.command('ping')
    print("You successfully connected to MongoDB!")
except Exception as e:
    print(e)
