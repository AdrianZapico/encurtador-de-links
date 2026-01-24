from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

# Inicializa o cliente usando a URL do nosso .env
client = AsyncIOMotorClient(settings.MONGO_URL)

# Define o banco de dados principal
db = client.encurtador_db