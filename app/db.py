from motor.motor_asyncio import AsyncIOMotorClient
import redis.asyncio as redis # Importe a versão assíncrona
from app.core.config import settings

# MongoDB
client = AsyncIOMotorClient(settings.MONGO_URL)
db = client.encurtador_db

