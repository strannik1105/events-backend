from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from common.db import PostgresBaseModel, PostgresDBSchemas
from models.mixins import CreatedAtMixin


EVENTS_SCHEMA = PostgresDBSchemas.EVENTS
USERS_SCHEMA = PostgresDBSchemas.USERS
METRICS_SCHEMA = PostgresDBSchemas.METRICS


class EventView(PostgresBaseModel, CreatedAtMixin):
    __tablename__ = "event_view"
    __table_args__ = {
        "schema": METRICS_SCHEMA,
        "comment": "Table with all event views",
    }

    user_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{USERS_SCHEMA}.user.sid", ondelete="CASCADE"),
        index=True,
        comment="User SID",
    )
    event_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{EVENTS_SCHEMA}.event.sid", ondelete="CASCADE"),
        index=True,
        comment="Event SID",
    )
