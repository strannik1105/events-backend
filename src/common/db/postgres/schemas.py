from enum import StrEnum, unique


@unique
class PostgresDBSchemas(StrEnum):
    USERS = "users"
    EVENTS = "events"
    SECURITY = "security"
    METRICS = "metrics"
