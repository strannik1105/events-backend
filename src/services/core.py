from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from repository.interfaces.repository import IRepository
from repository.postgres import PostgresRepository


class CoreService:
    def __init__(self, pg_db: AsyncSession) -> None:
        self.pg_db = pg_db
        self.repository: IRepository = PostgresRepository(pg_db)


class CoreServiceUtils:
    def __init__(self, pg_db: AsyncSession) -> None:
        self.pg_db = pg_db

    async def exists_validate(
        self,
        obj: Any | None,
        is_exists: bool,
        is_rollback: bool,
        exists_exception: Exception,
        not_found_exception: Exception,
    ) -> None:
        if is_exists:
            if not obj:
                if is_rollback:
                    await self.pg_db.rollback()
                raise not_found_exception
        else:
            if obj:
                if is_rollback:
                    await self.pg_db.rollback()
                raise exists_exception
