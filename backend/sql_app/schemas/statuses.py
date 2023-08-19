from typing import Optional
from pydantic import BaseModel


class StatusBase(BaseModel):
    name: Optional[str] = None


class StatusCreate(StatusBase):
    name: str


class StatusInDBBase(StatusBase):
    id: int
    name: str

    class Config:
        from_attributes = True
