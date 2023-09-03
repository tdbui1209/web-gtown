from fastapi import APIRouter


router = APIRouter()


@router.get('/')
def check():
    return {'message': 'Health check successful'}