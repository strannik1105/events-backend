from datetime import datetime

from pydantic import BaseModel, Field


class CreatedAtMixin(BaseModel):
    created_at: datetime = Field(..., description="DateTime of create record")


class UpdatedAtMixin(BaseModel):
    updated_at: datetime = Field(..., description="DateTime of update record")


class DateTimeMixin(UpdatedAtMixin, CreatedAtMixin):
    pass
