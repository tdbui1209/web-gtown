from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str
    price: float
    description: str


class Product(ProductBase):
    id: int
    category_id: int

    class Config:
        from_attributes = True
