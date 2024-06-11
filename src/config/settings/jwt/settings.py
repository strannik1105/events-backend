from pydantic import Field

from ..core import EnvCoreSettings


class JWTSettings(EnvCoreSettings):
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = Field(..., alias="JWT_SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
