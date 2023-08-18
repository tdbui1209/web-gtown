from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: Optional[str] = None


class CategoryCreate(CategoryBase):
    name: str


class CategoryInDBBase(CategoryBase):
    id: int
    name: str

    class Config:
        orm_mode = True
