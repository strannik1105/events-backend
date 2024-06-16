from typing import Annotated, AsyncIterator

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import AsyncSession

import services
import usecases
from common.db import postgres, redis
from common.managers import JWTManager
from config.exceptions import APIException
from enums import auth as auth_enums
from models import users as user_models
from schemas import auth as auth_schemas


async def get_pg_session() -> AsyncIterator[AsyncSession]:
    db = postgres.PostgresSession.get_async()
    try:
        yield db
    finally:
        await db.rollback()
        await db.close()


async def get_redis_token_client() -> aioredis.Redis:
    return redis.RedisTokenClient.get_async()


def get_use_case(
    pg_db: AsyncSession = Depends(get_pg_session),
) -> usecases.UseCase:
    return usecases.UseCase(pg_db)


def get_service(
    pg_db: AsyncSession = Depends(get_pg_session),
) -> services.Service:
    return services.Service(pg_db)


PgSession = Annotated[AsyncSession, Depends(get_pg_session)]
RedisTokenClient = Annotated[aioredis.Redis, Depends(get_redis_token_client)]
UseCase = Annotated[usecases.UseCase, Depends(get_use_case)]
Service = Annotated[services.Service, Depends(get_service)]


bearer_schema = HTTPBearer(auto_error=False)

AccessToken = Annotated[HTTPAuthorizationCredentials, Depends(bearer_schema)]


async def validate_access_token(
    access_token: AccessToken,
    redis_client: RedisTokenClient,
) -> auth_schemas.AuthTokensPayload:
    if not access_token:
        raise APIException.invalid_access_token
    access_token_str = access_token.credentials
    try:
        payload = await JWTManager.get_token_payload(
            redis_client=redis_client,
            token=access_token_str,
            token_type=auth_enums.JWTTypes.ACCESS,
        )
    except JWTError as exc:
        raise APIException.invalid_access_token from exc
    return auth_schemas.AuthTokensPayload.model_validate(payload)


AccessTokenPayload = Annotated[
    auth_schemas.AuthTokensPayload, Depends(validate_access_token)
]


async def get_current_user(
    service: Service,
    payload: AccessTokenPayload,
) -> user_models.User:
    return await service.user.get_user_by_sid(
        sid=payload.sub,
    )


CurrentUser = Annotated[user_models.User, Depends(get_current_user)]


async def get_current_active_user(
    current_user: CurrentUser,
) -> user_models.User:
    if not current_user.is_active:
        raise APIException.inactive_user
    return current_user


CurrentActiveUser = Annotated[
    user_models.User, Depends(get_current_active_user)
]

# class PermissionAccessActionValidate:
#     def __init__(self, permission: str, action: str):
#         self.permission = permission
#         self.action = action
#
#     def __call__(
#         self,
#         permissions: dict[str, str]
#         | None = Depends(get_current_user_permissions),
#     ):
#         if not permissions:
#             raise BackendException(error=ErrorCodes.not_allowed)
#
#         if self.action not in permissions.get(self.permission, ""):
#             raise BackendException(error=ErrorCodes.not_allowed)
