from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import SMALLINT, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from common.managers import DateTimeManager


class Sid:
    sid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)


class Label:
    label: Mapped[int] = mapped_column(SMALLINT, primary_key=True)


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=DateTimeManager.get_utcnow,
        comment="Record creating time",
    )


class UpdatedAtMixin:
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=DateTimeManager.get_utcnow,
        onupdate=DateTimeManager.get_utcnow,
        comment="Record updating time",
    )


class DateTimeMixin(CreatedAtMixin, UpdatedAtMixin):
    pass
