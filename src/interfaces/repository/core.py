from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

from fastapi_pagination import LimitOffsetPage
from pydantic import BaseModel
from sqlalchemy import BinaryExpression
from sqlalchemy.sql.base import ExecutableOption

from common.filters import CoreFilter


T = TypeVar("T")


class ICoreRepository(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    async def get_by_sid(
        self, sid: UUID, custom_options: list[ExecutableOption] | None = None
    ) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_label(
        self, label: UUID, custom_options: list[ExecutableOption] | None = None
    ) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by(
        self,
        filter_expression: BinaryExpression | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def get_all(
        self,
        filter_params: CoreFilter | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    async def get_all_by(
        self,
        filter_expression: BinaryExpression | None = None,
        filter_params: CoreFilter | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    async def get_few(
        self,
        limit: int,
        offset: int,
        filter_params: CoreFilter | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        raise NotImplementedError

    async def get_few_by(
        self,
        limit: int,
        offset: int,
        filter_params: CoreFilter | None = None,
        filter_expression: BinaryExpression | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    async def get_pagination(
        self,
        filter_params: CoreFilter | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> LimitOffsetPage[T]:
        raise NotImplementedError

    @abstractmethod
    async def get_pagination_by(
        self,
        filter_params: CoreFilter | None = None,
        filter_expression: BinaryExpression | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> LimitOffsetPage[T]:
        raise NotImplementedError

    @abstractmethod
    async def create(
        self, obj_in: dict | BaseModel, with_commit: bool = True
    ) -> T:
        raise NotImplementedError

    @abstractmethod
    async def update(
        self, obj: T, obj_in: dict | BaseModel, with_commit: bool = True
    ) -> T:
        raise NotImplementedError

    @abstractmethod
    async def remove(self, obj: T, with_commit: bool = True) -> None:
        raise NotImplementedError
