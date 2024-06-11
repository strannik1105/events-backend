from pydantic import Field, field_validator
from pydantic_core.core_schema import ValidationInfo

from ..core import EnvCoreSettings


class AppSettings(EnvCoreSettings):
    HOST: str = Field(...)
    PORT: int = Field(...)

    V1: str = "/api/v1"

    VERSION: str = "1.0.0"
    NAME: str = "Events Platform"

    WORKERS_NUM: int = Field(...)

    MODE: str = Field(...)
    LOCAL_MODE: bool | None = None
    TEST_MODE: bool | None = None
    PROD_MODE: bool | None = None

    @field_validator("LOCAL_MODE", mode="before")
    def assemble_local_mode(
        cls, v: bool | None, values: ValidationInfo
    ) -> bool:
        if isinstance(v, bool):
            return v
        return values.data.get("MODE") == "local"

    @field_validator("TEST_MODE", mode="before")
    def assemble_test_mode(
        cls, v: bool | None, values: ValidationInfo
    ) -> bool:
        if isinstance(v, bool):
            return v
        return values.data.get("MODE") == "test"

    @field_validator("PROD_MODE", mode="before")
    def assemble_prod_mode(
        cls, v: bool | None, values: ValidationInfo
    ) -> bool:
        if isinstance(v, bool):
            return v
        return values.data.get("MODE") == "prod"
