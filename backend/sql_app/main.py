from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/categories/", response_model=list[schemas.Category])
async def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories


@app.post("/categories/", response_model=schemas.Category)
async def create_category(category: schemas.CategoryBase, db: Session = Depends(get_db)):
    db_category = crud.create_category(db, category=category)
    if db_category is None:
        raise HTTPException(status_code=400, detail="Category already exists")
    return db_category


@app.get("/products/", response_model=list[schemas.Product])
async def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.post("/products/", response_model=schemas.Product)
async def create_products(product: schemas.ProductBase, db: Session = Depends(get_db)):
    db_product = crud.create_products(db, product=product)
    if db_product is None:
        raise HTTPException(status_code=400, detail="Product already exists")
    return db_product


@app.get("users/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
