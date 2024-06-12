from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class Sid(BaseModel):
    sid: UUID = Field(..., description="Record SID")


class Label(BaseModel):
    label: int = Field(..., ge=0, le=32767, description="Record label")


class CreatedAtMixin(BaseModel):
    created_at: datetime = Field(..., description="Record creating time")


class UpdatedAtMixin(BaseModel):
    updated_at: datetime = Field(..., description="Record updating time")


class DateTimeMixin(UpdatedAtMixin, CreatedAtMixin):
    pass
