from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy.sql.base import ExecutableOption

from common import schemas as common_schemas
from interfaces.repository.core import ICoreRepository


T = TypeVar("T")


class IEventPullRepository(Generic[T], ICoreRepository[T], metaclass=ABCMeta):
    @abstractmethod
    async def get_by_event_sids(
        self,
        event_sids: common_schemas.EventSids,
        custom_options: list[ExecutableOption] | None = None,
    ) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_event_user_sids(
        self,
        event_user_sids: common_schemas.EventUserSids,
        custom_options: list[ExecutableOption] | None = None,
    ) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_sids(
        self,
        event_pull_sids: common_schemas.EventPullSids,
        custom_options: list[ExecutableOption] | None = None,
    ) -> T | None:
        raise NotImplementedError
