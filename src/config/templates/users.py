from config.settings import settings
from models.security import enums
from models.users import schemas


class UserTemplate:
    @staticmethod
    def get_superuser() -> schemas.UserCreate:
        return schemas.UserCreate(
            first_name=settings.user.SUPERUSER_FIRST_NAME,
            last_name=settings.user.SUPERUSER_LAST_NAME,
            email=settings.user.SUPERUSER_EMAIL,
            password=settings.user.SUPERUSER_PASSWORD,
            role_label=enums.RoleLabel.SUPERUSER,
        )
