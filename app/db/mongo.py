"""
Event Memory System MongoDB Connector
Handles the asynchronous connection to our primary behavioral database.
"""

from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

# Initialize the Async MongoDB Client using the URI from our environment
client = AsyncIOMotorClient(settings.MONGODB_URI)

# We use a dedicated database 'event_memory_db' to separate our data from 
# other potential apps in the cluster.
db = client["event_memory_db"]

async def get_database():
    """Returns the active database instance."""
    return db
