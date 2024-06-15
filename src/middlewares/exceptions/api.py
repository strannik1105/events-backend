from typing import Any

from fastapi import Request
from starlette.responses import JSONResponse

from common.managers import LoggerManager
from config.exceptions import APIExceptionBook


class APIExceptionMiddleware:
    @staticmethod
    async def internal_error(request: Request, call_next: Any) -> Any:
        try:
            return await call_next(request)
        except Exception as exc:
            logger = LoggerManager.get_base_logger()
            logger.error(f"Internal server error: {exc}", exc_info=True)
            return JSONResponse(
                status_code=APIExceptionBook.internal.status_code,
                content=APIExceptionBook.internal.detail,
            )
