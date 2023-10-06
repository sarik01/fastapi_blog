import pytest
from sqlalchemy import insert, select

from src.auth.models import role
from tests.conftest import client, async_session_maker


async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(role).values(id=1, name="admin", permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, 'admin', None)], "Роль не добавилась"
def test_register():
    response = client.post("/auth/register", json={
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
        "role_id": 1
    })

    assert response.status_code == 201


from httpx import AsyncClient


async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post("/posts", json={
      "title": "2",
      "text": "2",
      "instrument_type": "2",
      "type": "2"
    })
    assert response.status_code == 200

async def test_get_specific_operations(ac: AsyncClient):
    response = await ac.get("/posts/1")

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1