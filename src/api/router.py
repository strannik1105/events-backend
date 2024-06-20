from fastapi import APIRouter

from .prefixes import APIPrefixes
from .v1 import auth, events, security, users


class Router:
    @staticmethod
    def _include_routers(router: APIRouter) -> APIRouter:
        router.include_router(
            auth.router, prefix=APIPrefixes.AUTH, tags=["Auth"]
        )
        router.include_router(
            users.router, prefix=APIPrefixes.USER, tags=["User"]
        )
        router.include_router(
            security.router, prefix=APIPrefixes.SECURITY, tags=["Security"]
        )
        router.include_router(
            events.event_router,
            prefix=APIPrefixes.EVENT,
            tags=["Event"],
        )
        router.include_router(
            events.event_content_router,
            prefix=APIPrefixes.EVENT,
            tags=["Event content"],
        )
        router.include_router(
            events.event_file_router,
            prefix=APIPrefixes.EVENT,
            tags=["Event file"],
        )
        return router

    @classmethod
    def get(cls) -> APIRouter:
        return cls._include_routers(APIRouter())
