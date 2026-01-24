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
    
    # 3. Salvar no Banco
   await db.links.insert_one(new_link)
    
    # --- ONDE VOCÊ DEVE ALTERAR ---
    # Em vez de 'return new_link', use:
    return Link(**new_link)

@router.get("/{code}")
async def redirect_to_url(code: str):
    # 1. Busca o link no MongoDB pelo short_code
    link_data = await db.links.find_one({"short_code": code})
    
    if not link_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Link não encontrado"
        )
    
    # 2. Incrementa o contador de cliques no banco
    await db.links.update_one(
        {"short_code": code}, 
        {"$inc": {"clicks": 1}}
    )
    
    # 3. Redireciona o usuário para a URL original
    return RedirectResponse(url=link_data["target_url"])