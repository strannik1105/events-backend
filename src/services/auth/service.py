from typing import Any

import bcrypt
from sqlalchemy.ext.asyncio import AsyncSession

from config.exceptions import APIException
from services.core import CoreService


class AuthService(CoreService):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)

    async def authenticate(
        self, db_session: AsyncSession, username: str, password: str
    ) -> Any:
        user = await self._auth_repository.get_user_by_username(
            db_session, username
        )

        if not user:
            raise APIException.unauthorized

        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            raise APIException.unauthorized

        return user
