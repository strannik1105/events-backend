from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy.sql.base import ExecutableOption

from interfaces.repository.core import ICoreRepository


T = TypeVar("T")


class IEventFileTypeRepository(
    Generic[T], ICoreRepository[T], metaclass=ABCMeta
):
    @abstractmethod
    async def get_by_name(
        self, name: str, custom_options: list[ExecutableOption] | None = None
    ) -> T | None:
        raise NotImplementedError
