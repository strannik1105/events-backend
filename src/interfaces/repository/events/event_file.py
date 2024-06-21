from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy.sql.base import ExecutableOption

from common import schemas as common_schemas
from interfaces.repository.core import ICoreRepository


T = TypeVar("T")


class IEventFileRepository(Generic[T], ICoreRepository[T], metaclass=ABCMeta):
    @abstractmethod
    async def get_all_by_event_sids(
        self,
        event_sids: common_schemas.EventSids,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        raise NotImplementedError
