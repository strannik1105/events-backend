from pydantic import BaseModel, Field


class Msg(BaseModel):
    msg: str = Field(..., description="Some message")
