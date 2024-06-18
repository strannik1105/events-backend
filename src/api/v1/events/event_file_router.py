from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile

from api import deps
from api.params import APIParam
from common import schemas
from models import events as event_models
from schemas import events as event_schemas

from .paths import APIPath


router = APIRouter()


@router.get(
    path=APIPath.GET_EVENT_FILE_BY_SID,
    response_model=str,
)
async def get_event_file_by_sid(
    _: deps.CurrentActiveUser,
    s3_client: deps.S3Client,
    use_case: deps.UseCase,
    event_file_sid: Annotated[UUID, APIParam.query(..., alias="eventFileSid")],
) -> str:
    return await use_case.event.get_event_file_by_sid(
        s3_client=s3_client,
        event_file_sid=event_file_sid,
    )


@router.get(
    path=APIPath.GET_EVENT_FILES,
    response_model=list[event_schemas.EventFile],
)
async def get_event_files(
    _: deps.CurrentActiveUser,
    use_case: deps.UseCase,
    event_sids: Annotated[schemas.EventSids, Depends()],
) -> list[event_models.EventFile]:
    return await use_case.event.get_event_files(
        event_sids=event_sids,
    )


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
    event_sids: Annotated[schemas.EventSids, Depends()],
    file: Annotated[UploadFile, APIParam.file(...)],
) -> event_models.EventFile:
    return await use_case.event.create_event_file(
        s3_client=s3_client,
        event_sids=event_sids,
        file=file,
    )


@router.delete(
    path=APIPath.REMOVE_EVENT_FILE_BY_SID,
    response_model=schemas.Msg,
)
async def remove_event_file_by_sid(
    _: deps.CurrentActiveUser,
    s3_client: deps.S3Client,
    use_case: deps.UseCase,
    event_file_sid: Annotated[UUID, APIParam.query(..., alias="eventFileSid")],
) -> schemas.Msg:
    return await use_case.event.remove_event_file_by_sid(
        s3_client=s3_client,
        event_file_sid=event_file_sid,
    )
