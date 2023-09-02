from typing import Optional

from pydantic import BaseModel


class ProductCategoryBase(BaseModel):
    pass

    class Config:
        from_attribute = True


class ProductCategoryCreate(ProductCategoryBase):
    product_category_name: str


class ProductCategoryItem(ProductCategoryBase):
    id: int
    product_category_name: str
