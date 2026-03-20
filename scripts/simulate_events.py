import httpx
import asyncio
import json
import uuid
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "http://localhost:8000"
API_KEY = os.getenv("API_KEY")

TEST_USER_ID = f"test_user_{uuid.uuid4().hex[:8]}"

TEST_EVENTS = [
    {
        "user_id": TEST_USER_ID,
        "event_type": "view_product",
        "metadata": {
            "product_id": "laptop_pro_2024",
            "category": "High-End Electronics",
            "price": 2499.00
        }
    },
    {
        "user_id": TEST_USER_ID,
        "event_type": "add_to_cart",
        "metadata": {
            "product_id": "laptop_pro_2024",
            "category": "High-End Electronics",
            "price": 2499.00
        }
    },
    {
        "user_id": TEST_USER_ID,
        "event_type": "view_product",
        "metadata": {
            "product_id": "mechanical_keyboard_x",
            "category": "Accessories",
            "price": 150.00
        }
    }
]

async def send_event(event):
    headers = {"X-API-Key": API_KEY}
    async with httpx.AsyncClient() as client:
        print(f"Sending {event['event_type']} for user {event['user_id']}...")
        response = await client.post(f"{API_URL}/events", json=event, headers=headers)
        if response.status_code == 200:
            print(f"✅ Success: {response.json()['event_id']}")
        else:
            print(f"❌ Error {response.status_code}: {response.text}")

async def get_memory(user_id):
    headers = {"X-API-Key": API_KEY}
    async with httpx.AsyncClient() as client:
        print(f"\nRetrieving memory for user {user_id}...")
        response = await client.get(f"{API_URL}/users/{user_id}/memory", headers=headers)
        if response.status_code == 200:
            memory = response.json()
            print("--- MEMORY PROFILE ---")
            print(json.dumps(memory, indent=2))
        else:
            print(f"❌ Error {response.status_code}: {response.text}")

async def main():
    print(f"Starting test simulation for user: {TEST_USER_ID}")
    
    # Send events
    for event in TEST_EVENTS:
        await send_event(event)
        await asyncio.sleep(0.5) # Small gap
    
    print("\nEvents sent. Waiting for async processing (Celery + LLM)...")
    await asyncio.sleep(10) # Wait for LLM and worker
    
    # Check memory
    await get_memory(TEST_USER_ID)

if __name__ == "__main__":
    asyncio.run(main())
