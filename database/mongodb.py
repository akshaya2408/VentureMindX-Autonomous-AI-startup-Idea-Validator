from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017"
)

db = client["venturemind"]

startup_collection = db["startups"]

report_collection = db["reports"]