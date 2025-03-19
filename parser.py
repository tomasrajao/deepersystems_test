from dataclasses import dataclass
import json

from pymongo import MongoClient

from schemas import UserModel
    

client = MongoClient("mongodb://localhost:27017/")
db = client["database"]
users_collection = db["users"]

with open('udata.json', 'r') as file:
    users_data = json.load(file)
    validated_users = [UserModel(**user).to_mongo() for user in users_data['users']]
    if isinstance(validated_users, list):
        result = users_collection.insert_many(validated_users)
    else:
        result = users_collection.insert_one(validated_users)

print("Data has been imported successfully!")
