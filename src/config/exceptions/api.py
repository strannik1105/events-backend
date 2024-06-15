from fastapi import HTTPException
from starlette import status

from common.tools import Iterator
from config.exceptions import schemas


class APIExceptionBook(metaclass=Iterator):
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
    violation_role_branch = schemas.APIException(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        detail=schemas.APIExceptionDetail(
            code=101,
            description="Violation role branch",
        ),
    )
    violation_event_role_branch = schemas.APIException(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        detail=schemas.APIExceptionDetail(
            code=102,
            description="Violation event role branch",
        ),
    )
    invalid_access_token = schemas.APIException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=schemas.APIExceptionDetail(
            code=103,
            description="Invalid access token",
        ),
    )
    invalid_refresh_token = schemas.APIException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=schemas.APIExceptionDetail(
            code=104,
            description="Invalid refresh token",
        ),
    )
    role_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=105,
            description="Role already exists",
        ),
    )
    role_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=106,
            description="Role not found",
        ),
    )
    permission_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=107,
            description="Permission already exists",
        ),
    )
    permission_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=108,
            description="Permission not found",
        ),
    )
    role_x_permission_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=109,
            description="Permission of role already exists",
        ),
    )
    role_x_permission_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=110,
            description="Permission of role not found",
        ),
    )
    invalid_password = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=111,
            description="Invalid password",
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
    user_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=300,
            description="User already exists",
        ),
    )
    user_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=301,
            description="User not found",
        ),
    )

    # --================ Event ================--
    event_file_type_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=400,
            description="Event file type already exists",
        ),
    )
    event_file_type_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=401,
            description="Event file type not found",
        ),
    )


class APIException:
    # --================ Base ================--
    internal = HTTPException(
        status_code=APIExceptionBook.internal.status_code,
        detail=APIExceptionBook.internal.detail,
    )

    # --================ Security ================--
    not_allowed = HTTPException(
        status_code=APIExceptionBook.not_allowed.status_code,
        detail=APIExceptionBook.not_allowed.detail,
    )
    violation_role_branch = HTTPException(
        status_code=APIExceptionBook.violation_role_branch.status_code,
        detail=APIExceptionBook.violation_role_branch.detail,
    )
    violation_event_role_branch = HTTPException(
        status_code=APIExceptionBook.violation_event_role_branch.status_code,
        detail=APIExceptionBook.violation_event_role_branch.detail,
    )
    invalid_access_token = HTTPException(
        status_code=APIExceptionBook.invalid_access_token.status_code,
        detail=APIExceptionBook.invalid_access_token.detail,
    )
    invalid_refresh_token = HTTPException(
        status_code=APIExceptionBook.invalid_refresh_token.status_code,
        detail=APIExceptionBook.invalid_refresh_token.detail,
    )
    role_already_exists = HTTPException(
        status_code=APIExceptionBook.role_already_exists.status_code,
        detail=APIExceptionBook.role_already_exists.detail,
    )
    role_not_found = HTTPException(
        status_code=APIExceptionBook.role_not_found.status_code,
        detail=APIExceptionBook.role_not_found.detail,
    )
    permission_already_exists = HTTPException(
        status_code=APIExceptionBook.permission_already_exists.status_code,
        detail=APIExceptionBook.permission_already_exists.detail,
    )
    permission_not_found = HTTPException(
        status_code=APIExceptionBook.permission_not_found.status_code,
        detail=APIExceptionBook.permission_not_found.detail,
    )
    role_x_permission_already_exists = HTTPException(
        status_code=APIExceptionBook.role_x_permission_already_exists.status_code,
        detail=APIExceptionBook.role_x_permission_already_exists.detail,
    )
    role_x_permission_not_found = HTTPException(
        status_code=APIExceptionBook.role_x_permission_not_found.status_code,
        detail=APIExceptionBook.role_x_permission_not_found.detail,
    )
    invalid_password = HTTPException(
        status_code=APIExceptionBook.invalid_password.status_code,
        detail=APIExceptionBook.invalid_password.detail,
    )

    # --================ Auth ================--
    unidentified = HTTPException(
        status_code=APIExceptionBook.unidentified.status_code,
        detail=APIExceptionBook.unidentified.detail,
    )

    # --================ User ================--
    user_already_exists = HTTPException(
        status_code=APIExceptionBook.user_already_exists.status_code,
        detail=APIExceptionBook.user_already_exists.detail,
    )
    user_not_found = HTTPException(
        status_code=APIExceptionBook.user_not_found.status_code,
        detail=APIExceptionBook.user_not_found.detail,
    )

    # --================ Event ================--
    event_file_type_already_exists = HTTPException(
        status_code=APIExceptionBook.event_file_type_already_exists.status_code,
        detail=APIExceptionBook.event_file_type_already_exists.detail,
    )
    event_file_type_not_found = HTTPException(
        status_code=APIExceptionBook.event_file_type_not_found.status_code,
        detail=APIExceptionBook.event_file_type_not_found.detail,
    )
