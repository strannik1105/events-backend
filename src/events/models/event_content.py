from uuid import uuid4

from sqlalchemy import String, UUID, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from common.db.base import SQLAlchemyBaseModel
from events.models.event_content_type import EventContentTypeModel


class EventContentModel(SQLAlchemyBaseModel):
    __tablename__ = 'event_content'
    __table_args__ = {
        "schema": "event_content",
        "extend_existing": True,
    }

    sid: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    event_content_type_sid = mapped_column(ForeignKey(EventContentTypeModel.sid))
    
    event_type = relationship(
        EventContentTypeModel, foreign_keys=[event_content_type_sid], lazy='joined'
    )