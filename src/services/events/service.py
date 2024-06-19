from uuid import UUID

from botocore.client import BaseClient
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from common import schemas as common_schemas
from common.managers import S3Manager
from config.exceptions import APIException
from config.settings import settings
from models import events as event_models
from schemas import events as event_schemas
from services.core import CoreService

from .utils import EventServiceUtils


class EventService(CoreService):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
        self._utils = EventServiceUtils(pg_db)
        self._events_bucket: str = settings.s3.EVENTS_BUCKET

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

    async def get_event_file_by_sid(
        self,
        sid: UUID,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventFile | None:
        event_file = await self._pg_repository.event_file.get_by_sid(
            sid=sid, custom_options=custom_options
        )
        if validate:
            await self._utils.exists_validate(
                obj=event_file,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.event_file_already_exists,
                not_found_exception=APIException.event_file_not_found,
            )
        return event_file

    async def get_event_pull_by_event_sids(
        self,
        event_sids: common_schemas.EventSids,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventPull | None:
        event_pull = await self._pg_repository.event_pull.get_by_event_sids(
            event_sids=event_sids,
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

    async def get_event_pull_by_event_user_sids(
        self,
        event_user_sids: common_schemas.EventUserSids,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventPull | None:
        event_pull = (
            await self._pg_repository.event_pull.get_by_event_user_sids(
                event_user_sids=event_user_sids,
                custom_options=custom_options,
            )
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
        event_pull_sids: common_schemas.EventPullSids,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventPull | None:
        event_pull = await self._pg_repository.event_pull.get_by_sids(
            event_pull_sids=event_pull_sids,
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

    async def get_event_file_type_by_name(
        self,
        name: str,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventFileType | None:
        event_file_type = (
            await self._pg_repository.event_file_type.get_by_name(
                name=name, custom_options=custom_options
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

    async def get_event_file_types(self) -> list[event_models.EventFileType]:
        return await self._pg_repository.event_file_type.get_all()

    async def get_event_files_by_event_sids(
        self,
        event_sids: common_schemas.EventSids,
    ) -> list[event_models.EventFileType]:
        return await self._pg_repository.event_file.get_all_by_event_sids(
            event_sids=event_sids,
        )

    async def export_event_file(
        self,
        s3_client: BaseClient,
        event_file: event_models.EventFile,
    ) -> str:
        return S3Manager.generate_url(
            s3_client=s3_client,
            bucket=self._events_bucket,
            obj=event_file.file_name,
            folder=str(event_file.event_sid)
            if event_file.event_content_sid is None
            else f"{event_file.event_sid}/{event_file.event_content_sid}",
        )

    async def upload_event_file(
        self,
        s3_client: BaseClient,
        event_file: event_models.EventFile,
        file: UploadFile,
    ) -> None:
        S3Manager.put_obj(
            s3_client=s3_client,
            bucket=self._events_bucket,
            file_io=file.file,
            obj=event_file.file_name,
            folder=str(event_file.event_sid)
            if event_file.event_content_sid is None
            else f"{event_file.event_sid}/{event_file.event_content_sid}",
            content_type=file.content_type,
        )

    async def unload_event_file(
        self,
        s3_client: BaseClient,
        event_file: event_models.EventFile,
    ) -> None:
        S3Manager.remove(
            s3_client=s3_client,
            bucket=self._events_bucket,
            obj=event_file.file_name,
            folder=str(event_file.event_sid)
            if event_file.event_content_sid is None
            else f"{event_file.event_sid}/{event_file.event_content_sid}",
        )

    async def create_event_file(
        self,
        event_file_in: event_schemas.EventFileCreate,
        with_commit: bool = True,
    ) -> event_models.EventFile:
        return await self._pg_repository.event_file.create(
            obj_in=event_file_in,
            with_commit=with_commit,
        )

    async def remove_event_file(
        self,
        event_file: event_models.EventFile,
        with_commit: bool = True,
    ) -> None:
        return await self._pg_repository.event_file.remove(
            obj=event_file,
            with_commit=with_commit,
        )

    async def create_event_file_type(
        self,
        event_file_type_in: event_schemas.EventFileTypeCreate,
        with_commit: bool = True,
    ) -> event_models.EventFileType:
        return await self._pg_repository.event_file_type.create(
            obj_in=event_file_type_in,
            with_commit=with_commit,
        )
