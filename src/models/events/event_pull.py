from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from common.db.base_model import BaseModel
from models.events.ext import EVENTS_SCHEMA


class EventPull(BaseModel):
    __tablename__ = "event_content"
    __table_args__ = {"schema": EVENTS_SCHEMA}

    event_sid = mapped_column(ForeignKey("events.event.sid"), nullable=False)
    event = relationship("Event")

    event_content_sid = mapped_column(
        ForeignKey("events.event_content.sid"), nullable=False
    )
    event_content = mapped_column(ForeignKey("EventContent"))

    user_sid = mapped_column("users.user.sid", nullable=False)
    user = relationship("User")
