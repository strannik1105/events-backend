from fastapi import HTTPException
from starlette import status

from common.tools import IteratorMeta
from config.exceptions import schemas


class APIExceptionBook(metaclass=IteratorMeta):
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
    resource_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=107,
            description="Resource already exists",
        ),
    )
    resource_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=108,
            description="Resource not found",
        ),
    )
    role_x_resource_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=109,
            description="Resource of role already exists",
        ),
    )
    role_x_resource_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=110,
            description="Resource of role not found",
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
    inactive_user = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=300,
            description="User was blocked",
        ),
    )
    unverified_user = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=301,
            description="User not verified",
        ),
    )
    user_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=302,
            description="User already exists",
        ),
    )
    user_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=303,
            description="User not found",
        ),
    )

    # --================ Event ================--
    event_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=400,
            description="Event already exists",
        ),
    )
    event_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=401,
            description="Event not found",
        ),
    )
    event_content_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=402,
            description="Event content already exists",
        ),
    )
    event_content_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=403,
            description="Event content not found",
        ),
    )
    event_pull_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=404,
            description="Event pull already exists",
        ),
    )
    event_pull_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=405,
            description="Event pull not found",
        ),
    )
    event_file_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=406,
            description="Event file already exists",
        ),
    )
    event_file_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=407,
            description="Event file not found",
        ),
    )
    event_file_type_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=408,
            description="Event file type already exists",
        ),
    )
    event_file_type_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=409,
            description="Event file type not found",
        ),
    )
    invalid_event_file_size = schemas.APIException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=schemas.APIExceptionDetail(
            code=410,
            description="Invalid event file size",
        ),
    )
    event_type_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=411,
            description="Event type already exists",
        ),
    )
    event_type_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=412,
            description="Event type not found",
        ),
    )
    event_content_type_already_exists = schemas.APIException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=schemas.APIExceptionDetail(
            code=413,
            description="Event content type already exists",
        ),
    )
    event_content_type_not_found = schemas.APIException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=schemas.APIExceptionDetail(
            code=414,
            description="Event content type not found",
        ),
    )


class APIException:
    # --================ Base ================--
    internal = HTTPException(
        status_code=APIExceptionBook.internal.status_code,
        detail=APIExceptionBook.internal.detail.model_dump(),
    )

    # --================ Security ================--
    not_allowed = HTTPException(
        status_code=APIExceptionBook.not_allowed.status_code,
        detail=APIExceptionBook.not_allowed.detail.model_dump(),
    )
    violation_role_branch = HTTPException(
        status_code=APIExceptionBook.violation_role_branch.status_code,
        detail=APIExceptionBook.violation_role_branch.detail.model_dump(),
    )
    violation_event_role_branch = HTTPException(
        status_code=APIExceptionBook.violation_event_role_branch.status_code,
        detail=APIExceptionBook.violation_event_role_branch.detail.model_dump(),
    )
    invalid_access_token = HTTPException(
        status_code=APIExceptionBook.invalid_access_token.status_code,
        detail=APIExceptionBook.invalid_access_token.detail.model_dump(),
    )
    invalid_refresh_token = HTTPException(
        status_code=APIExceptionBook.invalid_refresh_token.status_code,
        detail=APIExceptionBook.invalid_refresh_token.detail.model_dump(),
    )
    role_already_exists = HTTPException(
        status_code=APIExceptionBook.role_already_exists.status_code,
        detail=APIExceptionBook.role_already_exists.detail.model_dump(),
    )
    role_not_found = HTTPException(
        status_code=APIExceptionBook.role_not_found.status_code,
        detail=APIExceptionBook.role_not_found.detail.model_dump(),
    )
    resource_already_exists = HTTPException(
        status_code=APIExceptionBook.resource_already_exists.status_code,
        detail=APIExceptionBook.resource_already_exists.detail.model_dump(),
    )
    resource_not_found = HTTPException(
        status_code=APIExceptionBook.resource_not_found.status_code,
        detail=APIExceptionBook.resource_not_found.detail.model_dump(),
    )
    role_x_resource_already_exists = HTTPException(
        status_code=APIExceptionBook.role_x_resource_already_exists.status_code,
        detail=APIExceptionBook.role_x_resource_already_exists.detail.model_dump(),
    )
    role_x_resource_not_found = HTTPException(
        status_code=APIExceptionBook.role_x_resource_not_found.status_code,
        detail=APIExceptionBook.role_x_resource_not_found.detail.model_dump(),
    )
    invalid_password = HTTPException(
        status_code=APIExceptionBook.invalid_password.status_code,
        detail=APIExceptionBook.invalid_password.detail.model_dump(),
    )

    # --================ Auth ================--
    unidentified = HTTPException(
        status_code=APIExceptionBook.unidentified.status_code,
        detail=APIExceptionBook.unidentified.detail.model_dump(),
    )

    # --================ User ================--
    inactive_user = HTTPException(
        status_code=APIExceptionBook.inactive_user.status_code,
        detail=APIExceptionBook.inactive_user.detail.model_dump(),
    )
    unverified_user = HTTPException(
        status_code=APIExceptionBook.unverified_user.status_code,
        detail=APIExceptionBook.unverified_user.detail.model_dump(),
    )
    user_already_exists = HTTPException(
        status_code=APIExceptionBook.user_already_exists.status_code,
        detail=APIExceptionBook.user_already_exists.detail.model_dump(),
    )
    user_not_found = HTTPException(
        status_code=APIExceptionBook.user_not_found.status_code,
        detail=APIExceptionBook.user_not_found.detail.model_dump(),
    )

    # --================ Event ================--
    event_already_exists = HTTPException(
        status_code=APIExceptionBook.event_already_exists.status_code,
        detail=APIExceptionBook.event_already_exists.detail.model_dump(),
    )
    event_not_found = HTTPException(
        status_code=APIExceptionBook.event_not_found.status_code,
        detail=APIExceptionBook.event_not_found.detail.model_dump(),
    )
    event_content_already_exists = HTTPException(
        status_code=APIExceptionBook.event_content_already_exists.status_code,
        detail=APIExceptionBook.event_content_already_exists.detail.model_dump(),
    )
    event_content_not_found = HTTPException(
        status_code=APIExceptionBook.event_content_not_found.status_code,
        detail=APIExceptionBook.event_content_not_found.detail.model_dump(),
    )
    event_pull_already_exists = HTTPException(
        status_code=APIExceptionBook.event_pull_already_exists.status_code,
        detail=APIExceptionBook.event_pull_already_exists.detail.model_dump(),
    )
    event_pull_not_found = HTTPException(
        status_code=APIExceptionBook.event_pull_not_found.status_code,
        detail=APIExceptionBook.event_pull_not_found.detail.model_dump(),
    )
    event_file_already_exists = HTTPException(
        status_code=APIExceptionBook.event_file_already_exists.status_code,
        detail=APIExceptionBook.event_file_already_exists.detail.model_dump(),
    )
    event_file_not_found = HTTPException(
        status_code=APIExceptionBook.event_file_not_found.status_code,
        detail=APIExceptionBook.event_file_not_found.detail.model_dump(),
    )
    event_file_type_already_exists = HTTPException(
        status_code=APIExceptionBook.event_file_type_already_exists.status_code,
        detail=APIExceptionBook.event_file_type_already_exists.detail.model_dump(),
    )
    event_file_type_not_found = HTTPException(
        status_code=APIExceptionBook.event_file_type_not_found.status_code,
        detail=APIExceptionBook.event_file_type_not_found.detail.model_dump(),
    )
    invalid_event_file_size = HTTPException(
        status_code=APIExceptionBook.invalid_event_file_size.status_code,
        detail=APIExceptionBook.invalid_event_file_size.detail.model_dump(),
    )
    event_type_already_exists = HTTPException(
        status_code=APIExceptionBook.event_type_already_exists.status_code,
        detail=APIExceptionBook.event_type_already_exists.detail.model_dump(),
    )
    event_type_not_found = HTTPException(
        status_code=APIExceptionBook.event_type_not_found.status_code,
        detail=APIExceptionBook.event_type_not_found.detail.model_dump(),
    )
    event_content_type_already_exists = HTTPException(
        status_code=APIExceptionBook.event_content_type_already_exists.status_code,
        detail=APIExceptionBook.event_content_type_already_exists.detail.model_dump(),
    )
    event_content_type_not_found = HTTPException(
        status_code=APIExceptionBook.event_content_type_not_found.status_code,
        detail=APIExceptionBook.event_content_type_not_found.detail.model_dump(),
    )
