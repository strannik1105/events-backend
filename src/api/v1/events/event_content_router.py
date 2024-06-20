from fastapi import APIRouter

from api import deps
from models import events as event_models
from schemas import events as event_schemas

from .paths import APIPath


router = APIRouter()


@router.get(
    path=APIPath.GET_EVENT_CONTENT_TYPES,
    response_model=list[event_schemas.EventContentType],
)
async def get_event_content_types(
    _: deps.CurrentActiveUser,
    use_case: deps.UseCase,
) -> list[event_models.EventContentType]:
    return await use_case.event.get_event_content_types()
