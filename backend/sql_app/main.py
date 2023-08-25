from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

from database.connection import Base, engine

from routes.categories import category_router
from routes.statuses import status_router
from routes.users import user_router
from routes.products import product_router


app = FastAPI()

# Register routes
app.include_router(category_router)
app.include_router(status_router)
app.include_router(user_router)
app.include_router(product_router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.1.11", port=5000, reload=True)
