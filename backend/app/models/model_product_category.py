from sqlalchemy import Column, Integer, String

from .model_base import Base


class ProductCategories(Base):
    product_category_name = Column(
        String(20), nullable=False, unique=True, index=True
    )
