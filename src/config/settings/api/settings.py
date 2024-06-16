from pydantic import Field

from ..core import EnvCoreSettings


class ApiSettings(EnvCoreSettings):
    HOST: str = Field(...)
    PORT: int = Field(...)

    V1: str = "/api/v1"
    OPENAPI_URL: str = "openapi.json"
