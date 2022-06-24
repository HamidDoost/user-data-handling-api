import os

from sqlmodel import SQLModel

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.environ.get("DATABASE_URL")


engine = create_async_engine(  # Initializing a new async SQLAlchemy engine
    DATABASE_URL, echo=True, future=True  # enabling to see SQL queries in terminal
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_async_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
