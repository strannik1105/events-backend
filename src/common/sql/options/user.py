from sqlalchemy.orm import selectinload
from sqlalchemy.sql.base import ExecutableOption

from models import security as security_models
from models import users as user_models


class SQLUserOptions:
    @staticmethod
    def permissions() -> list[ExecutableOption]:
        return [
            selectinload(user_models.User.role).selectinload(
                security_models.Role.permissions
            )
        ]
