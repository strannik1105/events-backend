from abc import ABCMeta, abstractmethod
from datetime import datetime
from uuid import UUID

from fastapi_pagination import LimitOffsetPage
from sqlalchemy.sql.base import ExecutableOption

from interfaces.services.core import ICoreService
from models import users as user_models
from schemas import users as user_schemas


class IUserService(ICoreService, metaclass=ABCMeta):
    @abstractmethod
    async def get_user_by_sid(
        self,
        sid: UUID,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> user_models.User | None:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_email(
        self,
        email: str,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> user_models.User | None:
        raise NotImplementedError

    @abstractmethod
    async def get_users(
        self,
        custom_options: list[ExecutableOption] | None = None,
    ) -> LimitOffsetPage[user_models.User]:
        raise NotImplementedError

    @abstractmethod
    async def create_user(
        self,
        user_in: user_schemas.UserDTOCreate,
        with_commit: bool = True,
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def create_verify_user(
        self,
        user_in: user_schemas.UserDTOCreate,
        with_commit: bool = True,
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def update_user(
        self,
        user: user_models.User,
        user_in: user_schemas.UserDTOUpdate,
        with_commit: bool = True,
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def update_user_password(
        self, user: user_models.User, password: str, with_commit: bool = True
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def update_user_verify(
        self, user: user_models.User, is_verify: bool, with_commit: bool = True
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def update_user_active(
        self, user: user_models.User, is_active: bool, with_commit: bool = True
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def update_last_login_at(
        self,
        user: user_models.User,
        last_login_at: datetime | None,
        with_commit: bool = True,
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def remove_user(
        self,
        user: user_models.User,
        with_commit: bool = True,
    ) -> None:
        raise NotImplementedError
