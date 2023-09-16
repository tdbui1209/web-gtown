from datetime import datetime
from passlib.context import CryptContext
from starlette.requests import Request

from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from app.schemas.sche_user import UserRegisterRequest, UserItemResponse, UserLoginRequest
from app.models.model_user import User


router = APIRouter()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@router.get('', response_model=list[UserItemResponse])
def read_users():
    try:
        users = db.session.query(User).all()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/signup')
def signup(register: UserRegisterRequest):
    if len(register.full_name) == 0:
        raise HTTPException(status_code=400, detail='Full name cannot be empty')
    if len(register.password) == 0:
        raise HTTPException(status_code=400, detail='Password cannot be empty')
    try:
        user = User(
            full_name=register.full_name,
            email=register.email,
            hashed_password=pwd_context.hash(register.password),
        )
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/login')
def login(userlogin: UserLoginRequest, request: Request):
    if len(userlogin.password) == 0:
        raise HTTPException(status_code=400, detail='Password cannot be empty')
    try:
        user = db.session.query(User).filter(User.email == userlogin.email).first()
        if not user:
            raise HTTPException(status_code=404, detail='User not found')
        if not pwd_context.verify(userlogin.password, user.hashed_password):
            raise HTTPException(status_code=403, detail='Incorrect password')
        if not user.is_active:
            raise HTTPException(status_code=403, detail='User is not active')
        user.last_login = datetime.now()
        db.session.commit()
        request.session['user'] = user.email
        return {'message': 'Login success'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/logout')
def logout(request: Request):
    if 'user' in request.session:
        del request.session['user']
        return {'message': 'Logout success'}
    else:
        return {'message': 'User not logged in'}
