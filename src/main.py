import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from starlette.middleware.cors import CORSMiddleware

from api.docs import APIDoc
from api.router import Router
from config.settings import settings
from middlewares.exceptions import APIExceptionMiddleware


app = FastAPI(
    debug=settings.app.LOCAL_MODE is True,
    openapi_url=f"{settings.api.V1}/openapi.json",
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

app.include_router(Router.get(), prefix=settings.app.V1)

add_pagination(app)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.app.LOCAL_MODE is True,
        workers=settings.app.WORKERS_NUM,
    )
