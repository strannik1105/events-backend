from pydantic import BaseModel, EmailStr, field_validator


class Email(BaseModel):
    email: EmailStr

    @field_validator("email", mode="after")
    def validate_email(cls, v: str) -> str:
        return v.strip().lower()
