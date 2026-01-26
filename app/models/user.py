from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# Schema para a criação de um novo usuário (O que o Front-end envia)
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

# Schema para o retorno da API (O que o Front-end recebe - SEM A SENHA!)
class UserOut(BaseModel):
    id: str = Field(..., alias="_id") # Mapeia o _id do MongoDB
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        populate_by_name = True # Permite usar o alias _id como id
        from_attributes = True

# Schema interno para o Banco de Dados (Como salvamos no MongoDB)
class UserInDB(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)