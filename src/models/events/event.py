from sqlalchemy import String, DateTime
from sqlalchemy.orm import mapped_column
from common.db.base_model import BaseModel
from models.events.ext import EVENTS_SCHEMA


class Event(BaseModel):
    __tablename__ = "event"
    __table_args__ = {"schema": EVENTS_SCHEMA}
    name = mapped_column(String, nullable=False)
    description = mapped_column(String, nullable=False)
    address = mapped_column(String, nullable=False)
    datetime_start = mapped_column(DateTime, nullable=False)
    datetime_end = mapped_column(DateTime, nullable=False)
