from fastapi import HTTPException
from starlette import status

from common.tools import Iterator
from config.exceptions import schemas


class APIExceptionBody(metaclass=Iterator):
    # --================ Base ================--
    internal = schemas.APIException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=schemas.APIExceptionDetail(
            code=0,
            description="Internal server error",
        ),
    )

    # --================ Security ================--
    not_allowed = schemas.APIException(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        detail=schemas.APIExceptionDetail(
            code=100,
            description="Method not allowed",
        ),
    )
    invalid_access_token = schemas.APIException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=schemas.APIExceptionDetail(
            code=101,
            description="Invalid access token",
        ),
    )
    invalid_refresh_token = schemas.APIException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=schemas.APIExceptionDetail(
            code=102,
            description="Invalid refresh token",
        ),
    )

    # --================ Auth ================--
    unidentified = schemas.APIException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=schemas.APIExceptionDetail(
            code=200,
            description="Invalid authentication credentials",
        ),
    )

    # --================ User ================--
    user_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=300,
            description="User not found",
        ),
    )


class APIException:
    # --================ Base ================--
    internal = HTTPException(
        status_code=APIExceptionBody.internal.status_code,
        detail=APIExceptionBody.internal.detail,
    )

    # --================ Security ================--
    not_allowed = HTTPException(
        status_code=APIExceptionBody.not_allowed.status_code,
        detail=APIExceptionBody.not_allowed.detail,
    )
    invalid_access_token = HTTPException(
        status_code=APIExceptionBody.invalid_access_token.status_code,
        detail=APIExceptionBody.invalid_access_token.detail,
    )
    invalid_refresh_token = HTTPException(
        status_code=APIExceptionBody.invalid_refresh_token.status_code,
        detail=APIExceptionBody.invalid_refresh_token.detail,
    )

    # --================ Auth ================--
    unidentified = HTTPException(
        status_code=APIExceptionBody.unidentified.status_code,
        detail=APIExceptionBody.unidentified.detail,
    )

    # --================ User ================--
    user_not_found = HTTPException(
        status_code=APIExceptionBody.user_not_found.status_code,
        detail=APIExceptionBody.user_not_found.detail,
    )
