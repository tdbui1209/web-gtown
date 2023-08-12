from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/categories/", response_model=list[schemas.Category])
async def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(SessionLocal)):
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories
