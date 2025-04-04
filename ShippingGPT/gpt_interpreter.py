import os
import openai
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv

# Load OpenAI API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["shippinggpt"]
collection = db["chaos_events"]

# Get the most recent chaos event
latest_event = collection.find_one(sort=[("timestamp", -1)])

if not latest_event:
    print("❌ No chaos events found.")
    exit()

# Construct the GPT prompt from the event
prompt = f"""
You are WarehouseGPT, a logistics process analyst trained in entropy-aware systems.

A new chaos event has been logged from the warehouse. Your task is to analyze it and suggest a structured, SOP-aligned recommendation to improve stability and prevent recurrence.

Chaos Event Details:
- Type: {latest_event['event_type']}
- Source: {latest_event['source']}
- SOP Reference: {latest_event['sop_reference']}
- Description: {latest_event['description']}
- Severity: {latest_event['severity']}
- Operator: {latest_event['operator_id']}

Give a short recommendation and explain how it connects to the SOP reference provided.
"""

# GPT API call using new syntax (v1.0+)
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",  # Use gpt-4 if/when you have access
    messages=[
        {"role": "system", "content": "You are a warehouse entropy analyst helping reduce chaos through SOP improvements."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.2
)

# Output GPT result
print("\n📤 GPT Recommendation:\n")
print(response.choices[0].message.content)
