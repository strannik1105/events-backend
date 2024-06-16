from datetime import datetime
from uuid import UUID

from pydantic import Field

from common.schemas import CoreModel
from enums import auth as auth_enums
from enums import security as security_enums


class AccessToken(CoreModel):
    access_token: str = Field(..., description="Access token")


class RefreshToken(CoreModel):
    refresh_token: str = Field(..., description="Refresh token")


class AuthTokens(RefreshToken, AccessToken):
    pass


class JWTCreds(CoreModel):
    sub: UUID = Field(..., description="JWT subscriber")
    jti: UUID = Field(..., description="JWT ID")
    type: auth_enums.JWTTypes = Field(..., description="JWT token type")


class JWTPayload(CoreModel):
    sub: UUID = Field(..., description="JWT subscriber")
    jti: UUID = Field(..., description="JWT ID")
    type: auth_enums.JWTTypes = Field(..., description="JWT token type")
    exp: datetime = Field(..., description="JWT expired at")


class AuthTokensCreatePayload(CoreModel):
    role_label: security_enums.RoleLabel = Field(..., description="Role label")


class AuthTokensPayload(AuthTokensCreatePayload, JWTPayload):
    pass
