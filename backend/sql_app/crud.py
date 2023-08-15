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


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserBase):
    db_user = models.Users(
        name=user.name,
        email=user.email,
        password=user.password,
        status_id=1  # default status_id = 1
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_role(db: Session, role: schemas.RoleBase):
    db_role = models.Roles(
        name=role.name,
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def get_status(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Status).offset(skip).limit(limit).all()


def get_status_by_user(db: Session, username: str):
    return db.query(models.Status).filter(models.Status.id == username).first()


def create_status(db: Session, status: schemas.StatusBase):
    db_status = models.Status(
        name=status.name,
    )
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status
