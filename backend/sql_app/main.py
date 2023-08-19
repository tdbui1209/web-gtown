from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

from database.connection import Base, engine

from routes.categories import category_router


app = FastAPI()

# Register routes
app.include_router(category_router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.1.11", port=5000, reload=True)
