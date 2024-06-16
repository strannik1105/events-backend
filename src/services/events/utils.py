from sqlalchemy.ext.asyncio import AsyncSession

from services.core import CoreServiceUtils


class EventServiceUtils(CoreServiceUtils):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
