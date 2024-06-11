from uuid import UUID

from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin


class EventFileBase(CoreModel):
    file_name: str = Field(..., description="Event file name")
    file_bytes: int = Field(..., description="Event file bytes")
    event_sid: UUID = Field(..., description="Event SID")
    event_content_sid: UUID = Field(..., description="Event content SID")
    type_sid: UUID = Field(..., description="Event file type SID")

    @field_validator("file_name", mode="after")
    def validate_file_name(cls, v: str) -> str:
        return v.strip()


class EventFile(EventFileBase, DateTimeMixin):
    sid: UUID = Field(..., description="Event file SID")
