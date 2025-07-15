import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client.ai_agent_db
collection = db.candidates

def save_candidates(candidates: list, job_criteria: dict):
    doc = {
        "job_criteria": job_criteria,
        "candidates": candidates
    }
    collection.insert_one(doc)
    print("✅ Candidates saved to MongoDB.")
