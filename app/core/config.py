from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PINECONE_API_KEY: str
    PINECONE_INDEX_NAME: str
    REDIS_URL: str
    DATABASE_URL: str
    GEMINI_API_KEY: str 

    class Config:
        env_file = ".env"

settings = Settings()