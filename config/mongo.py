import os
from pymongo import MongoClient

def get_mongo_client():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    return MongoClient(mongo_uri)

def get_entropy_collection():
    client = get_mongo_client()
    db = client["shippinggpt"]
    return db["entropy_logs"]
