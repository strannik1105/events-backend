from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import AsyncSession

from common import enums, schemas
from common.managers import DateTimeManager, SecurityManager
from schemas import auth as auth_schemas
from usecases.core import CoreUseCase


class AuthUseCase(CoreUseCase):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)

    async def login(
        self,
        redis_client: aioredis.Redis,
        login_in: auth_schemas.LogIn,
    ) -> auth_schemas.AuthTokens:
        user = await self._service.user.get_user_by_email(
            email=login_in.email,
        )
        SecurityManager.verify_password(
            password=login_in.password,
            hashed_password=user.hashed_password,
        )
        user = await self._service.user.update_last_login_at(
            user=user,
            last_login_at=DateTimeManager.get_utcnow_without_timezone(),
        )
        return await self._service.auth.get_auth_tokens(
            redis_client=redis_client,
            user=user,
        )

    async def refresh(
        self,
        redis_client: aioredis.Redis,
        refresh_token: str,
    ) -> auth_schemas.AuthTokens:
        return await self._service.auth.refresh_auth_tokens(
            redis_client=redis_client,
            refresh_token=refresh_token,
        )

    async def logout(
        self,
        redis_client: aioredis.Redis,
        access_token_payload: auth_schemas.AuthTokensPayload,
        is_everywhere: bool,
    ) -> schemas.Msg:
        await self._service.auth.logout(
            redis_client=redis_client,
            access_token_payload=access_token_payload,
            is_everywhere=is_everywhere,
        )
        return schemas.Msg(msg=enums.ResponseMessages.SUCCESS)
