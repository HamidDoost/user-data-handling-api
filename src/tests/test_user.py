import asyncio

import pytest
from httpx import AsyncClient

from tests.conftest import app


@pytest.mark.asyncio
async def test_get_users(test_app_with_db):
    test_data = []
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/users/")
        assert response.status_code == 200
        assert response.json() == test_data


@pytest.mark.asyncio
async def test_add_user(test_app_with_db):
    test_data = {
        "first_name": "string",
        "last_name": "string",
        "email": "string",
        "phone": "string",
        "age": 0,
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/", json=test_data)
        assert response.status_code == 201
        assert response.json() == {**test_data, "id": response.json()["id"]}
