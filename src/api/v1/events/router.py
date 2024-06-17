from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, UploadFile

from api import deps
from api.params import APIParam
from models import events as event_models
from schemas import events as event_schemas

from .paths import APIPath


router = APIRouter()


@router.get(
    path=APIPath.GET_EVENT_FILE_TYPES,
    response_model=list[event_schemas.EventFileType],
)
async def get_event_file_types(
    _: deps.CurrentActiveUser,
    use_case: deps.UseCase,
) -> list[event_models.EventFileType]:
    return await use_case.event.get_event_file_types()


@router.post(
    path=APIPath.CREATE_EVENT_FILE, response_model=event_schemas.EventFile
)
async def create_event_file(
    _: deps.CurrentActiveUser,
    s3_client: deps.S3Client,
    use_case: deps.UseCase,
    event_sid: Annotated[UUID, APIParam.query(..., alias="eventSid")],
    file: Annotated[UploadFile, APIParam.file(...)],
    event_content_sid: UUID
    | None = APIParam.query(None, alias="eventContentSid"),
) -> event_models.EventFile:
    return await use_case.event.create_event_file(
        s3_client=s3_client,
        event_sid=event_sid,
        event_content_sid=event_content_sid,
        file=file,
    )
