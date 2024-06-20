from uuid import uuid4

from jose import JWTError
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import AsyncSession

from common.managers import JWTManager
from common.sql.options import users as user_options
from config.exceptions import APIException
from enums import auth as auth_enums
from models import users as user_models
from schemas import auth as auth_schemas
from services.core import CoreService

from .utils import AuthServiceUtils


class AuthService(CoreService):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
        self._utils = AuthServiceUtils(pg_db)

    async def get_auth_tokens(
        self, redis_client: aioredis.Redis, user: user_models.User
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
                resource_permissions=self._utils.get_resource_permissions(
                    role=user.role,
                ),
            ),
        )
        refresh_token = JWTManager.get_token(
            creds=refresh_token_creds,
            payload=auth_schemas.AuthTokensCreatePayload(
                role_label=user.role_label,
                resource_permissions=self._utils.get_resource_permissions(
                    role=user.role,
                ),
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

    async def refresh_auth_tokens(
        self,
        redis_client: aioredis.Redis,
        refresh_token: str,
    ) -> auth_schemas.AuthTokens:
        try:
            payload = await JWTManager.get_token_payload(
                redis_client=redis_client,
                token=refresh_token,
                token_type=auth_enums.JWTTypes.REFRESH,
            )
        except JWTError as exc:
            raise APIException.invalid_refresh_token from exc

        creds = auth_schemas.JWTCreds.model_validate(payload)
        user = await self.repository.user.get_by_sid(
            sid=creds.sub,
            custom_options=user_options.SQLUserOptions.permissions(),
        )

        await JWTManager.remove_token(
            redis_client=redis_client,
            creds=creds,
        )

        return await self.get_auth_tokens(
            redis_client=redis_client,
            user=user,
        )

    @staticmethod
    async def logout(
        redis_client: aioredis.Redis,
        access_token_payload: auth_schemas.AuthTokensPayload,
        is_everywhere: bool,
    ) -> None:
        creds = auth_schemas.JWTCreds.model_validate(access_token_payload)
        if is_everywhere:
            await JWTManager.remove_all_tokens(
                redis_client=redis_client, creds=creds
            )
        else:
            await JWTManager.remove_token(
                redis_client=redis_client, creds=creds
            )
