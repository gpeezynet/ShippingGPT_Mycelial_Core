from pymongo import MongoClient
from datetime import datetime

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["shippinggpt"]
collection = db["chaos_events"]

def log_event():
    print("📦 CHAOS EVENT LOGGER")
    event = {
        "event_type": input("Event type (e.g., short_count, mislabel): ").strip(),
        "source": input("Source (e.g., receiving, packing): ").strip(),
        "sop_reference": input("SOP Reference (e.g., 5.1): ").strip(),
        "description": input("Description: ").strip(),
        "timestamp": datetime.utcnow(),
        "severity": int(input("Severity (1–5): ").strip()),
        "resolved": False,
        "operator_id": input("Operator ID (e.g., georgie01): ").strip(),
        "tags": input("Tags (comma-separated, optional): ").strip().split(",")
    }
    result = collection.insert_one(event)
    print(f"✅ Logged. Event ID: {result.inserted_id}")

if __name__ == "__main__":
    log_event()
