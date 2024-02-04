from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class EventBase(BaseModel):
    name: Optional[str]
    description: Optional[str]
    address: Optional[str]
    datetime_start: Optional[datetime]
    datetime_end: Optional[datetime]


class Event(EventBase):
    pass
