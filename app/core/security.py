import bcrypt
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "SUA_CHAVE_SUPER_SECRETA_AQUI"
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    # Transforma a senha em bytes, gera o salt e faz o hash
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_password.decode('utf-8') # Salva como string no banco

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Compara a senha digitada com o hash do banco
    password_byte = plain_password.encode('utf-8')
    hashed_byte = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_byte, hashed_byte)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)