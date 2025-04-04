import os
import datetime
from config.mongo import get_entropy_collection

def log_entropy_event(
    event_type,
    location,
    operator_id,
    resolution_status,
    notes,
    root_cause_tag=None
):
    collection = get_entropy_collection()
    event = {
        "event_type": event_type,
        "timestamp": datetime.datetime.utcnow(),
        "location": location,
        "operator_id": operator_id,
        "resolution_status": resolution_status,
        "notes": notes,
        "root_cause_tag": root_cause_tag or "unclassified"
    }
    result = collection.insert_one(event)
    print(f"✅ Logged entropy event with ID: {result.inserted_id}")

# Optional direct use for testing
if __name__ == "__main__":
    log_entropy_event(
        event_type="label_generation_failure",
        location="Label Station A",
        operator_id="ZREED",
        resolution_status="escalated",
        notes="Test run: label API timeout during batch print",
        root_cause_tag="api_latency"
    )
