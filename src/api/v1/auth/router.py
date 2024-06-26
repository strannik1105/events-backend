from typing import Annotated

from fastapi import APIRouter

from api import deps
from api.params import APIParam
from common import schemas as common_schemas
from enums import security as security_enums
from models import users as user_models
from schemas import auth as auth_schemas
from schemas import users as user_schemas

from .paths import APIPath


router = APIRouter()


@router.post(path=APIPath.SIGNUP, response_model=user_schemas.User)
async def signup(
    usecase: deps.UseCase,
    user_in: Annotated[
        user_schemas.UserDTOCreateWithoutRoleLabel, APIParam.body(...)
    ],
) -> user_models.User:
    return await usecase.user.create_user(
        user_in=user_schemas.UserDTOCreate(
            **user_in.model_dump(),
            role_label=security_enums.RoleLabel.USER,
        )
    )


@router.post(path=APIPath.LOGIN, response_model=auth_schemas.AuthTokens)
async def login(
    usecase: deps.UseCase,
    redis_client: deps.RedisTokenClient,
    login_in: Annotated[auth_schemas.LogIn, APIParam.body(...)],
) -> auth_schemas.AuthTokens:
    return await usecase.auth.login(
        redis_client=redis_client,
        login_in=login_in,
    )


@router.post(path=APIPath.REFRESH, response_model=auth_schemas.AuthTokens)
async def refresh(
    usecase: deps.UseCase,
    redis_client: deps.RedisTokenClient,
    refresh_token: Annotated[
        str, APIParam.body(..., alias="refreshToken", embed=True)
    ],
) -> auth_schemas.AuthTokens:
    return await usecase.auth.refresh(
        redis_client=redis_client,
        refresh_token=refresh_token,
    )


@router.post(path=APIPath.LOGOUT, response_model=common_schemas.Msg)
async def logout(
    access_token_payload: deps.AccessTokenPayload,
    usecase: deps.UseCase,
    redis_client: deps.RedisTokenClient,
    is_everywhere: Annotated[bool, APIParam.query(..., alias="isEverywhere")],
) -> common_schemas.Msg:
    return await usecase.auth.logout(
        redis_client=redis_client,
        access_token_payload=access_token_payload,
        is_everywhere=is_everywhere,
    )
