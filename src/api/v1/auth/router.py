from typing import Annotated

from fastapi import APIRouter, Depends, Form, Path
from router import utils as auth_utils
from router.deps import PGSession, get_auth_service

from services.auth.service import AuthService

from .paths import APIPath


router = APIRouter()


@router.post(path=APIPath.LOGIN)
async def login(
    db: PGSession,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
    username: str = Path(description="имя пользователя"),
    password: str = Form(),
):
    db_obj = await auth_service.authenticate(db, username, password)
    jwt_payload = {
        "username": db_obj.name,
    }
    token = auth_utils.encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer",
    )
