from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from common import schemas as common_schemas
from models.events import EventFile
from interfaces.repository.events import IEventFileRepository
from repository.postgres.core import CoreRepository


class EventFileRepository(
    IEventFileRepository[EventFile], CoreRepository[EventFile]
):
    def __init__(self, db: AsyncSession, model: type[EventFile]) -> None:
        super().__init__(db, model)

    async def get_all_by_event_sids(
        self,
        event_sids: common_schemas.EventSids,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[EventFile]:
        return await self.get_all_by(
            filter_expression=(
                (self._model.event_sid == event_sids.event_sid)
                & (
                    self._model.event_content_sid
                    == event_sids.event_content_sid
                )
            ),
            custom_options=custom_options,
        )
