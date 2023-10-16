import secrets
from pydantic_settings import BaseSettings

class Settings(BaseSettings):


    SQLALCHEMY_DATABASE_URI: str
    PROJECT_NAME: str
    PROJECT_V1_NAME: str
    DEBUG: bool = True


    # CORS
    ALLOW_ORIGINS: list = ["*"]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list = ["*"]
    ALLOW_HEADERS: list = ["*"]

    class Config:

        env_file = ".env"


settings = Settings()
