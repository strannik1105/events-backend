from enum import StrEnum


class APIPath(StrEnum):
    EXPORT_EVENT_FILE_BY_SID = "/files/{eventFileSid}"
    GET_EVENT_FILES = "/files"
    GET_EVENT_TYPES = "/types"
    GET_EVENT_CONTENT_TYPES = "/content/types"
    GET_EVENT_FILE_TYPES = "/file/types"
    CREATE_EVENT_FILE = "/file"
    REMOVE_EVENT_FILE_BY_SID = "/files/{eventFileSid}"
