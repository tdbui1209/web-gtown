from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import categories
from database.connection import get_session
from models.models import Categories


category_router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@category_router.get("/", response_model=list[categories.Category])
async def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return db.query(Categories).offset(skip).limit(limit).all()
