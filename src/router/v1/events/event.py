from typing import Optional

from models.events import schemas
from fastapi import APIRouter

from router import deps

router = APIRouter()


@router.get("/", response_model=Optional[list[schemas.event.Event]])
async def get_events(
    pg_session: deps.PGSession,
    event_service: deps.EventService,
    event_repository: deps.EventRepository,
):
    items = await event_service.get_all_events(event_repository, pg_session)
    return items
