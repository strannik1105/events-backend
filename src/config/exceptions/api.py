from fastapi import HTTPException
from starlette import status

from config.exceptions import schemas


class APIExceptionBook:
    internal = schemas.APIException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=schemas.APIExceptionDetail(
            code=1,
            description="Item not found",
        ),
    )
    unauthorized = schemas.APIException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=schemas.APIExceptionDetail(
            code=2,
            description="Invalid username or password",
        ),
    )


class APIException:
    not_found = HTTPException(
        status_code=APIExceptionBook.internal.status_code,
        detail=APIExceptionBook.internal.detail,
    )
    unauthorized = HTTPException(
        status_code=APIExceptionBook.unauthorized.status_code,
        detail=APIExceptionBook.unauthorized.detail,
    )
