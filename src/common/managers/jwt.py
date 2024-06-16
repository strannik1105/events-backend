import json
from datetime import UTC, datetime, timedelta
from typing import Any

from jose import jwt
from pydantic import BaseModel
from redis import asyncio as aioredis

from config.exceptions import APIException
from config.settings import settings
from enums import auth as auth_enums
from schemas import auth as auth_schemas


class JWTManager:
    _secret_key: str = settings.jwt.SECRET_KEY
    _algorithm: str = settings.jwt.ALGORITHM

    _access: str = auth_enums.JWTTypes.ACCESS
    _refresh: str = auth_enums.JWTTypes.REFRESH

    _access_expire_seconds: int = settings.jwt.ACCESS_TOKEN_EXPIRE_SECONDS
    _refresh_expire_seconds: int = settings.jwt.REFRESH_TOKEN_EXPIRE_SECONDS
    _deactivate_expire_seconds: int = (
        settings.jwt.DEACTIVATE_TOKEN_EXPIRE_SECONDS
    )

    _activate_value: str = "True"
    _deactivate_value: str = "False"

    @classmethod
    def _raise_invalid_token_error(
        cls, token_type: auth_enums.JWTTypes
    ) -> None:
        if token_type == cls._access:
            raise APIException.invalid_access_token
        if token_type == cls._refresh:
            raise APIException.invalid_refresh_token

    @classmethod
    def _get_expire_seconds(cls, token_type: auth_enums.JWTTypes) -> int:
        expire = 0
        if token_type == cls._access:
            expire = cls._access_expire_seconds
        if token_type == cls._refresh:
            expire = cls._refresh_expire_seconds
        return expire

    @classmethod
    def _get_redis_key(cls, creds: auth_schemas.JWTCreds) -> str:
        return f"{creds.sub}:{creds.jti}"

    @classmethod
    def get_token(
        cls,
        creds: auth_schemas.JWTCreds,
        payload: BaseModel | dict[str, Any] | None = None,
    ) -> str:
        to_encode = json.loads(
            auth_schemas.JWTPayload(
                **creds.model_dump(),
                exp=datetime.now(UTC)
                + timedelta(seconds=cls._get_expire_seconds(creds.type)),
            ).model_dump_json()
        )

        if payload is not None:
            if isinstance(payload, BaseModel):
                to_encode.update(json.loads(payload.model_dump_json()))
            else:
                to_encode.update(payload)

        return jwt.encode(
            to_encode, key=cls._secret_key, algorithm=cls._algorithm
        )

    @classmethod
    async def get_token_payload(
        cls,
        redis_client: aioredis.Redis,
        token: str,
        token_type: auth_enums.JWTTypes,
    ) -> dict[str, Any]:
        payload = jwt.decode(
            token, key=cls._secret_key, algorithms=[cls._algorithm]
        )
        creds = auth_schemas.JWTCreds.model_validate(payload)

        if creds.type != token_type:
            cls._raise_invalid_token_error(token_type=token_type)

        if (
            await redis_client.get(cls._get_redis_key(creds=creds))
            != cls._activate_value
        ):
            cls._raise_invalid_token_error(token_type=token_type)

        return payload

    @classmethod
    async def activate_token(
        cls, redis_client: aioredis.Redis, creds: auth_schemas.JWTCreds
    ) -> None:
        await redis_client.setex(
            name=cls._get_redis_key(creds=creds),
            time=cls._get_expire_seconds(token_type=creds.type),
            value=cls._activate_value,
        )

    @classmethod
    async def remove_token(
        cls,
        redis_client: aioredis.Redis,
        creds: auth_schemas.JWTCreds,
        is_delete: bool = True,
    ) -> None:
        if is_delete:
            await redis_client.delete(cls._get_redis_key(creds=creds))
        else:
            await redis_client.setex(
                name=cls._get_redis_key(creds=creds),
                time=cls._deactivate_expire_seconds,
                value=cls._deactivate_value,
            )

    @classmethod
    async def deactivate_token_by_key(
        cls, redis_client: aioredis.Redis, key: str, is_delete: bool = True
    ) -> None:
        if is_delete:
            await redis_client.delete(key)
        else:
            await redis_client.setex(
                name=key,
                time=cls._deactivate_expire_seconds,
                value=cls._deactivate_value,
            )

    @classmethod
    async def exists_token(
        cls,
        redis_client: aioredis.Redis,
        creds: auth_schemas.JWTCreds,
    ) -> bool:
        is_exists = await redis_client.exists(cls._get_redis_key(creds=creds))
        return bool(is_exists)
