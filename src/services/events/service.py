from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from config.exceptions import APIException
from models import events as event_models
from schemas import events as event_schemas
from services.core import CoreService

from .utils import EventServiceUtils


class EventService(CoreService):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
        self._utils = EventServiceUtils(pg_db)

    async def get_event_file_type_by_label(
        self,
        label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventFileType | None:
        event_file_type = (
            await self.pg_repository.event_file_type.get_by_label(
                label=label, custom_options=custom_options
            )
        )
        if validate:
            await self._utils.exists_validate(
                obj=event_file_type,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.event_file_type_already_exists,
                not_found_exception=APIException.event_file_type_not_found,
            )
        return event_file_type

    async def create_event_file_type(
        self,
        event_file_type_in: event_schemas.EventFileTypeCreate,
        with_commit: bool = True,
    ) -> event_models.EventFileType:
        return await self.pg_repository.event_file_type.create(
            obj_in=event_file_type_in,
            with_commit=with_commit,
        )
