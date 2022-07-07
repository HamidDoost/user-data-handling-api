import asyncio
import os

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from app.config import Settings, get_settings
from app.db import get_async_session
from app.main import create_application

DATABASE_URL = os.environ.get("DATABASE_TEST_URL")

engine_test = create_async_engine(  # Initialise a new async SQLAlchemy engine for tests
    DATABASE_URL, echo=True, future=True  # Enable to see SQL queries in terminal
)

# Initialise test database
async def init_db_test():
    async with engine_test.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


# Set async session for tests
async def get_async_session_override() -> AsyncSession:
    async_session = sessionmaker(
        engine_test, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
        await session.commit()


# Set environment variables for testing and test database
def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


# Prevent pytest to send two tests to different event lops
@pytest.fixture(scope="session")
def event_loop(request):
    # Create an instance of the default event loop for each test case.
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


app = create_application()
app.dependency_overrides[get_settings] = get_settings_override
app.dependency_overrides[get_async_session] = get_async_session_override


@pytest.fixture(scope="session")
async def test_app_with_db():
    await init_db_test()