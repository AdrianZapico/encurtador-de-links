from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import UserCreate, UserOut, UserInDB
from app.core.security import hash_password, verify_password, create_access_token
from app.db import db  
from datetime import datetime

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate):
    # Verificar se já existe
    user_exists = await db["users"].find_one({"email": user_in.email})
    if user_exists:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")

    # Criptografar senha
    hashed = hash_password(user_in.password)
    
    # Criar o dicionário dos dados
    user_dict = {
        "username": user_in.username,
        "email": user_in.email,
        "hashed_password": hashed,
        "created_at": datetime.utcnow()
    }

    # Salvar no Atlas
    result = await db["users"].insert_one(user_dict)
    
    # Adicionar o ID gerado de volta ao dicionário para o UserOut ler
    user_dict["_id"] = str(result.inserted_id)
    
    return user_dict
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # 1. Buscar usuário por e-mail (ou username) no Atlas
    user = await db["users"].find_one({"email": form_data.username})
    
    # 2. Validar existência e senha
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos."
        )

    # 3. Gerar o Token de acesso
    access_token = create_access_token(data={"sub": user["email"]})
    
    return {"access_token": access_token, "token_type": "bearer"}