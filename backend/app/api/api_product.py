import logging
from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from app.schemas.sche_product import ProductCreate, ProductItem, ProductCategoryCreate, ProductCategoryItem
from app.models.model_product import Products, ProductCategories


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
    if len(product.product_name) == 0:
        raise HTTPException(status_code=400, detail='Product name cannot be empty')
    if product.product_price <= 0:
        raise HTTPException(status_code=400, detail='Product price must be greater than 0')
    if db.session.query(ProductCategories).filter(
        ProductCategories.id == product.product_category_id
    ).first() is None:
        raise HTTPException(status_code=400, detail=f'Product category {product.product_category_id} does not exist')
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


@router.get('/categories', response_model=list[ProductCategoryItem])
def read_product_categories():
    try:
        product_categories = db.session.query(ProductCategories).all()
        return product_categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=logger.error(e))
    

@router.post('/categories', response_model=ProductCategoryCreate)
def create_product_category(product_category: ProductCategoryCreate):
    if len(product_category.product_category_name) == 0:
        raise HTTPException(status_code=400, detail='Product category name cannot be empty')
    if db.session.query(ProductCategories).filter(
        ProductCategories.product_category_name == product_category.product_category_name
    ).first():
        raise HTTPException(status_code=400, detail=f'Product category {product_category.product_category_name} already exists')
    try:
        db_category = ProductCategories(
            product_category_name=product_category.product_category_name
        )
        db.session.add(db_category)
        db.session.commit()
        return product_category
    except Exception as e:
        raise HTTPException(status_code=500, detail=logger.error(e))
