from abc import ABCMeta, abstractmethod
from typing import Any

from common.db.postgres.base import PostgresBaseModel


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

class ICrudService(metaclass=ABCMeta):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_sid(self):
        pass

    @abstractmethod
    def create(self, obj_instance: PostgresBaseModel):
        pass

    @abstractmethod
    def update(self, obj_instance: PostgresBaseModel):
        pass

    @abstractmethod
    def delete(self, obj_instance: PostgresBaseModel):
        pass