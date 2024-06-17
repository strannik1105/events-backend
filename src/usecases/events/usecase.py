from uuid import UUID, uuid4

from botocore.client import BaseClient
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from models import events as event_models
from schemas import events as event_schemas
from usecases.core import CoreUseCase

from .utils import EventUseCaseUtils


class EventUseCase(CoreUseCase):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
        self._utils = EventUseCaseUtils(pg_db)

    async def get_event_file_types(self) -> list[event_models.EventFileType]:
        return await self._service.event.get_event_file_types()

    async def create_event_file(
        self,
        s3_client: BaseClient,
        event_sid: UUID,
        event_content_sid: UUID | None,
        file: UploadFile,
    ) -> event_models.EventFile:
        self._utils.validate_file_size(file=file)
        file_extension = self._utils.get_file_extension(file=file)
        event_file_type = (
            await self._service.event.get_event_file_type_by_name(
                name=file_extension,
            )
        )

        await self._service.event.get_event_by_sid(sid=event_sid)
        if event_content_sid is not None:
            await self._service.event.get_event_content_by_sid(
                sid=event_content_sid
            )
            await self._service.event.get_event_pull_by_event_sids(
                event_sid=event_sid,
                event_content_sid=event_content_sid,
            )

        event_file = await self._service.event.create_event_file(
            event_file_in=event_schemas.EventFileCreate(
                sid=uuid4(),
                file_name=file.filename,
                file_bytes=file.size,
                event_sid=event_sid,
                event_content_sid=event_content_sid,
                type_label=event_file_type.label,
            ),
            with_commit=False,
        )
        await self._service.event.upload_event_file(
            s3_client=s3_client,
            event_file=event_file,
            file=file,
        )

        await self._pg_db.commit()
        await self._pg_db.refresh(event_file)

        return event_file
