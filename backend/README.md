# Project structure

```
backend
├── app
    ├── api              - Api endpoints.
    ├── core             - Application configuration, startup events, logging.
    ├── db               - SQLAlchemy database configuration.
    ├── models           - SQLAlchemy models for DB tables.
    ├── schemas          - Pydantic schemas for API input and output validation.
    ├── __init__.py
    ├── main.py          - FastAPI application creation and configuration.
    └── requirements.txt - Python dependencies.
├── migrations           - Alembic migrations.
├── .env                 - Environment variables.
├── alembic.ini          - Alembic configuration.
└── logging.ini          - Logging configuration.
```

# Web routes

All routes are available on /docs or /redoc paths with Swagger or ReDoc.
