import re

from pydantic import BaseModel, Field, field_validator

from config.settings import settings


class Password(BaseModel):
    password: str = Field(..., description="Any password")


class CreatePassword(BaseModel):
    password: str = Field(
        ...,
        min_length=settings.auth.PASSWORD_LENGTH,
    )

    @field_validator("password", mode="after")
    def validate_password(cls, v: str) -> str:
        check = re.match(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]",
            v,
        )
        assert check, "Invalid password format"
        return v
