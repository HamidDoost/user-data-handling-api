import os
import pytest
from httpx import AsyncClient

from app.main import app
from app.config import get_settings
from tests.conftest import get_settings_override


@pytest.mark.asyncio
async def test_health():
    app.dependency_overrides[get_settings] = get_settings_override
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/ping")
        assert response.status_code == 200
        assert response.json() == {
            "ping": "pong!",
            "environment": "dev",
            "testig": True,
        }
