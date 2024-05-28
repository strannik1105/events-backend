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
