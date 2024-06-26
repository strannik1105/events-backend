from typing import Annotated, Any, AsyncIterator

from botocore.client import BaseClient
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi_pagination import LimitOffsetParams
from jose import JWTError
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import AsyncSession

import services
import usecases
from common.db import postgres, redis, s3
from common.managers import JWTManager
from config.exceptions import APIException
from enums import auth as auth_enums
from enums import security as security_enums
from interfaces import services as i_services
from interfaces import usecases as i_usecases
from schemas import auth as auth_schemas
from schemas import users as user_schemas


async def get_pg_session() -> AsyncIterator[AsyncSession]:
    db = postgres.PostgresSession.get_async()
    try:
        yield db
    finally:
        await db.rollback()
        await db.close()


async def get_s3_client() -> BaseClient:
    return s3.S3Client.get()


async def get_redis_token_client() -> aioredis.Redis:
    return redis.RedisTokenClient.get_async()


def get_usecase(
    pg_db: AsyncSession = Depends(get_pg_session),
) -> i_usecases.IUseCase:
    return usecases.UseCase(pg_db)


def get_service(
    pg_db: AsyncSession = Depends(get_pg_session),
) -> i_services.IService:
    return services.Service(pg_db)


PgSession = Annotated[AsyncSession, Depends(get_pg_session)]
S3Client = Annotated[BaseClient, Depends(get_s3_client)]
RedisTokenClient = Annotated[aioredis.Redis, Depends(get_redis_token_client)]
UseCase = Annotated[i_usecases.IUseCase, Depends(get_usecase)]
Service = Annotated[i_services.IService, Depends(get_service)]


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
) -> user_schemas.CurrentUser:
    user = await service.user.get_user_by_sid(
        sid=payload.sub,
    )
    return user_schemas.CurrentUser(
        **user.__dict__,
        resource_permissions=payload.resource_permissions,
    )


CurrentUser = Annotated[user_schemas.CurrentUser, Depends(get_current_user)]


async def get_current_active_user(
    current_user: CurrentUser,
) -> user_schemas.CurrentUser:
    if not current_user.is_active:
        raise APIException.inactive_user
    return current_user


CurrentActiveUser = Annotated[
    user_schemas.CurrentUser, Depends(get_current_active_user)
]


class ResourcePermissionValidate:
    def __init__(
        self,
        resource_label: security_enums.ResourceLabel,
        permission_label: security_enums.PermissionLabel,
    ):
        self.resource_label = resource_label
        self.permission_label = permission_label

    def __call__(
        self,
        payload: Annotated[
            auth_schemas.AuthTokensPayload, Depends(validate_access_token)
        ],
    ) -> Any:
        if self.permission_label not in payload.resource_permissions.get(
            self.resource_label, ""
        ):
            raise APIException.not_allowed


PaginationParams = Annotated[LimitOffsetParams, Depends(LimitOffsetParams)]
