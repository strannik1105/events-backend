from enum import Enum, StrEnum, auto


class Role(Enum):
    SUPERUSER = 0
    ADMIN = 1
    MEMBER = 2


class EventRole(StrEnum):
    ORGANIZER = auto()
    MEMBER = auto()
