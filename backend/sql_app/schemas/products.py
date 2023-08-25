from typing import Optional
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: float
    description: str
    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductInDBBase(ProductBase):
    id: int
    category_id: int

    class Config:
        from_attributes = True


class ProductUpdate(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    category_id: Optional[int] = None


class ProductDelete(ProductBase):
    id: int
