from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Encurtador de Links"
    MONGO_URL: str  

    class Config:
        env_file = ".env"

settings = Settings()