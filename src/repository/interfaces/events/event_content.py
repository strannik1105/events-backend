from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

from sqlalchemy.sql.base import ExecutableOption

from repository.interfaces.core import ICoreRepository


T = TypeVar("T")


class IEventContentRepository(
    Generic[T], ICoreRepository[T], metaclass=ABCMeta
):
    @abstractmethod
    async def get_all_by_event_sid(
        self,
        event_sid: UUID,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        raise NotImplementedError
