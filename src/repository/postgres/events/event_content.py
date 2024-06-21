from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from interfaces.repository.events import IEventContentRepository
from models.events import EventContent
from repository.postgres.core import CoreRepository


class EventContentRepository(
    IEventContentRepository[EventContent], CoreRepository[EventContent]
):
    def __init__(self, db: AsyncSession, model: type[EventContent]) -> None:
        super().__init__(db, model)

    async def get_all_by_event_sid(
        self,
        event_sid: UUID,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[EventContent]:
        return await self.get_all_by(
            filter_expression=self._model.event_sid == event_sid,
            custom_options=custom_options,
        )
