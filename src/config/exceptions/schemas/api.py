from pydantic import Field

from common.schemas import CoreModel


class APIExceptionDetail(CoreModel):
    code: int = Field(..., description="Service code of error")
    description: str = Field(..., description="Description of error")


class APIException(CoreModel):
    status_code: int = Field(..., description="Status code of error")
    detail: APIExceptionDetail = Field(..., description="Detail of error")
