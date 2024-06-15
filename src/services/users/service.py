from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from common.managers import SecurityManager
from config.exceptions import APIException
from models import users as user_models
from schemas import users as user_schemas
from services.core import CoreService

from .utils import UserServiceUtils


class UserService(CoreService):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
        self._utils = UserServiceUtils(pg_db)

    async def get_user_by_email(
        self,
        email: str,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> user_models.User | None:
        user = await self.pg_repository.user.get_by_email(
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

    async def create_user(
        self,
        user_in: user_schemas.UserCreate,
        with_commit: bool = True,
    ) -> user_models.User:
        user = await self.pg_repository.user.create(
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

    async def update_user_password(
        self, user: user_models.User, password: str, with_commit: bool = True
    ) -> user_models.User:
        return await self.pg_repository.user.update_user_password(
            user=user,
            hashed_password=SecurityManager.get_password_hash(password),
            with_commit=with_commit,
        )
