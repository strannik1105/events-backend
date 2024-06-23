from typing import Generic, TypeVar
from uuid import UUID

from fastapi_pagination import LimitOffsetPage
from fastapi_pagination.ext.sqlalchemy import paginate
from pydantic import BaseModel
from sqlalchemy import BinaryExpression, Result, Select, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Query
from sqlalchemy.sql.base import ExecutableOption

from common.db.postgres import PostgresBaseModel
from common.filters import CoreFilter
from interfaces.repository import ICoreRepository


T = TypeVar("T", bound=PostgresBaseModel)


class CoreRepository(Generic[T], ICoreRepository[T]):
    def __init__(self, db: AsyncSession, model: type[T]) -> None:
        self._db = db
        self._model = model

    @staticmethod
    def _set_custom_options(
        query: Query | Select,
        custom_options: list[ExecutableOption] | None = None,
    ) -> Query | Select:
        if custom_options is not None:
            for custom_option in custom_options:
                query = query.options(custom_option)
        return query

    @staticmethod
    def _set_filter_expression(
        query: Query | Select,
        filter_expression: BinaryExpression | None = None,
    ) -> Query | Select:
        if filter_expression is not None:
            query = query.where(filter_expression)
        return query

    @staticmethod
    def _set_filter_params(
        query: Query | Select, filter_params: CoreFilter | None = None
    ) -> Query | Select:
        if filter_params is not None:
            query = filter_params.filter(query)
            query = filter_params.sort(query)
        return query

    async def get_by_sid(
        self, sid: UUID, custom_options: list[ExecutableOption] | None = None
    ) -> T | None:
        query = select(self._model).where(self._model.sid == sid)
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        result: Result = await self._db.execute(query)
        return result.scalars().first()

    async def get_by_label(
        self, label: UUID, custom_options: list[ExecutableOption] | None = None
    ) -> T | None:
        query = select(self._model).where(self._model.label == label)
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        result: Result = await self._db.execute(query)
        return result.scalars().first()

    async def get_by(
        self,
        filter_expression: BinaryExpression | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> T | None:
        query = select(self._model)
        query = self._set_filter_expression(
            query=query, filter_expression=filter_expression
        )
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        result: Result = await self._db.execute(query)
        return result.scalars().first()

    async def get_all(
        self,
        filter_params: CoreFilter | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        query = select(self._model)
        query = self._set_filter_params(
            query=query, filter_params=filter_params
        )
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        result: Result = await self._db.execute(query)
        return list(result.scalars().all())

    async def get_all_by(
        self,
        filter_params: CoreFilter | None = None,
        filter_expression: BinaryExpression | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        query = select(self._model)
        query = self._set_filter_expression(
            query=query, filter_expression=filter_expression
        )
        query = self._set_filter_params(
            query=query, filter_params=filter_params
        )
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        result: Result = await self._db.execute(query)
        return list(result.scalars().all())

    async def get_few(
        self,
        limit: int,
        offset: int,
        filter_params: CoreFilter | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        query = select(self._model).limit(limit).offset(offset)
        query = self._set_filter_params(
            query=query, filter_params=filter_params
        )
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        result: Result = await self._db.execute(query)
        return list(result.scalars().all())

    async def get_few_by(
        self,
        limit: int,
        offset: int,
        filter_params: CoreFilter | None = None,
        filter_expression: BinaryExpression | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        query = select(self._model).limit(limit).offset(offset)
        query = self._set_filter_expression(
            query=query, filter_expression=filter_expression
        )
        query = self._set_filter_params(
            query=query, filter_params=filter_params
        )
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        result: Result = await self._db.execute(query)
        return list(result.scalars().all())

    async def get_pagination(
        self,
        filter_params: CoreFilter | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> LimitOffsetPage[T]:
        query = select(self._model)
        query = self._set_filter_params(
            query=query, filter_params=filter_params
        )
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        return await paginate(self._db, query)

    async def get_pagination_by(
        self,
        filter_params: CoreFilter | None = None,
        filter_expression: BinaryExpression | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> LimitOffsetPage[T]:
        query = select(self._model)
        query = self._set_filter_expression(
            query=query, filter_expression=filter_expression
        )
        query = self._set_filter_params(
            query=query, filter_params=filter_params
        )
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        return await paginate(self._db, query)

    async def create(
        self, obj_in: dict | BaseModel, with_commit: bool = True
    ) -> T:
        if isinstance(obj_in, BaseModel):
            obj_in = obj_in.model_dump()

        obj = self._model(**obj_in)

        self._db.add(obj)
        if with_commit:
            await self._db.commit()
            await self._db.refresh(obj)
        else:
            await self._db.flush()

        return obj

    async def update(
        self, obj: T, obj_in: dict | BaseModel, with_commit: bool = True
    ) -> T:
        if isinstance(obj_in, BaseModel):
            obj_in = obj_in.model_dump()

        for field in obj.__dict__.keys():
            if field in obj_in.keys():
                setattr(obj, field, obj_in[field])

        if with_commit:
            await self._db.commit()
            await self._db.refresh(obj)
        else:
            await self._db.flush()

        return obj

    async def remove(self, obj: T, with_commit: bool = True) -> None:
        await self._db.delete(obj)
        if with_commit:
            await self._db.commit()
        else:
            await self._db.flush()
