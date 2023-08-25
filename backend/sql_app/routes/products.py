from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import products
from database.connection import get_session
from models.models import Products, Categories


product_router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@product_router.get("/", response_model=list[products.ProductInDBBase])
async def read_products(skip: int = 0, limit: int = 100,
                        db: Session = Depends(get_session)):
    return db.query(Products).offset(skip).limit(limit).all()


@product_router.post("/", response_model=products.ProductInDBBase,
                     status_code=status.HTTP_201_CREATED)
async def create_product(product: products.ProductCreate,
                         db: Session = Depends(get_session)):
    db_category = db.query(Categories).filter(
        Categories.id == product.category_id).one()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Category not found")
    db_product = Products(name=product.name, price=product.price,
                          description=product.description,
                          category_id=product.category_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@product_router.put("/", response_model=products.ProductInDBBase)
async def update_product(product: products.ProductUpdate,
                         db: Session = Depends(get_session)):
    db_product = db.query(Products).filter(Products.id == product.id).one()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    if product.name:
        db_product.name = product.name
    if product.price:
        db_product.price = product.price
    if product.description:
        db_product.description = product.description
    if product.category_id:
        db_category = db.query(Categories).filter(
            Categories.id == product.category_id).one()
        if not db_category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Category not found")
        db_product.category_id = product.category_id
    db.commit()
    return db_product


@product_router.delete("/", response_model=products.ProductDelete)
async def delete_product(product: products.ProductDelete,
                         db: Session = Depends(get_session)):
    db_product = db.query(Products).filter(Products.id == product.id).one()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    db.delete(db_product)
    db.commit()
    return db_product


@product_router.get("/{product_id}", response_model=products.ProductInDBBase)
async def read_product_by_id(product_id: int,
                       db: Session = Depends(get_session)):
    db_product = db.query(Products).filter(Products.id == product_id).one()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    return db_product


@product_router.get("/category/{category_id}",
                    response_model=list[products.ProductInDBBase])
async def read_products_by_category(category_id: int,
                                    db: Session = Depends(get_session)):
    db_category = db.query(Categories).filter(
        Categories.id == category_id).one()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Category not found")
    return db.query(Products).filter(
        Products.category_id == category_id).all()
