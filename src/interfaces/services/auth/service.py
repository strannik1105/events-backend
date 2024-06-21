from abc import ABCMeta, abstractmethod

from redis import asyncio as aioredis

from interfaces.services.core import ICoreService
from models import users as user_models
from schemas import auth as auth_schemas


class IAuthService(ICoreService, metaclass=ABCMeta):
    @abstractmethod
    async def get_auth_tokens(
        self, redis_client: aioredis.Redis, user: user_models.User
    ) -> auth_schemas.AuthTokens:
        raise NotImplementedError

    @abstractmethod
    async def refresh_auth_tokens(
        self,
        redis_client: aioredis.Redis,
        refresh_token: str,
    ) -> auth_schemas.AuthTokens:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def logout(
        redis_client: aioredis.Redis,
        access_token_payload: auth_schemas.AuthTokensPayload,
        is_everywhere: bool,
    ) -> None:
        raise NotImplementedError
