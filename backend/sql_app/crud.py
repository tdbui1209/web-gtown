from sqlalchemy.orm import Session

from . import models, schemas


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()
