from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi_pagination import LimitOffsetPage

from api import deps
from api.params import APIParam
from common import schemas as common_schemas
from enums import security as security_enums
from models import users as user_models
from schemas import users as user_schemas

from .paths import APIPath


router = APIRouter()


@router.get(
    path=APIPath.GET_ME,
    response_model=user_schemas.User,
)
async def get_me(
    current_user: deps.CurrentActiveUser,
) -> user_schemas.CurrentUser:
    return current_user


@router.get(
    path=APIPath.GET_USER_BY_SID,
    response_model=user_schemas.User,
    dependencies=[
        Depends(
            deps.ResourcePermissionValidate(
                resource_label=security_enums.ResourceLabel.USER,
                permission_label=security_enums.PermissionLabel.READ,
            ),
        )
    ],
)
async def get_user_by_sid(
    _: deps.CurrentActiveUser,
    use_case: deps.UseCase,
    user_sid: Annotated[UUID, APIParam.path(..., alias="userSid")],
) -> user_models.User:
    return await use_case.user.get_user_by_sid(user_sid=user_sid)


@router.get(
    path=APIPath.GET_USERS,
    response_model=LimitOffsetPage[user_schemas.User],
    dependencies=[
        Depends(
            deps.ResourcePermissionValidate(
                resource_label=security_enums.ResourceLabel.USER,
                permission_label=security_enums.PermissionLabel.READ,
            ),
        )
    ],
)
async def get_users(
    _: deps.PaginationParams,
    __: deps.CurrentActiveUser,
    use_case: deps.UseCase,
) -> LimitOffsetPage[user_models.User]:
    return await use_case.user.get_users()


@router.put(
    path=APIPath.UPDATE_ME,
    response_model=user_schemas.User,
)
async def update_me(
    current_user: deps.CurrentActiveUser,
    use_case: deps.UseCase,
    user_in: Annotated[user_schemas.UserUpdate, APIParam.body(...)],
) -> user_models.User:
    return await use_case.user.update_me(
        current_user=current_user,
        user_in=user_in,
    )


@router.put(
    path=APIPath.UPDATE_USER_BY_SID,
    response_model=user_schemas.User,
    dependencies=[
        Depends(
            deps.ResourcePermissionValidate(
                resource_label=security_enums.ResourceLabel.USER,
                permission_label=security_enums.PermissionLabel.UPDATE,
            ),
        )
    ],
)
async def update_user(
    current_user: deps.CurrentActiveUser,
    use_case: deps.UseCase,
    user_sid: Annotated[UUID, APIParam.path(..., alias="userSid")],
    user_in: Annotated[user_schemas.UserUpdate, APIParam.body(...)],
) -> user_models.User:
    return await use_case.user.update_user(
        current_user=current_user,
        user_sid=user_sid,
        user_in=user_in,
    )


@router.patch(
    path=APIPath.UPDATE_USER_ACTIVE_STATUS_BY_SID,
    response_model=user_schemas.User,
    dependencies=[
        Depends(
            deps.ResourcePermissionValidate(
                resource_label=security_enums.ResourceLabel.USER,
                permission_label=security_enums.PermissionLabel.UPDATE,
            ),
        )
    ],
)
async def update_user_active_status(
    current_user: deps.CurrentActiveUser,
    use_case: deps.UseCase,
    user_sid: Annotated[UUID, APIParam.path(..., alias="userSid")],
    is_active: Annotated[bool, APIParam.query(..., alias="isActive")],
) -> user_models.User:
    return await use_case.user.update_user_active(
        current_user=current_user,
        user_sid=user_sid,
        is_active=is_active,
    )


@router.patch(
    path=APIPath.UPDATE_USER_VERIFY_STATUS_BY_SID,
    response_model=user_schemas.User,
    dependencies=[
        Depends(
            deps.ResourcePermissionValidate(
                resource_label=security_enums.ResourceLabel.USER,
                permission_label=security_enums.PermissionLabel.UPDATE,
            ),
        )
    ],
)
async def update_user_verify_status(
    current_user: deps.CurrentActiveUser,
    use_case: deps.UseCase,
    user_sid: Annotated[UUID, APIParam.path(..., alias="userSid")],
    is_verify: Annotated[bool, APIParam.query(..., alias="isVerify")],
) -> user_models.User:
    return await use_case.user.update_user_verify(
        current_user=current_user,
        user_sid=user_sid,
        is_verify=is_verify,
    )


@router.delete(
    path=APIPath.REMOVE_USER_BY_SID,
    response_model=common_schemas.Msg,
    dependencies=[
        Depends(
            deps.ResourcePermissionValidate(
                resource_label=security_enums.ResourceLabel.USER,
                permission_label=security_enums.PermissionLabel.DELETE,
            ),
        )
    ],
)
async def remove_user(
    current_user: deps.CurrentActiveUser,
    use_case: deps.UseCase,
    user_sid: Annotated[UUID, APIParam.path(..., alias="userSid")],
) -> common_schemas.Msg:
    return await use_case.user.remove_user(
        current_user=current_user,
        user_sid=user_sid,
    )
