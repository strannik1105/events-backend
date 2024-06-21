from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from models.users import User
from interfaces.repository.users import IUserRepository
from repository.postgres.core import CoreRepository


class UserRepository(IUserRepository[User], CoreRepository[User]):
    def __init__(self, db: AsyncSession, model: type[User]) -> None:
        super().__init__(db, model)

    async def get_by_email(
        self, email: str, custom_options: list[ExecutableOption] | None = None
    ) -> User | None:
        return await self.get_by(
            filter_expression=self._model.email == email,
            custom_options=custom_options,
        )

    async def update_user_password(
        self, user: User, hashed_password: str, with_commit: bool = True
    ) -> User:
        user.hashed_password = hashed_password
        if with_commit:
            await self._db.commit()
            await self._db.refresh(user)
        else:
            await self._db.flush()
        return user

    async def update_user_verify(
        self, user: User, is_verify: bool, with_commit: bool = True
    ) -> User:
        user.is_verify = is_verify
        if with_commit:
            await self._db.commit()
            await self._db.refresh(user)
        else:
            await self._db.flush()
        return user

    async def update_user_active(
        self, user: User, is_active: bool, with_commit: bool = True
    ) -> User:
        user.is_active = is_active
        if with_commit:
            await self._db.commit()
            await self._db.refresh(user)
        else:
            await self._db.flush()
        return user

    async def update_last_login_at(
        self,
        user: User,
        last_login_at: datetime | None,
        with_commit: bool = True,
    ) -> User:
        user.last_login_at = last_login_at
        if with_commit:
            await self._db.commit()
            await self._db.refresh(user)
        else:
            await self._db.flush()
        return user
