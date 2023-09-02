from fastapi import APIRouter

from . import api_product_category, api_product


router = APIRouter()

router.include_router(
    api_product_category.router,
    prefix="/product_categories",
    tags=["product_categories"]
)

router.include_router(
    api_product.router,
    prefix="/products",
    tags=["products"]
)
