from typing import Optional
from pydantic import BaseModel


class StatusBase(BaseModel):
    name: str


class StatusCreate(StatusBase):
    pass


class StatusInDBBase(StatusBase):
    id: int
    name: str

    class Config:
        from_attributes = True
