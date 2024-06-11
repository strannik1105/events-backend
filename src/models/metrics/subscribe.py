from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from common.db import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin


USERS_SCHEMA = PostgresDBSchemas.USERS
METRICS_SCHEMA = PostgresDBSchemas.METRICS


class Subscribe(PostgresBaseModel, DateTimeMixin):
    __tablename__ = "subscribe"
    __table_args__ = {
        "schema": METRICS_SCHEMA,
        "comment": "Table with all subscribers",
    }

    user_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{USERS_SCHEMA}.user.sid", ondelete="CASCADE"),
        index=True,
        comment="User SID",
    )
    subscriber_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{USERS_SCHEMA}.user.sid", ondelete="CASCADE"),
        index=True,
        comment="Subscriber SID",
    )
    is_notify: Mapped[bool] = mapped_column(
        default=True, server_default="true", comment="Notify status"
    )
