from config.mongo import get_entropy_collection

if __name__ == "__main__":
    try:
        collection = get_entropy_collection()
        print("✅ Connected to MongoDB collection:", collection.full_name)
    except Exception as e:
        print("❌ MongoDB connection failed:", str(e))
