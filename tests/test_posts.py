import pytest

@pytest.mark.asyncio
async def test_get_feed(client):
    response = await client.get("/feed")
    # bisa 401 kalau belum login → itu OK
    assert response.status_code in [200, 401]