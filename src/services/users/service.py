from datetime import datetime
from uuid import UUID

from fastapi_pagination import LimitOffsetPage
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from common.security import SecurityCrypto
from config.exceptions import APIException
from models import users as user_models
from schemas import users as user_schemas
from services.core import CoreService

from .utils import UserServiceUtils


class UserService(CoreService):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
        self._utils = UserServiceUtils(pg_db)

    async def get_user_by_sid(
        self,
        sid: UUID,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> user_models.User | None:
        user = await self.repository.user.get_by_sid(
            sid=sid, custom_options=custom_options
        )
        if validate:
            await self._utils.exists_validate(
                obj=user,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.user_already_exists,
                not_found_exception=APIException.user_not_found,
            )
        return user

    async def get_user_by_email(
        self,
        email: str,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> user_models.User | None:
        user = await self.repository.user.get_by_email(
            email=email, custom_options=custom_options
        )
        if validate:
            await self._utils.exists_validate(
                obj=user,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.user_already_exists,
                not_found_exception=APIException.user_not_found,
            )
        return user

    async def get_users(
        self,
        custom_options: list[ExecutableOption] | None = None,
    ) -> LimitOffsetPage[user_models.User]:
        return await self.repository.user.get_pagination(
            custom_options=custom_options,
        )

    async def create_user(
        self,
        user_in: user_schemas.UserCreate,
        with_commit: bool = True,
    ) -> user_models.User:
        user = await self.repository.user.create(
            obj_in=user_schemas.UserCreateWithoutPassword.model_validate(
                user_in.model_dump()
            ),
            with_commit=with_commit,
        )
        return await self.update_user_password(
            user=user,
            password=user_in.password,
            with_commit=with_commit,
        )

    async def create_verify_user(
        self,
        user_in: user_schemas.UserCreate,
        with_commit: bool = True,
    ) -> user_models.User:
        user = await self.repository.user.create(
            obj_in=user_schemas.UserCreateWithoutPassword.model_validate(
                user_in.model_dump()
            ),
            with_commit=with_commit,
        )
        user = await self.update_user_verify(
            user=user,
            is_verify=True,
            with_commit=with_commit,
        )
        return await self.update_user_password(
            user=user,
            password=user_in.password,
            with_commit=with_commit,
        )

    async def update_user(
        self,
        user: user_models.User,
        user_in: user_schemas.UserUpdate,
        with_commit: bool = True,
    ) -> user_models.User:
        return await self.repository.user.update(
            obj=user,
            obj_in=user_in,
            with_commit=with_commit,
        )

    async def update_user_password(
        self, user: user_models.User, password: str, with_commit: bool = True
    ) -> user_models.User:
        return await self.repository.user.update_user_password(
            user=user,
            hashed_password=SecurityCrypto.get_password_hash(password),
            with_commit=with_commit,
        )

    async def update_user_verify(
        self, user: user_models.User, is_verify: bool, with_commit: bool = True
    ) -> user_models.User:
        return await self.repository.user.update_user_verify(
            user=user,
            is_verify=is_verify,
            with_commit=with_commit,
        )

    async def update_user_active(
        self, user: user_models.User, is_active: bool, with_commit: bool = True
    ) -> user_models.User:
        return await self.repository.user.update_user_active(
            user=user,
            is_active=is_active,
            with_commit=with_commit,
        )

    async def update_last_login_at(
        self,
        user: user_models.User,
        last_login_at: datetime | None,
        with_commit: bool = True,
    ) -> user_models.User:
        return await self.repository.user.update_last_login_at(
            user=user,
            last_login_at=last_login_at,
            with_commit=with_commit,
        )

    async def remove_user(
        self,
        user: user_models.User,
        with_commit: bool = True,
    ) -> None:
        return await self.repository.user.remove(
            obj=user,
            with_commit=with_commit,
        )
