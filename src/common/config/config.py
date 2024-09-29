from pydantic_settings import BaseSettings

from common.singleton import Singleton


class Config(Singleton, BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # POSTGRES
    POSTGRES_USER: str = "events"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "events"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432

    # TELEGRAM
    TG_API_TOKEN: str = "7965879569:AAFnoTLPsrMalvsYXCbAXjK7FdIyTrDcVWs"
    TG_CHANNEL_ID: str = "-1002356469022"
