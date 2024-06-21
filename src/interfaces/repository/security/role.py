from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy.sql.base import ExecutableOption

from filters import security as security_filters
from interfaces.repository.core import ICoreRepository


T = TypeVar("T")


class IRoleRepository(Generic[T], ICoreRepository[T], metaclass=ABCMeta):
    @abstractmethod
    async def get_all_by_filter(
        self,
        filter_params: security_filters.RoleFilter,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        raise NotImplementedError
