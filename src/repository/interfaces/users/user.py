from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import Generic, TypeVar

from sqlalchemy.sql.base import ExecutableOption

from repository.interfaces.core import ICoreRepository


T = TypeVar("T")


class IUserRepository(Generic[T], ICoreRepository[T], metaclass=ABCMeta):
    @abstractmethod
    async def get_by_email(
        self, email: str, custom_options: list[ExecutableOption] | None = None
    ) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def update_user_password(
        self, user: T, hashed_password: str, with_commit: bool = True
    ) -> T:
        raise NotImplementedError

    @abstractmethod
    async def update_user_verify(
        self, user: T, is_verify: bool, with_commit: bool = True
    ) -> T:
        raise NotImplementedError

    @abstractmethod
    async def update_user_active(
        self, user: T, is_active: bool, with_commit: bool = True
    ) -> T:
        raise NotImplementedError

    @abstractmethod
    async def update_last_login_at(
        self,
        user: T,
        last_login_at: datetime | None,
        with_commit: bool = True,
    ) -> T:
        raise NotImplementedError
