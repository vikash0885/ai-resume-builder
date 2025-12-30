from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Resume Builder"
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "resume_builder"
    GEMINI_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
