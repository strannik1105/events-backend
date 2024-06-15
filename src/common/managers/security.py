from uuid import UUID

from passlib.context import CryptContext

from config.exceptions import APIException
from models.security import enums


class SecurityManager:
    _pwd_context = CryptContext(schemes=["bcrypt"])

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls._pwd_context.hash(password)

    @classmethod
    def verify_password(cls, password: str, hashed_password: str) -> bool:
        return cls._pwd_context.verify(password, hashed_password)

    @staticmethod
    async def validate_user_permission(
        permission: enums.PermissionLabel,
        action: enums.PermissionAccessAction,
        user_sid: UUID,
        event_sid: UUID | None = None,
        is_raise: bool = True,
    ) -> bool | None:
        if is_raise:
            raise APIException.not_allowed
        return True
