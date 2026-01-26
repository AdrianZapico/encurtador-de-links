from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

# Configuração do algoritmo de criptografia
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "SUA_CHAVE_SUPER_SECRETA_AQUI" # Mude isso depois!
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30) # Token dura 30 min
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)