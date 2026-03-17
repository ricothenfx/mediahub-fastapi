import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from app.main import app
from app.db import create_db_and_tables


@pytest.fixture(scope="session", autouse=True)
async def setup_db():
    await create_db_and_tables()


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as ac:
        yield ac