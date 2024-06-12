from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession


class IRepository[T]:
    def get(self, session: AsyncSession, sid: UUID) -> T:
        raise NotImplementedError

    def get_all(
        self, session: AsyncSession, limit: int, offset: int
    ) -> list[T]:
        raise NotImplementedError

    def create(self, session: AsyncSession, obj: T) -> T:
        raise NotImplementedError

    def update(self, session: AsyncSession, db_obj: T, new_obj) -> T:
        raise NotImplementedError
