from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    username: str
    name: str
    email: str
    password: str
    status_id: int


class UserInDBBase(UserBase):
    username: str
    name: str
    email: str
    password: str
    status_id: int

    class Config:
        from_attributes = True
