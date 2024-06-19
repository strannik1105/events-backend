from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from models.events import EventFileType
from repository.postgres.core import CoreRepository


class EventFileTypeRepository(CoreRepository[EventFileType]):
    def __init__(self, db: AsyncSession, model: type[EventFileType]) -> None:
        super().__init__(db, model)

    async def get_by_name(
        self, name: str, custom_options: list[ExecutableOption] | None = None
    ) -> EventFileType | None:
        return await self.get_by(
            filter_expression=self._model.name == name,
            custom_options=custom_options,
        )
