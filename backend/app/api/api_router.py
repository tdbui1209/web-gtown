from fastapi import APIRouter

from . import api_product_category


router = APIRouter()

router.include_router(
    api_product_category.router,
    prefix="/product_category",
    tags=["product_category"]
)