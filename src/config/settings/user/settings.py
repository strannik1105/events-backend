from pydantic import EmailStr, Field

from ..core import EnvCoreSettings


class UserSettings(EnvCoreSettings):
    SUPERUSER_FIRST_NAME: str = "Asu"
    SUPERUSER_LAST_NAME: str = "Events"
    SUPERUSER_EMAIL: EmailStr = Field(...)
    SUPERUSER_PASSWORD: str = Field()
