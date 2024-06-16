from enum import StrEnum


class APIPath(StrEnum):
    SIGNUP = "/signup"
    LOGIN = "/login"
    REFRESH = "/refresh"
    LOGOUT = "/logout"
