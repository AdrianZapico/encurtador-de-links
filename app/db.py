from motor.motor_asyncio import AsyncIOMotorClient
import redis.asyncio as redis # Importe a versão assíncrona
from app.core.config import settings

# MongoDB
client = AsyncIOMotorClient(settings.MONGO_URL)
db = client.encurtador_db

# Redis
redis_client = redis.Redis(
    host=settings.REDIS_HOST, 
    port=settings.REDIS_PORT, 
    decode_responses=True # Isso faz o Redis retornar strings em vez de bytes
)