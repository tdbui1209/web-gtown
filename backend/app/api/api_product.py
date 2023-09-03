import logging
from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from app.schemas.sche_product import ProductCreate, ProductItem
from app.models.model_product import Products
from app.models.model_product_category import ProductCategories


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


@router.get('/categories/{category}', response_model=list[ProductItem])
def read_products_by_category(category: str):
    try:
        category = db.session.query(ProductCategories).filter(
            ProductCategories.product_category_name == category
        ).first()
        if not category:
            raise HTTPException(status_code=404, detail=f'Category {category} not found')
        products = db.session.query(Products).filter(Products.id == category.id).all()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=logger.error(e))
