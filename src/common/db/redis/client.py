from typing import Any

from redis import asyncio as aioredis

from config.settings import settings


class RedisTokenClient:
    _instance: Any = None
    _client: aioredis.Redis | None = None

    def __new__(cls) -> Any:
        if cls._instance is None:
            cls._instance = super(RedisTokenClient, cls).__new__(cls)
            redis_auth_client = aioredis.Redis(
                host=settings.redis.HOST,
                port=settings.redis.PORT,
                db=settings.redis.TOKEN_DB,
                encoding=settings.redis.ENCODING,
                decode_responses=settings.redis.DECODE,
            )
            cls._client = redis_auth_client
        return cls._instance

    @classmethod
    def get_async(cls) -> aioredis.Redis:
        if cls._instance is None:
            cls()
        assert cls._client is not None, "Redis client has not been initialized"
        return cls._client
