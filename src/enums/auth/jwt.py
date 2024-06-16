from enum import IntEnum, unique


@unique
class JWTTypes(IntEnum):
    ACCESS = 0
    REFRESH = 1
