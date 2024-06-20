from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy.sql.base import ExecutableOption

from repository.interfaces.core import ICoreRepository


T = TypeVar("T")


class IRoleXResourceRepository(
    Generic[T], ICoreRepository[T], metaclass=ABCMeta
):
    @abstractmethod
    async def get_by_labels(
        self,
        role_label: int,
        resource_label: int,
        custom_options: list[ExecutableOption] | None = None,
    ) -> T | None:
        raise NotImplementedError
