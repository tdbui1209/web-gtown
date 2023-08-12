from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
