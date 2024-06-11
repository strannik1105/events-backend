from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from common.base import DateTimeManager


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=DateTimeManager.get_utcnow,
        comment="DateTime of create record",
    )


class UpdatedAtMixin:
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=DateTimeManager.get_utcnow,
        onupdate=DateTimeManager.get_utcnow,
        comment="DateTime of update record",
    )


class DateTimeMixin(CreatedAtMixin, UpdatedAtMixin):
    pass
