from uuid import UUID

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

    async def get_event_by_sid(
        self,
        sid: UUID,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.Event | None:
        event = await self._pg_repository.event.get_by_sid(
            sid=sid, custom_options=custom_options
        )
        if validate:
            await self._utils.exists_validate(
                obj=event,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.event_already_exists,
                not_found_exception=APIException.event_not_found,
            )
        return event

    async def get_event_content_by_sid(
        self,
        sid: UUID,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventContent | None:
        event_content = await self._pg_repository.event_content.get_by_sid(
            sid=sid, custom_options=custom_options
        )
        if validate:
            await self._utils.exists_validate(
                obj=event_content,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.event_content_already_exists,
                not_found_exception=APIException.event_content_not_found,
            )
        return event_content

    async def get_event_pull_by_event_sids(
        self,
        event_sid: UUID,
        event_content_sid: UUID | None,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventContent | None:
        event_pull = await self._pg_repository.event_pull.get_by_event_sids(
            event_sid=event_sid,
            event_content_sid=event_content_sid,
            custom_options=custom_options,
        )
        if validate:
            await self._utils.exists_validate(
                obj=event_pull,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.event_pull_already_exists,
                not_found_exception=APIException.event_pull_not_found,
            )
        return event_pull

    async def get_event_pull_by_sids(
        self,
        event_sid: UUID,
        event_content_sid: UUID | None,
        user_sid: UUID,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventContent | None:
        event_pull = await self._pg_repository.event_pull.get_by_sids(
            event_sid=event_sid,
            event_content_sid=event_content_sid,
            user_sid=user_sid,
            custom_options=custom_options,
        )
        if validate:
            await self._utils.exists_validate(
                obj=event_pull,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.event_pull_already_exists,
                not_found_exception=APIException.event_pull_not_found,
            )
        return event_pull

    async def get_event_file_type_by_label(
        self,
        label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventFileType | None:
        event_file_type = (
            await self._pg_repository.event_file_type.get_by_label(
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
        return await self._pg_repository.event_file_type.create(
            obj_in=event_file_type_in,
            with_commit=with_commit,
        )
