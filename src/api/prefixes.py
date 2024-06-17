from enum import StrEnum, unique


@unique
class APIPrefixes(StrEnum):
    AUTH = "/auth"
    SECURITY = "/security"
    EVENT = "/event"
