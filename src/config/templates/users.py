from config.settings import settings
from enums import security as security_enums
from schemas import users as user_schemas


class UserTemplate:
    @staticmethod
    def get_superuser() -> user_schemas.UserDTOCreate:
        return user_schemas.UserDTOCreate(
            first_name=settings.user.SUPERUSER_FIRST_NAME,
            last_name=settings.user.SUPERUSER_LAST_NAME,
            email=settings.user.SUPERUSER_EMAIL,
            password=settings.user.SUPERUSER_PASSWORD,
            role_label=security_enums.RoleLabel.SUPERUSER,
        )
