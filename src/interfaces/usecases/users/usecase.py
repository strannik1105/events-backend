from abc import ABCMeta, abstractmethod
from uuid import UUID

from fastapi_pagination import LimitOffsetPage

from common import schemas as common_schemas
from interfaces.usecases.core import ICoreUseCase
from models import users as user_models
from schemas import users as user_schemas


class IUserUseCase(ICoreUseCase, metaclass=ABCMeta):
    @abstractmethod
    async def get_user_by_sid(self, user_sid: UUID) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def get_users(self) -> LimitOffsetPage[user_models.User]:
        raise NotImplementedError

    @abstractmethod
    async def update_me(
        self,
        current_user: user_schemas.CurrentUser,
        user_in: user_schemas.UserDTOUpdate,
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def update_user_active(
        self,
        current_user: user_schemas.CurrentUser,
        user_sid: UUID,
        is_active: bool,
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def update_user_verify(
        self,
        current_user: user_schemas.CurrentUser,
        user_sid: UUID,
        is_verify: bool,
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def update_user(
        self,
        current_user: user_schemas.CurrentUser,
        user_sid: UUID,
        user_in: user_schemas.UserDTOUpdate,
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def create_user(
        self, user_in: user_schemas.UserDTOCreate
    ) -> user_models.User:
        raise NotImplementedError

    @abstractmethod
    async def remove_user(
        self,
        current_user: user_schemas.CurrentUser,
        user_sid: UUID,
    ) -> common_schemas.Msg:
        raise NotImplementedError
