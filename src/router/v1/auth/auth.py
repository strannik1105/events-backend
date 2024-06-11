from typing import Annotated

from auth import utils as auth_utils
from fastapi import APIRouter, Depends, Form, Path

from router.deps import PGSession, get_auth_service
from router.v1.auth.schemas import TokenInfo
from services.auth.auth_service import AuthService


router = APIRouter()


@router.post("/login/{username}", response_model=TokenInfo)
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
