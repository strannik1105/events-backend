from typing import Optional
from uuid import UUID

from common.schemas.schemas import BaseSchema


class EventContentTypeBaseSchema(BaseSchema):
    sid: Optional[UUID]
    name: Optional[str]
    description: Optional[str]


class EventContentTypeCreateSchema(BaseSchema):
    name: str
    description: str