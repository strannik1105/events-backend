from uuid import uuid4

from sqlalchemy import String, UUID
from sqlalchemy.orm import mapped_column, Mapped

from common.db.base import SQLAlchemyBaseModel


class EventContentTypeModel(SQLAlchemyBaseModel):
    __tablename__ = 'event_content_type'
    __table_args__ = {
        "schema": "event_content_type",
        "extend_existing": True,
    }

    sid: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
