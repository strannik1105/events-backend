from enum import Enum, StrEnum, unique


@unique
class PermissionLabel(Enum):
    USER = 0
    EVENT = 1
    EVENT_CONTENT = 2
    EVENT_FILE = 3
    EVENT_SPEAKER_FILE = 4


@unique
class PermissionAccessAction(StrEnum):
    READ = "R"
    CREATE = "C"
    UPDATE = "U"
    DELETE = "D"
    EXPORT = "E"
