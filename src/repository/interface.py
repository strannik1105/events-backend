from abc import ABCMeta, abstractmethod
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import BinaryExpression
from sqlalchemy.sql.base import ExecutableOption


class IRepository[T](metaclass=ABCMeta):
    @abstractmethod
    def get_by_sid(
        self, sid: UUID, custom_options: list[ExecutableOption] | None = None
    ) -> T | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_label(
        self, label: int, custom_options: list[ExecutableOption] | None = None
    ) -> T | None:
        raise NotImplementedError

    @abstractmethod
    def get_by(
        self,
        filter_expression: BinaryExpression | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> T | None:
        raise NotImplementedError

    @abstractmethod
    def get_all(
        self, custom_options: list[ExecutableOption] | None = None
    ) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def get_few(
        self,
        limit: int,
        offset: int,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def create(self, obj_in: T | BaseModel, with_commit: bool = True) -> T:
        raise NotImplementedError

    @abstractmethod
    def update(
        self, obj: T, obj_in: dict | BaseModel, with_commit: bool = True
    ) -> T:
        raise NotImplementedError

    @abstractmethod
    def remove(self, obj: T, with_commit: bool = True) -> None:
        raise NotImplementedError
