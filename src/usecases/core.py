from sqlalchemy.ext.asyncio import AsyncSession

from services import Service


class CoreUseCase:
    def __init__(self, pg_db: AsyncSession) -> None:
        self.pg_db = pg_db
        self.service = Service(pg_db)


class CoreUseCaseUtils:
    def __init__(self, pg_db: AsyncSession) -> None:
        self.pg_db = pg_db
