import pytest
import uuid


@pytest.mark.asyncio
async def test_full_auth_flow(client):
    # 🔹 unique email biar tidak bentrok
    email = f"test_{uuid.uuid4()}@example.com"
    password = "password123"

    # 1️⃣ Register
    register_response = await client.post(
        "/auth/register",
        json={
            "email": email,
            "password": password
        }
    )
    assert register_response.status_code in [200, 201]

    # 2️⃣ Login
    login_response = await client.post(
        "/auth/jwt/login",
        data={
            "username": email,
            "password": password
        }
    )

    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    # 3️⃣ Access protected endpoint
    headers = {
        "Authorization": f"Bearer {token}"
    }

    feed_response = await client.get("/feed", headers=headers)

    assert feed_response.status_code == 200
    assert "posts" in feed_response.json()


@pytest.mark.asyncio
async def test_feed_requires_auth(client):
    response = await client.get("/feed")
    assert response.status_code == 401