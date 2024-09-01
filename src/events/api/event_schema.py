from typing import Optional
from uuid import UUID

from common.schemas.schemas import BaseSchema


class EventBaseSchema(BaseSchema):
    name: Optional[str]

class EventSchema(BaseSchema):
    sid: Optional[UUID]
    name: str

class EventCreateSchema(BaseSchema):
    name: str

class EventUpdateSchema(BaseSchema):
    name: Optional[str]
