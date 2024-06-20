from uuid import UUID

from botocore.client import BaseClient
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from common import enums
from common import schemas
from common import schemas as common_schemas
from common.security import SecurityRole
from enums import security as security_enums
from models import events as event_models
from schemas import events as event_schemas
from schemas import users as user_schemas
from usecases.core import CoreUseCase

from .utils import EventUseCaseUtils


class EventUseCase(CoreUseCase):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
        self._utils = EventUseCaseUtils(pg_db)

    async def get_event_files(
        self,
        current_user: user_schemas.CurrentUser,
        event_sids: schemas.EventSids,
    ) -> list[event_models.EventFile]:
        resource_label = security_enums.ResourceLabel.EVENT_FILE
        if event_sids.event_content_sid is not None:
            resource_label = security_enums.ResourceLabel.EVENT_SPEAKER_FILE

        await SecurityRole.validate_event_role_permission(
            repository=self.service.repository,
            resource_label=resource_label,
            permission_label=security_enums.PermissionLabel.READ,
            current_user=current_user,
            event_sids=event_sids,
        )

        await self.service.event.get_event_by_sid(sid=event_sids.event_sid)
        if event_sids.event_content_sid is not None:
            await self.service.event.get_event_content_by_sid(
                sid=event_sids.event_content_sid
            )
            await self.service.event.get_event_pull_by_event_sids(
                event_sids=event_sids,
            )

        return await self.service.event.get_event_files_by_event_sids(
            event_sids=event_sids,
        )

    async def get_event_types(self) -> list[event_models.EventType]:
        return await self.service.event.get_event_types()

    async def get_event_content_types(
        self,
    ) -> list[event_models.EventContentType]:
        return await self.service.event.get_event_content_types()

    async def get_event_file_types(self) -> list[event_models.EventFileType]:
        return await self.service.event.get_event_file_types()

    async def export_event_file_by_sid(
        self,
        current_user: user_schemas.CurrentUser,
        s3_client: BaseClient,
        event_file_sid: UUID,
    ) -> str:
        event_file = await self.service.event.get_event_file_by_sid(
            sid=event_file_sid
        )

        resource_label = security_enums.ResourceLabel.EVENT_FILE
        if event_file.event_content_sid is not None:
            resource_label = security_enums.ResourceLabel.EVENT_SPEAKER_FILE

        await SecurityRole.validate_event_role_permission(
            repository=self.service.repository,
            resource_label=resource_label,
            permission_label=security_enums.PermissionLabel.EXPORT,
            current_user=current_user,
            event_sids=common_schemas.EventSids(
                event_sid=event_file.event_sid,
                event_content_sid=event_file.event_content_sid,
            ),
        )

        return await self.service.event.export_event_file(
            s3_client=s3_client,
            event_file=event_file,
        )

    async def create_event_file(
        self,
        current_user: user_schemas.CurrentUser,
        s3_client: BaseClient,
        event_sids: schemas.EventSids,
        file: UploadFile,
    ) -> event_models.EventFile:
        resource_label = security_enums.ResourceLabel.EVENT_FILE
        if event_sids.event_content_sid is not None:
            resource_label = security_enums.ResourceLabel.EVENT_SPEAKER_FILE

        await SecurityRole.validate_event_role_permission(
            repository=self.service.repository,
            resource_label=resource_label,
            permission_label=security_enums.PermissionLabel.CREATE,
            current_user=current_user,
            event_sids=event_sids,
        )

        self._utils.validate_file_size(file=file)
        file_extension = self._utils.get_file_extension(file=file)
        event_file_type = await self.service.event.get_event_file_type_by_name(
            name=file_extension,
        )

        await self.service.event.get_event_by_sid(sid=event_sids.event_sid)
        if event_sids.event_content_sid is not None:
            await self.service.event.get_event_content_by_sid(
                sid=event_sids.event_content_sid
            )
            await self.service.event.get_event_pull_by_event_sids(
                event_sids=event_sids,
            )

        event_file = await self.service.event.create_event_file(
            event_file_in=event_schemas.EventFileCreate(
                file_name=file.filename,
                file_bytes=file.size,
                event_sid=event_sids.event_sid,
                event_content_sid=event_sids.event_content_sid,
                type_label=event_file_type.label,
            ),
            with_commit=False,
        )
        await self.service.event.upload_event_file(
            s3_client=s3_client,
            event_file=event_file,
            file=file,
        )

        await self.pg_db.commit()
        await self.pg_db.refresh(event_file)

        return event_file

    async def remove_event_file_by_sid(
        self,
        current_user: user_schemas.CurrentUser,
        s3_client: BaseClient,
        event_file_sid: UUID,
    ) -> schemas.Msg:
        event_file = await self.service.event.get_event_file_by_sid(
            sid=event_file_sid
        )

        resource_label = security_enums.ResourceLabel.EVENT_FILE
        if event_file.event_content_sid is not None:
            resource_label = security_enums.ResourceLabel.EVENT_SPEAKER_FILE

        await SecurityRole.validate_event_role_permission(
            repository=self.service.repository,
            resource_label=resource_label,
            permission_label=security_enums.PermissionLabel.DELETE,
            current_user=current_user,
            event_sids=common_schemas.EventSids(
                event_sid=event_file.event_sid,
                event_content_sid=event_file.event_content_sid,
            ),
        )

        await self.service.event.remove_event_file(
            event_file=event_file,
            with_commit=False,
        )
        await self.service.event.unload_event_file(
            s3_client=s3_client,
            event_file=event_file,
        )

        await self.pg_db.commit()

        return schemas.Msg(msg=enums.ResponseMessages.SUCCESS)
