from abc import ABCMeta, abstractmethod

from redis import asyncio as aioredis

from common import schemas
from interfaces.usecases.core import ICoreUseCase
from schemas import auth as auth_schemas


class IAuthUseCase(ICoreUseCase, metaclass=ABCMeta):
    @abstractmethod
    async def login(
        self,
        redis_client: aioredis.Redis,
        login_in: auth_schemas.LogIn,
    ) -> auth_schemas.AuthTokens:
        raise NotImplementedError

    @abstractmethod
    async def refresh(
        self,
        redis_client: aioredis.Redis,
        refresh_token: str,
    ) -> auth_schemas.AuthTokens:
        raise NotImplementedError

    @abstractmethod
    async def logout(
        self,
        redis_client: aioredis.Redis,
        access_token_payload: auth_schemas.AuthTokensPayload,
        is_everywhere: bool,
    ) -> schemas.Msg:
        raise NotImplementedError
