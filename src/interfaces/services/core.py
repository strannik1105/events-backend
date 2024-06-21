from abc import ABCMeta, abstractmethod
from typing import Any


class ICoreService(metaclass=ABCMeta):
    pass


class ICoreServiceUtils(metaclass=ABCMeta):
    @abstractmethod
    async def exists_validate(
        self,
        obj: Any | None,
        is_exists: bool,
        is_rollback: bool,
        exists_exception: Exception,
        not_found_exception: Exception,
    ) -> None:
        raise NotImplementedError
