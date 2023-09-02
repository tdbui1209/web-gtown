import logging
from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from schemas.sche_product import ProductCreate, ProductItem
from models.model_product import Products


logger = logging.getLogger()
router = APIRouter()


@router.get('/', response_model=list[ProductItem])
def read_products():
    try:
        products = db.session.query(Products).all()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=logger.error(e))
    

@router.post('/', response_model=ProductCreate)
def create_product(product: ProductCreate):
    try:
        db_product = Products(
            product_name=product.product_name,
            product_price=product.product_price,
            product_description=product.product_description,
            product_category_id=product.product_category_id
        )
        db.session.add(db_product)
        db.session.commit()
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=logger.error(e))
