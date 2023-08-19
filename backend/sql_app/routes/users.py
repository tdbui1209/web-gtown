from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.connection import get_session
from models.models import Users, Status
from schemas import users


user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@user_router.get("/", response_model=list[users.UserBase])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return db.query(Users).offset(skip).limit(limit).all()


@user_router.post("/", response_model=users.UserInDBBase)
async def create_user(user: users.UserCreate, db: Session = Depends(get_session)):
    active_status_id = db.query(Status).filter(Status.name == "active").one().id
    db_user = Users(username=user.username, name=user.name, email=user.email,
                    password=user.password, status_id=active_status_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
