from fastapi import APIRouter, HTTPException, status
from app.models.link import Link, LinkCreate
from app.core.utils import generate_short_code
from app.db import db, redis_client
from datetime import datetime
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.post("/", response_model=Link, status_code=status.HTTP_201_CREATED)
async def create_short_link(link_in: LinkCreate):

    short_code = generate_short_code()
    
 
    new_link = {
        "target_url": str(link_in.target_url),
        "short_code": short_code,
        "clicks": 0,
        "created_at": datetime.utcnow()
    }
    
    await db.links.insert_one(new_link)
    
  
    return Link(**new_link)

@router.get("/{code}")
async def redirect_to_url(code: str):
    
    link_data = await db.links.find_one({"short_code": code.strip()})
    
    if not link_data:
        raise HTTPException(status_code=404, detail="Link não encontrado")
    
   
    await db.links.update_one(
        {"short_code": code.strip()}, 
        {"$inc": {"clicks": 1}}
    )
    
   
    return RedirectResponse(url=link_data["target_url"])