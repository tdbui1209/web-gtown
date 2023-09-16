from sqlalchemy import Column, String, Boolean, DateTime

from app.models.model_base import Base


class User(Base):
    full_name = Column(String(100))
    email = Column(String(100), nullable=False, unique=True, index=True)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    role = Column(String(50), default='guest')
    last_login = Column(DateTime)
