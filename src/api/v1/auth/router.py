from fastapi import APIRouter, Form, Path
from api import deps

from .paths import APIPath


router = APIRouter()


@router.post(path=APIPath.LOGIN)
async def login(
    use_case: deps.UseCase,
    username: str = Path(),
    password: str = Form(),
):
    pass
