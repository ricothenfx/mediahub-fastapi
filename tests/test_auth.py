import pytest
import uuid


@pytest.mark.asyncio
async def test_register(client):
    email = f"test_{uuid.uuid4()}@example.com"

    response = await client.post(
        "/auth/register",
        json={"email": email, "password": "password123"}
    )

    assert response.status_code in [200, 201]


@pytest.mark.asyncio
async def test_login(client):
    # register first
    await client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )

    # then login
    response = await client.post(
        "/auth/jwt/login",
        data={
            "username": "test@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200