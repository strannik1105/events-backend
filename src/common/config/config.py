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
    

class S3StorageSettings(BaseSettings):
    endpoint: str | None = 'localhost:9000'
    bucket_name: str = 'events'
    access_key: str | None = None
    secret_key: str | None = None
    session_token: str | None = None
    secure: bool = False
    region: str | None = None
