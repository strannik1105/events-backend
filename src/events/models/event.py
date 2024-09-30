from uuid import uuid4

from sqlalchemy import String, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from common.db.base import SQLAlchemyBaseModel
from events.models.event_image import EventImageModel
from events.models.event_type import EventTypeModel


class EventModel(SQLAlchemyBaseModel):
    __tablename__ = "event"
    __table_args__ = {
        "schema": "events",
        "extend_existing": True,
    }

    sid: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    event_type_sid = mapped_column(ForeignKey(EventTypeModel.sid))
    event_image_sid = mapped_column(ForeignKey(EventImageModel.sid))
    
    # event_type = relationship(
    #     EventTypeModel, foreign_keys=[event_type_sid], lazy='joined'
    # )
    # event_image = relationship(
    #     EventImageModel, foreign_keys=[event_image_sid], lazy='joined'
    # )
