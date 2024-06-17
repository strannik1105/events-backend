from uuid import UUID

from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin, Sid
from enums import events as event_enums


class EventFileBase(CoreModel):
    file_name: str = Field(..., description="Event file name")
    file_bytes: int = Field(..., description="Event file bytes")
    event_sid: UUID = Field(..., description="Event SID")
    event_content_sid: UUID | None = Field(
        None, description="Event content SID"
    )
    type_label: event_enums.EventFileTypeLabel = Field(
        ..., description="Event file type label"
    )

    @field_validator("file_name", mode="after")
    def validate_file_name(cls, v: str) -> str:
        return v.strip()


class EventFileCreate(EventFileBase, Sid):
    pass


class EventFile(EventFileBase, Sid, DateTimeMixin):
    pass
