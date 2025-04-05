from flask import Flask, jsonify, request
from pymongo import MongoClient
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# MongoDB setup
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["shippinggpt"]
entropy = db["entropy_logs"]

# Get entropy events from the last 7 days
@app.route("/entropy/week", methods=["GET"])
def get_week_entropy():
    since = datetime.utcnow() - timedelta(days=7)
    events = list(entropy.find({"timestamp": {"$gte": since}}))
    for e in events:
        e["_id"] = str(e["_id"])
        e["timestamp"] = e["timestamp"].isoformat() + "Z"
    return jsonify(events)

# Get the current system stability score
@app.route("/stability/current", methods=["GET"])
def get_stability():
    # Mock score for now
    score = {
        "Shipping_Stability": 42.7,
        "as_of": datetime.utcnow().isoformat() + "Z"
    }
    return jsonify(score)

# Post a new chaos event
@app.route("/entropy/log", methods=["POST"])
def post_entropy():
    data = request.json
    required = ["event_type", "location", "operator_id", "resolution_status", "notes"]
    if not all(k in data for k in required):
        return jsonify({"error": "Missing required fields"}), 400
    data["timestamp"] = datetime.utcnow()
    data["root_cause_tag"] = data.get("root_cause_tag", "unclassified")
    result = entropy.insert_one(data)
    return jsonify({"message": "Event logged", "id": str(result.inserted_id)}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)
