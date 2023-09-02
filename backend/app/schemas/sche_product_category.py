from typing import Optional

from pydantic import BaseModel


class ProductCategoryBase(BaseModel):
    product_category_name: str

    class Config:
        from_attribute = True


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategoryItem(ProductCategoryBase):
    id: int
