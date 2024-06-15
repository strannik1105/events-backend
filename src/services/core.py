from sqlalchemy.ext.asyncio import AsyncSession

from repository.postgres import PostgresRepository


class CoreService:
    def __init__(self, pg_db: AsyncSession) -> None:
        self.pg_repository = PostgresRepository(pg_db)
