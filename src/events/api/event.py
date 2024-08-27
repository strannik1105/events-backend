from fastapi import APIRouter

class EventApi:
    router = APIRouter(prefix="/event")

    @router.get("")
    def get_all(self) -> None:
        pass
