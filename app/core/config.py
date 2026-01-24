from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # O Pydantic procura automaticamente por essas chaves no arquivo .env
    PROJECT_NAME: str = "Encurtador de Links"
    MONGO_URL: str = "mongodb://localhost:27017"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    class Config:
        env_file = ".env"

settings = Settings()