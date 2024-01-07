import secrets
import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from pydantic import (
    BaseSettings,
    validator,
)

# load .env from project
load_dotenv()


# BaseSettings get data from .env
class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv('PROJECT_NAME')
    API_VERSION: str = os.getenv('API_VERSION')
    PROXY_ROOT_PATH: str = os.getenv('PROXY_ROOT_PATH')
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEFAULT_PAGESIZE: int = 10
    POSTGRES_DB_SERVER: str = os.getenv('POSTGRES_DB_SERVER')
    POSTGRES_DB_API_USER: str = os.getenv('POSTGRES_DB_API_USER')
    POSTGRES_DB_API_PASSWORD: str = os.getenv('POSTGRES_DB_API_PASSWORD')
    POSTGRES_DB_API: str = os.getenv('POSTGRES_DB_API')
    POSTGRES_DB_EXPOSE_PORT: str = os.getenv('POSTGRES_DB_EXPOSE_PORT')

    SQLALCHEMY_WITH_DRIVER_URI: Optional[str] = None

    @validator("SQLALCHEMY_WITH_DRIVER_URI", pre=True)
    def postgresql_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v

        # dialect[+driver]://user:password@host/dbname[?key=value..]
        scheme = "postgresql"
        driver = "asyncpg"
        user = values.get("POSTGRES_DB_API_USER")
        password = values.get("POSTGRES_DB_API_PASSWORD")
        host = values.get("POSTGRES_DB_SERVER")
        database = values.get("POSTGRES_DB_API")
        return "{}+{}://{}:{}@{}/{}".format(scheme, driver, user, password, host, database)

    # --

    ENVIRONMENT: str = 'dev'
    TESTING: bool = False

settings = Settings()