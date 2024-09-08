from enum import Enum, auto


class HttpMethod(str, Enum):
    GET: str = "GET"
    POST: str = "POST"
    PUT: str = "PUT"
    DELETE: str = "DELETE"
