from typing import Literal

from pydantic import Field

from ..core import EnvCoreSettings


class RedisSettings(EnvCoreSettings):
    HOST: str = Field(..., alias="REDIS_HOST")
    PORT: int = Field(..., alias="REDIS_PORT")

    ENCODING: str = "utf-8"
    DECODE: Literal[True] = True

    TOKEN_DB: int = 0
