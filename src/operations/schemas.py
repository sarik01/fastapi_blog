from pydantic import BaseModel


class OperationCreate(BaseModel):
    title: str
    text: str
    instrument_type: str
    user_id: int

    type: str


class Role(BaseModel):
    name: str
