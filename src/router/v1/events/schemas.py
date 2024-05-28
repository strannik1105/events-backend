from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class EventBaseSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    address: Optional[str]
    datetime_start: Optional[datetime]
    datetime_end: Optional[datetime]


class EventSchema(EventBaseSchema):
    sid: UUID


class EventContentBaseSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    address: Optional[str]
    event_sid: UUID


class EventContentSchema(EventContentBaseSchema):
    sid: UUID


class EventContentCreateSchema(EventContentBaseSchema):
    name: str


class EventContentUpdateSchema(EventContentBaseSchema):
    event_sid: Optional[UUID]


class EventPullSchema(BaseModel):
    event_sid: UUID
    event_content_sid: UUID

    user_sid: UUID
