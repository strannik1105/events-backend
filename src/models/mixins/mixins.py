from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import mapped_column


class CreatedChangedMixin:
    created_at = mapped_column(DateTime, default=func.now())
    created_by = mapped_column(ForeignKey("users.user.sid"))

    changed_at = mapped_column(DateTime)
    changed_by = mapped_column(ForeignKey("users.user.sid"))
