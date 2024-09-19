from pydantic_settings import BaseSettings

from common.singleton import Singleton


class Config(Singleton, BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # POSTGRES
    POSTGRES_USER: str = "POSTGRES_USER"
    POSTGRES_PASSWORD: str = "POSTGRES_PASSWORD"
    POSTGRES_DB: str = "POSTGRES_DB"
    POSTGRES_HOST: str = "POSTGRES_HOST"
    POSTGRES_PORT: int = 5432
