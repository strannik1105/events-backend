from abc import ABCMeta, abstractmethod
from uuid import UUID

from botocore.client import BaseClient
from fastapi import UploadFile
from fastapi_pagination import LimitOffsetPage
from sqlalchemy.sql.base import ExecutableOption

from common import schemas as common_schemas
from interfaces.services.core import ICoreService
from models import events as event_models
from schemas import events as event_schemas


class IEventService(ICoreService, metaclass=ABCMeta):
    @abstractmethod
    async def get_event_by_sid(
        self,
        sid: UUID,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.Event | None:
        raise NotImplementedError

    @abstractmethod
    async def get_event_type_by_label(
        self,
        label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventType | None:
        raise NotImplementedError

    @abstractmethod
    async def get_event_content_by_sid(
        self,
        sid: UUID,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventContent | None:
        raise NotImplementedError

    @abstractmethod
    async def get_event_content_type_by_label(
        self,
        label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventContentType | None:
        raise NotImplementedError

    @abstractmethod
    async def get_event_file_by_sid(
        self,
        sid: UUID,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventFile | None:
        raise NotImplementedError

    @abstractmethod
    async def get_event_pull_by_event_sids(
        self,
        event_sids: common_schemas.EventSids,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventPull | None:
        raise NotImplementedError

    @abstractmethod
    async def get_event_pull_by_event_user_sids(
        self,
        event_user_sids: common_schemas.EventUserSids,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventPull | None:
        raise NotImplementedError

    @abstractmethod
    async def get_event_pull_by_sids(
        self,
        event_pull_sids: common_schemas.EventPullSids,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventPull | None:
        raise NotImplementedError

    @abstractmethod
    async def get_event_file_type_by_label(
        self,
        label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventFileType | None:
        raise NotImplementedError

    @abstractmethod
    async def get_event_file_type_by_name(
        self,
        name: str,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> event_models.EventFileType | None:
        raise NotImplementedError

    @abstractmethod
    async def get_events(
        self,
        custom_options: list[ExecutableOption] | None = None,
    ) -> LimitOffsetPage[event_models.Event]:
        raise NotImplementedError

    @abstractmethod
    async def get_event_types(
        self,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[event_models.EventType]:
        raise NotImplementedError

    @abstractmethod
    async def get_event_contents_by_event_sid(
        self,
        event_sid: UUID,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[event_models.EventContent]:
        raise NotImplementedError

    @abstractmethod
    async def get_event_content_types(
        self,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[event_models.EventContentType]:
        raise NotImplementedError

    @abstractmethod
    async def get_event_file_types(self) -> list[event_models.EventFileType]:
        raise NotImplementedError

    @abstractmethod
    async def get_event_files_by_event_sids(
        self,
        event_sids: common_schemas.EventSids,
    ) -> list[event_models.EventFile]:
        raise NotImplementedError

    @abstractmethod
    async def export_event_file(
        self,
        s3_client: BaseClient,
        event_file: event_models.EventFile,
    ) -> str:
        raise NotImplementedError

    @abstractmethod
    async def upload_event_file(
        self,
        s3_client: BaseClient,
        event_file: event_models.EventFile,
        file: UploadFile,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def unload_event_file(
        self,
        s3_client: BaseClient,
        event_file: event_models.EventFile,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def create_event(
        self,
        event_in: event_schemas.EventDTOCreate,
        with_commit: bool = True,
    ) -> event_models.Event:
        raise NotImplementedError

    @abstractmethod
    async def create_event_type(
        self,
        event_type_in: event_schemas.EventTypeDTOCreate,
        with_commit: bool = True,
    ) -> event_models.EventType:
        raise NotImplementedError

    @abstractmethod
    async def create_event_content(
        self,
        event_content_in: event_schemas.EventContentDTOCreate,
        with_commit: bool = True,
    ) -> event_models.EventContent:
        raise NotImplementedError

    @abstractmethod
    async def create_event_content_type(
        self,
        event_content_type_in: event_schemas.EventContentTypeDTOCreate,
        with_commit: bool = True,
    ) -> event_models.EventContentType:
        raise NotImplementedError

    @abstractmethod
    async def create_event_pull(
        self,
        event_pull_in: event_schemas.EventPullDTOCreate,
        with_commit: bool = True,
    ) -> event_models.EventPull:
        raise NotImplementedError

    @abstractmethod
    async def create_event_file(
        self,
        event_file_in: event_schemas.EventFileDTOCreate,
        with_commit: bool = True,
    ) -> event_models.EventFile:
        raise NotImplementedError

    @abstractmethod
    async def remove_event_file(
        self,
        event_file: event_models.EventFile,
        with_commit: bool = True,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def create_event_file_type(
        self,
        event_file_type_in: event_schemas.EventFileTypeDTOCreate,
        with_commit: bool = True,
    ) -> event_models.EventFileType:
        raise NotImplementedError
