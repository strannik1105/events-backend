from enum import StrEnum, unique


@unique
class PermissionLabel(StrEnum):
    READ = "R"
    CREATE = "C"
    UPDATE = "U"
    DELETE = "D"
    EXPORT = "E"
