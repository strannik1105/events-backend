from functools import lru_cache

from .api import ApiSettings
from .app import AppSettings
from .auth import AuthSettings
from .jwt import JWTSettings
from .log import LogSettings
from .minio import MinioSettings
from .postgres import PostgresSettings
from .redis import RedisSettings
from .s3 import S3Settings
from .tz import TZSettings
from .unit import UnitSettings
from .user import UserSettings


class Settings:
    app = AppSettings()
    api = ApiSettings()
    postgres = PostgresSettings()
    redis = RedisSettings()
    minio = MinioSettings()
    log = LogSettings()
    unit = UnitSettings()
    tz = TZSettings()
    jwt = JWTSettings()
    auth = AuthSettings()
    user = UserSettings()
    s3 = S3Settings()


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
