from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import BinaryExpression, Result, Select, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from common.db.postgres import PostgresBaseModel
from repository.interface import IRepository


T = TypeVar("T", bound=PostgresBaseModel)


class CoreRepository(Generic[T], IRepository[T]):
    def __init__(self, db: AsyncSession, model: type[T]) -> None:
        self._db = db
        self._model = model

    @staticmethod
    def _set_custom_options(
        query: Select, custom_options: list[ExecutableOption] | None = None
    ) -> Select:
        if custom_options is not None:
            for custom_option in custom_options:
                query = query.options(custom_option)
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
        if filter_expression is not None:
            query = query.where(filter_expression)
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        result: Result = await self._db.execute(query)
        return result.scalars().first()

    async def get_all(
        self, custom_options: list[ExecutableOption] | None = None
    ) -> list[T]:
        query = select(self._model)
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        result: Result = await self._db.execute(query)
        return list(result.scalars().all())

    async def get_few(
        self,
        limit: int,
        offset: int,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[T]:
        query = select(self._model).limit(limit).offset(offset)
        query = self._set_custom_options(
            query=query, custom_options=custom_options
        )
        result: Result = await self._db.execute(query)
        return list(result.scalars().all())

    async def create(
        self, obj_in: T | BaseModel, with_commit: bool = True
    ) -> T:
        if isinstance(obj_in, BaseModel):
            obj = self._model(**obj_in.model_dump())
        else:
            obj = obj_in

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
            changes = obj_in.model_dump()
        else:
            changes = obj_in

        for change in changes.keys():
            if getattr(obj, change):
                setattr(obj, change, changes[change])

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
