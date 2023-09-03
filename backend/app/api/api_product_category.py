import logging
from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.schemas.sche_product_category import ProductCategoryCreate, ProductCategoryItem
from app.models.model_product_category import ProductCategories


logger = logging.getLogger()
router = APIRouter()


@router.get('/', response_model=list[ProductCategoryItem])
def read_product_categories():
    try:
        product_categories = db.session.query(ProductCategories).all()
        return product_categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=logger.error(e))
    

@router.post('/', response_model=ProductCategoryCreate)
def create_product_category(product_category: ProductCategoryCreate):
    try:
        db_category = ProductCategories(
            product_category_name=product_category.product_category_name
        )
        db.session.add(db_category)
        db.session.commit()
        return product_category
    except Exception as e:
        raise HTTPException(status_code=500, detail=logger.error(e))
