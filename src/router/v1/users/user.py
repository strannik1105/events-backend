from fastapi import APIRouter

from models.users.schemas import user

router = APIRouter()


@router.get("/", response_model=user.User)
def get_users():
    pass
