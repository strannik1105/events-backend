from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.repository import IRepository
from interfaces.services import ICoreService, ICoreServiceUtils
from interfaces.services.core import ICrudService
from repository.postgres import PostgresRepository


class CoreService(ICoreService):
    def __init__(self, pg_db: AsyncSession) -> None:
        self._pg_db = pg_db
        self._repository: IRepository = PostgresRepository(pg_db)


class CoreServiceUtils(ICoreServiceUtils):
    def __init__(self, pg_db: AsyncSession) -> None:
        self._pg_db = pg_db

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
                    await self._pg_db.rollback()
                raise not_found_exception
        else:
            if obj:
                if is_rollback:
                    await self._pg_db.rollback()
                raise exists_exception

class CRUDService(ICrudService):
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session

    def get_all(self):
        

    def get_sid():
        pass

    def create(obj_instance: PostgresBaseModel):
        pass

    def update(obj_instance: PostgresBaseModel):
        pass

    def delete(obj_instance: PostgresBaseModel):
        pass