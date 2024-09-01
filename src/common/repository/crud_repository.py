from typing import Type, TypeVar

from sqlalchemy import select

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

    async def create(self, obj, with_commit=True) -> T:
        self._session.get_async().add(obj)
        if with_commit:
            await self._session.get_async().commit()
        else:
            await self._session.get_async().flush()
        await self._session.get_async().refresh(obj)
        return obj
