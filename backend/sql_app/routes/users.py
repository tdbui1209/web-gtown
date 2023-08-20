from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database.connection import get_session
from models.models import Users, Status
from schemas import users


user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@user_router.get("/", response_model=list[users.UserBase])
async def read_users(skip: int = 0, limit: int = 100,
                     db: Session = Depends(get_session)):
    return db.query(Users).offset(skip).limit(limit).all()


@user_router.post("/", response_model=users.UserInDBBase)
async def create_user(user: users.UserCreate,
                      db: Session = Depends(get_session)):
    active_status_id = db.query(Status).filter(
        Status.name == "active").one().id
    db_user = Users(username=user.username, name=user.name,
                    email=user.email, password=user.password,
                    status_id=active_status_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@user_router.put("/")
async def update_status_of_user(user: users.UserUpdate,
                                db: Session = Depends(get_session)):
    db_user = db.query(Users).filter(Users.username == user.username).one()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    db_user.status_id = user.status_id
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK,
                    content={"message": "User status updated successfully"})


@user_router.post("/login")
async def login_user(user: users.UserLogin,
                     db: Session = Depends(get_session)):
    db_user = db.query(Users).filter(Users.username == user.username).one()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    if db_user.password != user.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect password")
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Login successful"})
