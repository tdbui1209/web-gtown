from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.connection import get_session
from models.models import Status, Users
from schemas import statuses


status_router = APIRouter(
    prefix="/status",
    tags=["status"],
)


@status_router.get("/", response_model=list[statuses.StatusInDBBase])
async def read_statuses(skip: int = 0, limit: int = 100,
                        db: Session = Depends(get_session)):
    return db.query(Status).offset(skip).limit(limit).all()


@status_router.post("/", response_model=statuses.StatusInDBBase,
                    status_code=status.HTTP_201_CREATED)
async def create_status(status: statuses.StatusCreate,
                        db: Session = Depends(get_session)):
    db_status = Status(name=status.name)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


@status_router.get("/{username}/")
async def read_user_status(username: str,
                           db: Session = Depends(get_session)):
    result = db.query(Users, Status).filter(
        Users.username == username).join(Status).one()
    return {
        "username": result.Users.username,
        "status": result.Status.name
    }
