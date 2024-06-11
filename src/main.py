import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import settings
from middlewares import APIExceptionMiddleware
from router.api import api_router


app = FastAPI(
    debug=settings.app.LOCAL_MODE is True,
    openapi_url=f"{settings.api.V1}/openapi.json",
    title=settings.app.NAME,
    version=settings.app.VERSION,
)

app.middleware("http")(APIExceptionMiddleware.internal_error)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.app.V1)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.app.LOCAL_MODE is True,
        workers=settings.app.WORKERS_NUM,
    )
