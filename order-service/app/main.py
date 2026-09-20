from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.db import db_engine, get_db, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await db_engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "Welcome to the Order Service"}