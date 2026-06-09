def test_stores_requires_token(client):
    resp = client.get("/api/v1/stores")
    assert resp.status_code == 401
    assert str(resp.json()["code"]) == "40101"


def test_stores_rejects_invalid_token(client):
    resp = client.get(
        "/api/v1/stores",
        headers={"Authorization": "Bearer invalid.token.value"},
    )
    assert resp.status_code == 401
    assert str(resp.json()["code"]) == "40102"


def test_stores_rejects_expired_token(client, expired_access_token):
    resp = client.get(
        "/api/v1/stores",
        headers={"Authorization": f"Bearer {expired_access_token}"},
    )
    assert resp.status_code == 401
    assert str(resp.json()["code"]) == "40103"
