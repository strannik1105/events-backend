from enum import StrEnum, unique


@unique
class APIPrefixes(StrEnum):
    AUTH = "/auth"
    USER = "/user"
    SECURITY = "/security"
    EVENT = "/event"
