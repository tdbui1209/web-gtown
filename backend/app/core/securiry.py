import jwt
from core.config import settings
from datetime import datetime, timedelta
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def create_access_token(user_id: int) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=settings.ACCESS_TOKEN_EXPIRE_SECONDS
    )
    to_encode = {'exp': expire, 'user_id': user_id}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRECT_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)  


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
