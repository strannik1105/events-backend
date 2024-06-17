from enum import StrEnum


class APIPath(StrEnum):
    GET_EVENT_FILE_TYPES = "/file/types"
    CREATE_EVENT_FILE = "/file"
