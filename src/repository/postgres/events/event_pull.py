from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from models.events import EventPull
from repository.postgres.core import CoreRepository


class EventPullRepository(CoreRepository[EventPull]):
    def __init__(self, db: AsyncSession, model: type[EventPull]) -> None:
        super().__init__(db, model)

    async def get_by_event_sids(
        self,
        event_sid: UUID,
        event_content_sid: UUID | None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> EventPull | None:
        return await self.get_by(
            filter_expression=(
                (self._model.event_sid == event_sid)
                & (self._model.event_content_sid == event_content_sid)
            ),
            custom_options=custom_options,
        )

    async def get_by_sids(
        self,
        event_sid: UUID,
        event_content_sid: UUID | None,
        user_sid: UUID,
        custom_options: list[ExecutableOption] | None = None,
    ) -> EventPull | None:
        return await self.get_by(
            filter_expression=(
                (self._model.event_sid == event_sid)
                & (self._model.event_content_sid == event_content_sid)
                & (self._model.user_sid == user_sid)
            ),
            custom_options=custom_options,
        )
