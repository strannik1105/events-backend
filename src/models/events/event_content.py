from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column
from common.db.base_model import BaseModel
from models.events.ext import EVENTS_SCHEMA


class EventContent(BaseModel):
    __tablename__ = "event_content"
    __table_args__ = {"schema": EVENTS_SCHEMA}
    name = mapped_column(String, nullable=False)
    description = mapped_column(String)
    address = mapped_column(String)
    # datetime_start = mapped_column(DateTime, nullable=False)
    # datetime_end = mapped_column(DateTime, nullable=False)

    event_sid = mapped_column(ForeignKey("events.event.sid"), nullable=False)
