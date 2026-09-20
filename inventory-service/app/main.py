from fastapi import FastAPI
from app.core.db import db_engine, get_db, Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_engine.begin() as conn:
        conn.run_sync(Base.metadata.create_all)
    yield
    db_engine.dispose()

app = FastAPI()

@app.get("/")
def default():
    return {"message": "connected to inventory service"}