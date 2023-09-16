import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


Base_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))  # backend/app/core/config.py -> backend/
load_dotenv(os.path.join(Base_DIR, '.env'))


class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv('PROJECT_NAME')
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    API_PREFIX: str = os.getenv('API_PREFIX')
    BACKEND_CORS_ORIGINS: list = ['*']
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # 7 days
    LOGGING_CONFIG: str = os.path.join(Base_DIR, 'logging.ini')
    DATABASE_URL: str = os.getenv('SQL_DATABASE_URL')


settings = Settings()
