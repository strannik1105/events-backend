from typing import Generic, List, TypeVar
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from common.base.singleton import Singleton


T = TypeVar("T")


class IRepository(Generic[T], metaclass=Singleton):
    def get(self, session: AsyncSession, sid: UUID) -> T:
        raise NotImplementedError

    def get_all(
        self, session: AsyncSession, limit: int, offset: int
    ) -> List[T]:
        raise NotImplementedError

    def create(self, session: AsyncSession, obj: T) -> T:
        raise NotImplementedError

    def update(self, session: AsyncSession, db_obj: T, new_obj):
        raise NotImplementedError
