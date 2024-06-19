from pydantic import Field

from ..core import EnvCoreSettings


class MinioSettings(EnvCoreSettings):
    ADDR: str = Field(..., alias="MINIO_ADDR")
    USER: str = Field(..., alias="MINIO_ROOT_USER")
    PASS: str = Field(..., alias="MINIO_ROOT_PASSWORD")
