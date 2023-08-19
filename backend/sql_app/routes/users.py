from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.connection import get_session
from models.models import Users
from schemas import users


user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@user_router.get("/")
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return db.query(Users).offset(skip).limit(limit).all()
