from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.services.events import IEventServiceUtils
from services.core import CoreServiceUtils


class EventServiceUtils(IEventServiceUtils, CoreServiceUtils):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
