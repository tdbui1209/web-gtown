from sqlalchemy import Column, Integer, ForeignKey, String

from app.models.model_base import Base


class Products(Base):
    product_name = Column(String(100), nullable=False)
    product_price = Column(Integer, nullable=False)
    product_description = Column(String(200), nullable=True)
    product_category_id = Column(Integer, ForeignKey('productcategories.id'))
