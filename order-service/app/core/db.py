from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from app.core.settings import settings
from sqlalchemy.orm import DeclarativeBase

db_engine = create_async_engine(settings.DATABASE_URL)

db_session = async_sessionmaker(db_engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with db_session() as db:
        yield db