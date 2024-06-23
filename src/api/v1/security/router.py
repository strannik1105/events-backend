from typing import Annotated

from fastapi import APIRouter

from api import deps
from api.params import APIParam
from common.filters import FilterDepends
from filters import security as security_filters
from models import security as security_models
from schemas import security as security_schemas

from .paths import APIPath


router = APIRouter()


@router.get(
    path=APIPath.GET_ROLE_BY_LABEL, response_model=security_schemas.Role
)
async def get_role_by_label(
    _: deps.CurrentActiveUser,
    usecase: deps.UseCase,
    role_label: Annotated[int, APIParam.path(..., alias="roleLabel")],
) -> security_models.Role:
    return await usecase.security.get_role_by_label(role_label=role_label)


@router.get(path=APIPath.GET_ROLES, response_model=list[security_schemas.Role])
async def get_roles(
    _: deps.CurrentActiveUser,
    usecase: deps.UseCase,
    filter_params: Annotated[
        security_filters.RoleFilter, FilterDepends(security_filters.RoleFilter)
    ],
) -> list[security_models.Role]:
    return await usecase.security.get_roles(filter_params=filter_params)
