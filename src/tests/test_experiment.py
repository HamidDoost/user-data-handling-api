import asyncio

import pytest
from httpx import AsyncClient

from tests.conftest import app


@pytest.mark.asyncio
async def test_get_experiments(test_app_with_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/experiments/")
        assert response.status_code == 200
        assert response.json() == []


@pytest.mark.asyncio
async def test_add_experiment():
    data = {
        "experiment_name": "string",
        "experiment_description": "string",
        "user_id": None,
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/experiments/", json=data)
        assert response.status_code == 201
        assert response.json() == {**data, "id": response.json()["id"]}
