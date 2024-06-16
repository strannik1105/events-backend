from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.alias_generators import to_camel


class CoreModel(BaseModel):
    @field_validator("*", mode="after")
    def timezone_validate(cls, v: Any) -> Any:
        if isinstance(v, datetime):
            if v.tzinfo is not None:
                v = v.replace(tzinfo=None)
        return v

    model_config = ConfigDict(
        from_attributes=True, populate_by_name=True, alias_generator=to_camel
    )
