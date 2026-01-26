from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import UserCreate, UserOut, UserInDB
from app.core.security import hash_password, verify_password, create_access_token
from app.db.mongodb import db # Assumindo que sua conexão está aqui
from datetime import datetime

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate):
    # 1. Verificar se o usuário já existe no MongoDB Atlas
    user_exists = await db["users"].find_one({"email": user_in.email})
    if user_exists:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")

    # 2. Criptografar a senha e preparar o documento
    hashed = hash_password(user_in.password)
    user_dict = UserInDB(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed
    ).dict()

    # 3. Salvar no Banco
    new_user = await db["users"].insert_one(user_dict)
    
    # 4. Retornar os dados (o Pydantic filtrará a senha automaticamente)
    return {**user_dict, "_id": str(new_user.inserted_id)}

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