from typing import Optional
from uuid import UUID
from common.schemas.schemas import BaseSchema


class ImageDescr(BaseSchema):
    sid: Optional[UUID]
    name: str
    image: str


class ImageCreate(BaseSchema):
    sid: Optional[UUID]
    name: str
    size: int
