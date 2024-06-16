from pydantic import Field

from ..core import EnvCoreSettings


class JWTSettings(EnvCoreSettings):
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = Field(..., alias="JWT_SECRET_KEY")

    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 15
    REFRESH_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 30
    DEACTIVATE_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7
