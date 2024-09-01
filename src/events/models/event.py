from uuid import uuid4

from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from common.db.base import SQLAlchemyBaseModel


class EventModel(SQLAlchemyBaseModel):
    __tablename__ = "event"
    __table_args__ = {
        "schema": "events",
        "extend_existing": True,
    }

    sid: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
