from enum import IntEnum, unique


@unique
class RoleLabel(IntEnum):
    SUPERUSER = 0
    ADMIN = 1
    USER = 2


@unique
class EventRoleLabel(IntEnum):
    CREATOR = 3
    SPEAKER = 4
    MEMBER = 5
