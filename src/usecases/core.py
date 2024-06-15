from sqlalchemy.ext.asyncio import AsyncSession

from services import Service


class CoreUseCase:
    def __init__(self, pg_db: AsyncSession) -> None:
        self.service = Service(pg_db)