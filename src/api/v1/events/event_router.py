from fastapi import APIRouter

from api import deps
from models import events as event_models
from schemas import events as event_schemas

from .paths import APIPath


router = APIRouter()


@router.get(
    path=APIPath.GET_EVENTS,
    response_model=list[event_schemas.Event],
)
async def get_events(
    usecase: deps.UseCase
):
    return await usecase.event.get_all()

@router.get(
    path=APIPath.GET_EVENT_TYPES,
    response_model=list[event_schemas.EventType],
)
async def get_event_types(
    _: deps.CurrentActiveUser,
    usecase: deps.UseCase,
) -> list[event_models.EventType]:
    return await usecase.event.get_event_types()
