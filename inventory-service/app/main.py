from fastapi import FastAPI
from app.core.db import db_engine, get_db, Base
from contextlib import asynccontextmanager
from app.routes.product import router as product_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await db_engine.dispose()

app = FastAPI(lifespan=lifespan)

app.include_router(product_router, prefix="/products", tags=["product"])

@app.get("/")
def default():
    return {"message": "connected to inventory service"}