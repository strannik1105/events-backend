from datetime import timedelta

import jwt

from common.base import DateTimeManager
from config.settings import settings


class JWTManager:
    _secret_key = settings.jwt.SECRET_KEY
    _algorithm = settings.jwt.ALGORITHM
    _expire_minutes = settings.jwt.ACCESS_TOKEN_EXPIRE_MINUTES

    @classmethod
    def encode(
        cls,
        payload: dict,
        expire_timedelta: timedelta | None = None,
    ) -> str:
        to_encode = payload.copy()
        now = DateTimeManager.get_utcnow()

        if expire_timedelta:
            expire = now + expire_timedelta
        else:
            expire = now + timedelta(minutes=cls._expire_minutes)

        to_encode.update(
            exp=expire,
            iat=now,
        )

        encoded = jwt.encode(
            payload=to_encode,
            key=cls._secret_key,
            algorithm=cls._algorithm,
        )

        return encoded

    @classmethod
    def decode(
        cls,
        token: str | bytes,
    ) -> dict:
        return jwt.decode(
            jwt=token,
            key=cls._secret_key,
            algorithms=[cls._algorithm],
        )
