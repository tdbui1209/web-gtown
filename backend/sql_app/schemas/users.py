from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    username: str
    name: str
    email: str
    password: str


class UserInDBBase(UserBase):
    username: str
    name: str
    email: str
    password: str
    status_id: int

    class Config:
        from_attributes = True


class UserUpdate(UserBase):
    username: str
    password: Optional[str] = None
    status_id: Optional[int] = None


class UserLogin(UserBase):
    username: str
    password: str
