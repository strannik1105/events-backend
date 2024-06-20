import asyncio

import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from starlette.middleware.cors import CORSMiddleware

from api.docs import APIDoc
from api.router import Router
from config.settings import settings
from middlewares.exceptions import APIExceptionMiddleware
from scripts.connection import PostgresConnection
from scripts.init import EventInit, S3Init, SecurityInit, UserInit


app = FastAPI(
    debug=settings.app.LOCAL_MODE,
    openapi_url=f"{settings.api.V1}/{settings.api.OPENAPI_URL}",
    title=settings.app.NAME,
    version=settings.app.VERSION,
    openapi_tags=APIDoc.get_tags(),
    description=APIDoc.get_description(),
)

app.middleware("http")(APIExceptionMiddleware.internal_error)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Router.get(), prefix=settings.api.V1)

add_pagination(app)


async def init() -> None:
    await PostgresConnection.ping()
    await S3Init.events_bucket()
    await SecurityInit.set_roles()
    await SecurityInit.set_resources()
    await SecurityInit.set_role_x_resources()
    await EventInit.set_event_types()
    await EventInit.set_event_content_types()
    await EventInit.set_event_file_types()
    await UserInit.superuser()


def run() -> None:
    uvicorn.run(
        "main:app",
        host=settings.api.HOST,
        port=settings.api.PORT,
        reload=settings.app.LOCAL_MODE,
        workers=settings.app.WORKERS_NUM,
    )


if __name__ == "__main__":
    asyncio.run(init())
    run()
