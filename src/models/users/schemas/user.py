from datetime import datetime
from uuid import UUID

from pydantic import Field, field_validator

from common.schemas import CoreModel, CreatePassword, DateTimeMixin, Email, Sid


class UserBase(CoreModel):
    first_name: str = Field(..., description="User first name")
    middle_name: str | None = Field(None, description="User middle name")
    last_name: str = Field(..., description="User last name")

    @field_validator("first_name", mode="after")
    def validate_first_name(cls, v: str) -> str:
        return v.strip()

    @field_validator("middle_name", mode="after")
    def validate_middle_name(cls, v: str | None) -> str | None:
        if v is not None:
            return v.strip()
        return v

    @field_validator("last_name", mode="after")
    def validate_last_name(cls, v: str) -> str:
        return v.strip()


class UserCreate(UserBase, Email, CreatePassword):
    role_label: UUID = Field(..., description="Role label")


class UserUpdate(UserBase):
    pass


class User(UserBase, Sid, Email, DateTimeMixin):
    telegram_id: int | None = Field(None, description="User telegram id")
    is_active: bool = Field(True, description="User active status")
    is_verified: bool = Field(True, description="User verified status")
    last_login_at: datetime = Field(..., description="User last login at")
    role_label: UUID = Field(..., description="Role label")
