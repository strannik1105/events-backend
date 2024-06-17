from enum import StrEnum


class APIPath(StrEnum):
    GET_ROLES = "/roles"
    GET_ROLE_BY_LABEL = "/roles/{roleLabel}"
