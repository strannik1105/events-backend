from sqlalchemy.orm import selectinload
from sqlalchemy.sql.base import ExecutableOption

from models import events as event_models
from models import security as security_models


class SQLEventPullOptions:
    @staticmethod
    def permissions() -> list[ExecutableOption]:
        return [
            selectinload(event_models.EventPull.role).selectinload(
                security_models.Role.permissions
            )
        ]
