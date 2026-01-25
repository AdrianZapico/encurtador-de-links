from fastapi import APIRouter, HTTPException, status
from app.models.link import Link, LinkCreate
from app.core.utils import generate_short_code
from app.db import db, redis_client
from datetime import datetime
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.post("/", response_model=Link, status_code=status.HTTP_201_CREATED)
async def create_short_link(link_in: LinkCreate):
    # 1. Gerar um código único
    short_code = generate_short_code()
    
    # 2. Preparar o documento para o Mongo
    new_link = {
        "target_url": str(link_in.target_url),
        "short_code": short_code,
        "clicks": 0,
        "created_at": datetime.utcnow()
    }
    
    await db.links.insert_one(new_link)
    
    # RETORNO CORRIGIDO:
    # Transformamos o dicionário em uma instância do modelo Link
    # Isso limpa o campo _id que o MongoDB injeta automaticamente
    return Link(**new_link)

@router.get("/{code}")
async def redirect_to_url(code: str):
    # 1. Busca o link no MongoDB pelo short_code
    # Usamos o strip() para garantir que espaços não quebrem a busca
    link_data = await db.links.find_one({"short_code": code.strip()})
    
    if not link_data:
        raise HTTPException(status_code=404, detail="Link não encontrado")
    
    # 2. Incrementa o contador de cliques no banco
    await db.links.update_one(
        {"short_code": code.strip()}, 
        {"$inc": {"clicks": 1}}
    )
    
    # 3. Redireciona o usuário para a URL original
    return RedirectResponse(url=link_data["target_url"])