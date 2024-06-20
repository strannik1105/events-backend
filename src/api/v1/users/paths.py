from enum import StrEnum


class APIPath(StrEnum):
    GET_ME = "/me"
    GET_USER_BY_SID = "/users/{userSid}"
    GET_USERS = "/users"
    UPDATE_ME = "/me"
    UPDATE_USER_BY_SID = "/users/{userSid}"
    UPDATE_USER_ACTIVE_STATUS_BY_SID = "/users/{userSid}/active"
    UPDATE_USER_VERIFY_STATUS_BY_SID = "/users/{userSid}/verify"
    REMOVE_USER_BY_SID = "/users/{userSid}"
