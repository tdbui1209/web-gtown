import logging

import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware

from api.api_router import router
from models.model_base import Base
from db.base import engine
from core.config import settings


logging.config.fileConfig(settings.LOGGING_CONFIG, disable_existing_loggers=False)
Base.metadata.create_all(engine)


def get_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    application.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)
    application.include_router(router, prefix=settings.API_PREFIX)

    return application


app = get_application()
if __name__ == '__main__':
    uvicorn.run(app, host='192.168.1.11', port=5000)
