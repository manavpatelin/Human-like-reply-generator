from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

try:
    client = MongoClient(MONGO_DB_URL, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    print("✅ MongoDB connected")
except Exception as e:
    print("❌ MongoDB connection failed:", e)

db = client["Reply_db"]
collection = db["Posts"]

def store_reply(platform, post_text, generated_reply):
    entry = {
        "platform": platform,
        "post_text": post_text,
        "generated_reply": generated_reply,
        "formatted_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    collection.insert_one(entry)
