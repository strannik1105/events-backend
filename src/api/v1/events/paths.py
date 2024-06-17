from enum import StrEnum


class APIPath(StrEnum):
    GET_EVENT_FILE_BY_SID = "/file/{eventFileSid}"
    GET_EVENT_FILES = "/files"
    GET_EVENT_FILE_TYPES = "/file/types"
    CREATE_EVENT_FILE = "/file"
    REMOVE_EVENT_FILE_BY_SID = "/file/{eventFileSid}"
