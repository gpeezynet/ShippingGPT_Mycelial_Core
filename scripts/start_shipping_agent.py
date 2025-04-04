import os
import datetime

def load_env():
    api_key = os.getenv("OPENAI_API_KEY", "NO_KEY_LOADED")
    mongo = os.getenv("MONGO_URI", "NO_DB")
    print(f"[{datetime.datetime.now()}] ShippingGPT STARTING...")
    print(f"→ OPENAI Key Loaded: {'Yes' if api_key != 'NO_KEY_LOADED' else 'No'}")
    print(f"→ Mongo Connection: {'Yes' if mongo != 'NO_DB' else 'No'}")

def simulate_agent():
    print("📦 Shipping agent in mock mode. Entropy detection systems warming up...")
    print("🧠 SOP monitoring active.")
    print("📈 Stability index placeholder loaded.")
    print("🧬 No live GPT calls – MOCK MODE ENABLED.")

if __name__ == "__main__":
    load_env()
    simulate_agent()
