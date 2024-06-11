from datetime import UTC, datetime

import pytz

from config.settings import settings


class DateTimeManager:
    _default_tz = settings.tz.MOSCOW

    @staticmethod
    def get_utcnow() -> datetime:
        return datetime.now(UTC)

    @classmethod
    def get_utcnow_w_timezone(cls, timezone: str | None = None) -> datetime:
        if not timezone:
            timezone = cls._default_tz
        return datetime.now(UTC).astimezone(pytz.timezone(timezone))
