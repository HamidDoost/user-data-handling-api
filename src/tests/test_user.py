import asyncio
import pytest

from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_get_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/users/")
        assert response.status_code == 200
        # Todo: fix this when correct mocking with FastAPI
        # assert response.json() == []


@pytest.mark.asyncio
async def test_add_user():
    data = {
        "first_name": "string",
        "last_name": "string",
        "email": "string",
        "phone": "string",
        "age": 0,
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/", json=data)
        assert response.status_code == 201
        assert response.json() == {**data, "id": response.json()["id"]}
