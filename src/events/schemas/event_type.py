from typing import Optional
from uuid import UUID

from common.schemas.schemas import BaseSchema


class EventTypeBaseSchema(BaseSchema):
    sid: Optional[UUID]
    name: Optional[str]
    description: Optional[str]


class EventTypeCreateSchema(BaseSchema):
    name: str
    description: str
