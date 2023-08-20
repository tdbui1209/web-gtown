from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import categories
from database.connection import get_session
from models.models import Categories


category_router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@category_router.get("/", response_model=list[categories.CategoryInDBBase])
async def read_categories(skip: int = 0, limit: int = 100,
                          db: Session = Depends(get_session)):
    return db.query(Categories).offset(skip).limit(limit).all()


@category_router.post("/", response_model=categories.CategoryInDBBase,
                      status_code=status.HTTP_201_CREATED)
async def create_category(category: categories.CategoryCreate,
                          db: Session = Depends(get_session)):
    db_category = Categories(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
