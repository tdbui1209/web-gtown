from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.connection import get_session
from models.models import Status
from schemas import statuses


status_router = APIRouter(
    prefix="/status",
    tags=["status"],
)


@status_router.get("/", response_model=list[statuses.StatusInDBBase])
async def read_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    return db.query(Status).offset(skip).limit(limit).all()
