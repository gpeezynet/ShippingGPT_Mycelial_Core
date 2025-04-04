import os
import datetime
from config.mongo import get_entropy_collection

def log_entropy_event(event):
    collection = get_entropy_collection()
    result = collection.insert_one(event)
    print(f"\n✅ Logged entropy event with ID: {result.inserted_id}\n")

def run_cli_logger():
    print("📦 Entropy Event Logger")
    print("----------------------")

    event = {}
    event["event_type"] = input("Event Type (e.g., barcode_scan_failure): ").strip()
    event["location"] = input("Location (e.g., Packing Station B): ").strip()
    event["operator_id"] = input("Operator ID (e.g., JHUNT): ").strip()
    event["resolution_status"] = input("Resolution Status (open/escalated/resolved): ").strip().lower()
    event["notes"] = input("Notes: ").strip()
    event["root_cause_tag"] = input("Root Cause Tag (optional): ").strip() or "unclassified"
    event["timestamp"] = datetime.datetime.utcnow()

    confirm = input("\n✅ Ready to log this event? (Y/N): ").strip().lower()
    if confirm == "y":
        log_entropy_event(event)
    else:
        print("❌ Event not logged.")

if __name__ == "__main__":
    run_cli_logger()
