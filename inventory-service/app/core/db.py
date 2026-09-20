from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.settings import settings


db_engine = create_async_engine(settings.DB_URL)

db_session = async_sessionmaker(db_engine)

async def get_db():
    async with db_session() as db:
        yield

class Base(DeclarativeBase):
    pass