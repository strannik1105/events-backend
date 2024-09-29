from typing import Optional
from uuid import UUID

from common.schemas.schemas import BaseSchema


class EventBaseSchema(BaseSchema):
    name: Optional[str]
    description: str
    event_type_sid: Optional[UUID]
    event_image_sid: Optional[UUID]


class EventSchema(BaseSchema):
    sid: Optional[UUID]
    name: str
    description: str
    event_type_sid: UUID
    event_image_sid: UUID


class EventCreateSchema(BaseSchema):
    name: str
    description: str
    event_type_sid: UUID
    event_image_sid: UUID


class EventUpdateSchema(BaseSchema):
    name: Optional[str]
    description: str
    event_type_sid: Optional[UUID]
    event_image_sid: Optional[UUID]
