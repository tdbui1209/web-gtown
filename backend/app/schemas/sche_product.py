from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    product_name: str
    product_price: int
    product_description: Optional[str] = None
    product_category_id: int

    class Config:
        from_attribute = True


class ProductCreate(ProductBase):
    pass


class ProductItem(ProductBase):
    id: int
