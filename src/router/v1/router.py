from fastapi import APIRouter

from router.v1.events import event, event_content
from router.v1.users import user
from router.v1.auth import auth


router = APIRouter(prefix="/v1")
router.include_router(user.router, prefix="/users", tags=["Пользователи"])
router.include_router(event.router, prefix="/events", tags=["События"])
router.include_router(event_content.router, prefix="/event_content", tags=["События"])
router.include_router(auth.router, prefix="/auth", tags=["Регистрация"])
