from sqlalchemy.orm import Session

from . import models, schemas


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Categories).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.CategoryBase):
    db_category = models.Categories(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Products).offset(skip).limit(limit).all()


def create_products(db: Session, product: schemas.ProductBase):
    db_product = models.Products(
        name=product.name,
        price=product.price,
        description=product.description,
        category_id=product.category_id,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
