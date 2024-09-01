from typing import Type, TypeVar
from uuid import UUID

from sqlalchemy import select, update, delete

from common.db.session import PostgresSession
from common.repository.abstract_crud_repository import AbstractCrudRepository

T = TypeVar("T")


class CrudRepository(AbstractCrudRepository[T]):
    def __init__(self, session: PostgresSession, model: Type[T]) -> None:
        self._session = session
        self._model = model

    async def get_all(self, limit: int = 100, offset: int = 0) -> list[T]:
        objs = await self._session.get_async().execute(
            select(self._model).limit(limit).offset(offset)
        )
        return list(objs.scalars().all())

    async def get(self, sid: UUID) -> T:
        obj = await self._session.get_async().execute(
            select(self._model).where(self._model.c.sid == sid)
        )
        return obj.scalar_one_or_none()
    
    async def create(self, obj):
        self._session.get_async().add(obj)
        await self._session.get_async().commit()
        await self._session.get_async().refresh(obj)
        return obj

    async def update(self, changes, sid):
        obj = await self._session.get_async().execute(
            update(self._model).where(self._model.c.sid == sid).values(changes)
        )
        return obj

    async def delete(self, obj):
        await self._session.get_async().delete(obj)
        await self._session.get_async().commit()