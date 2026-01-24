from fastapi import APIRouter, HTTPException, status
from app.models.link import Link, LinkCreate
from app.core.utils import generate_short_code
from app.db import db
from datetime import datetime

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
    
    return new_link