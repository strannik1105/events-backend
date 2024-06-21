from abc import ABCMeta, abstractmethod
from uuid import UUID

from botocore.client import BaseClient
from fastapi import UploadFile

from common import schemas
from interfaces.usecases.core import ICoreUseCase
from models import events as event_models
from schemas import users as user_schemas


class IEventUseCase(ICoreUseCase, metaclass=ABCMeta):
    @abstractmethod
    async def get_event_files(
        self,
        current_user: user_schemas.CurrentUser,
        event_sids: schemas.EventSids,
    ) -> list[event_models.EventFile]:
        raise NotImplementedError

    @abstractmethod
    async def get_event_types(self) -> list[event_models.EventType]:
        raise NotImplementedError

    @abstractmethod
    async def get_event_content_types(
        self,
    ) -> list[event_models.EventContentType]:
        raise NotImplementedError

    @abstractmethod
    async def get_event_file_types(self) -> list[event_models.EventFileType]:
        raise NotImplementedError

    @abstractmethod
    async def export_event_file_by_sid(
        self,
        current_user: user_schemas.CurrentUser,
        s3_client: BaseClient,
        event_file_sid: UUID,
    ) -> str:
        raise NotImplementedError

    @abstractmethod
    async def create_event_file(
        self,
        current_user: user_schemas.CurrentUser,
        s3_client: BaseClient,
        event_sids: schemas.EventSids,
        file: UploadFile,
    ) -> event_models.EventFile:
        raise NotImplementedError

    @abstractmethod
    async def remove_event_file_by_sid(
        self,
        current_user: user_schemas.CurrentUser,
        s3_client: BaseClient,
        event_file_sid: UUID,
    ) -> schemas.Msg:
        raise NotImplementedError
