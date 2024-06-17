from fastapi import APIRouter

from .prefixes import APIPrefixes
from .v1 import auth, events, security


class Router:
    @staticmethod
    def _include_routers(router: APIRouter) -> APIRouter:
        router.include_router(
            auth.router, prefix=APIPrefixes.AUTH, tags=["Auth"]
        )
        router.include_router(
            security.router, prefix=APIPrefixes.SECURITY, tags=["Security"]
        )
        router.include_router(
            events.router, prefix=APIPrefixes.EVENT, tags=["Event"]
        )
        return router

    @classmethod
    def get(cls) -> APIRouter:
        return cls._include_routers(APIRouter())
