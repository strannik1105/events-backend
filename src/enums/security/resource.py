from enum import IntEnum, unique


@unique
class ResourceLabel(IntEnum):
    USER = 0
    EVENT = 1
    EVENT_CONTENT = 2
    EVENT_FILE = 3
    EVENT_SPEAKER_FILE = 4
