from fastapi import APIRouter

from app.api import api_healthcheck, api_product_category, api_product


router = APIRouter()

router.include_router(api_healthcheck.router, prefix="/healthcheck", tags=["health-check"])
router.include_router(api_product_category.router, prefix="/product_categories", tags=["product-categories"])
router.include_router(api_product.router, prefix="/products", tags=["products"])
