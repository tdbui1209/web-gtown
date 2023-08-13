from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float, index=True)
    description = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))


class Status(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Users(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, index=True)
    status_id = Column(Integer, ForeignKey("status.id"))
