from fastapi import HTTPException
from starlette import status

from common.base import Iterator
from config.exceptions import schemas


class APIExceptionBody(metaclass=Iterator):
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
        status_code=APIExceptionBody.internal.status_code,
        detail=APIExceptionBody.internal.detail,
    )
    unauthorized = HTTPException(
        status_code=APIExceptionBody.unauthorized.status_code,
        detail=APIExceptionBody.unauthorized.detail,
    )
