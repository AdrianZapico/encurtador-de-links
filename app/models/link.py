from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime
from typing import Optional

class LinkBase(BaseModel):
    # Usamos HttpUrl para o Pydantic validar se é uma URL real (com http/https)
    target_url: HttpUrl 

class LinkCreate(LinkBase):
    # Este modelo é o que o usuário envia no POST
    pass

class Link(LinkBase):
    # Este é o modelo que representa o dado no Banco de Dados
    short_code: str
    clicks: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    # Opcional: expiração do link
    expires_at: Optional[datetime] = None

    class Config:
        # Permite que o Pydantic trabalhe com dicionários do MongoDB (_id)
        from_attributes = True