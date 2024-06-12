from enum import Enum, unique


@unique
class RoleLabel(Enum):
    SUPERUSER = 0
    ADMIN = 1
    USER = 2


@unique
class EventRoleLabel(Enum):
    CREATOR = 3
    SPEAKER = 4
    MEMBER = 5
