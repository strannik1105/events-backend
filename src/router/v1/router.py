from fastapi import APIRouter

from router.v1.events import event
from router.v1.users import user


router = APIRouter(prefix="/v1")
router.include_router(user.router, prefix="/users", tags=["Пользователи"])
router.include_router(event.router, prefix="/events", tags=["События"])
