from uuid import uuid4

from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import AsyncSession

from common.managers import JWTManager
from enums import auth as auth_enums
from models import users as user_models
from schemas import auth as auth_schemas
from services.core import CoreService


class AuthService(CoreService):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)

    @staticmethod
    async def get_jwt_tokens(
        redis_client: aioredis.Redis, user: user_models.User
    ) -> auth_schemas.AuthTokens:
        access_token_creds = auth_schemas.JWTCreds(
            sub=user.sid,
            jti=uuid4(),
            type=auth_enums.JWTTypes.ACCESS,
        )
        refresh_token_creds = auth_schemas.JWTCreds(
            sub=user.sid,
            jti=uuid4(),
            type=auth_enums.JWTTypes.REFRESH,
        )

        access_token = JWTManager.get_token(
            creds=access_token_creds,
            payload=auth_schemas.AuthTokensCreatePayload(
                role_label=user.role_label,
            ),
        )
        refresh_token = JWTManager.get_token(
            creds=refresh_token_creds,
            payload=auth_schemas.AuthTokensCreatePayload(
                role_label=user.role_label,
            ),
        )

        await JWTManager.activate_token(
            redis_client=redis_client,
            creds=access_token_creds,
        )
        await JWTManager.activate_token(
            redis_client=redis_client,
            creds=refresh_token_creds,
        )

        return auth_schemas.AuthTokens(
            access_token=access_token,
            refresh_token=refresh_token,
        )
