from fastapi import FastAPI
from app.core.config import settings
from app.db import client
from app.api.v1.endpoints.links import router as links_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(links_router, prefix="/api/v1/links", tags=["links"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem (para desenvolvimento)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
    # Verifica se a conexão com o Mongo está funcionando ao iniciar
    try:
        await client.admin.command('ping')
        print("✅ Conectado ao MongoDB com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao conectar ao MongoDB: {e}")

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()

@app.get("/")
async def root():
    return {"message": f"Bem-vindo ao {settings.PROJECT_NAME}", "status": "online"}