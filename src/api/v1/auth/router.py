from typing import Annotated, Any

from fastapi import APIRouter, Form, Path

from api import deps
from api.params import APIParam
from enums import security as security_enums
from models import users as user_models
from schemas import auth as auth_schemas
from schemas import users as user_schemas

from .paths import APIPath


router = APIRouter()


@router.post(path=APIPath.SIGNUP, response_model=user_schemas.User)
async def signup(
    use_case: deps.UseCase,
    user_in: Annotated[
        user_schemas.UserCreateWithoutRoleLabel, APIParam.body(...)
    ],
) -> user_models.User:
    return await use_case.user.create_user(
        user_in=user_schemas.UserCreate(
            **user_in.model_dump(),
            role_label=security_enums.RoleLabel.USER,
        )
    )


@router.post(path=APIPath.LOGIN, response_model=auth_schemas.AuthTokens)
async def login(
    use_case: deps.UseCase,
    redis_client: deps.RedisTokenClient,
    login_in: Annotated[auth_schemas.LogIn, APIParam.body(...)],
) -> auth_schemas.AuthTokens:
    return await use_case.auth.login(
        redis_client=redis_client,
        login_in=login_in,
    )


@router.post(path=APIPath.REFRESH, response_model=auth_schemas.AuthTokens)
async def refresh(
    use_case: deps.UseCase,
    username: str = Path(),
    password: str = Form(),
) -> auth_schemas.AuthTokens:
    pass


@router.post(path=APIPath.LOGOUT)
async def logout(
    use_case: deps.UseCase,
    username: str = Path(),
    password: str = Form(),
) -> Any:
    pass
