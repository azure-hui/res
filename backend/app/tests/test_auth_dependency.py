from fastapi.testclient import TestClient

from app.main import app
from app.services.mock_auth import get_user_by_username, build_access_token_for_user


client = TestClient(app)


def test_whoami_unauthorized():
    response = client.get("/api/v1/debug/whoami")
    assert response.status_code == 401
    body = response.json()
    assert body["code"] in [40104, 40105, 40103, 40102]


def test_whoami_success():
    user = get_user_by_username("owner_admin")
    assert user is not None
    token = build_access_token_for_user(user)

    response = client.get(
        "/api/v1/debug/whoami",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["data"]["username"] == "owner_admin"


def test_me_without_token_should_401(client):
    resp = client.get("/api/v1/auth/me")
    assert resp.status_code == 401

    body = resp.json()
    assert body["code"] == 40101
    assert "message" in body
    assert "request_id" in body
    assert "timestamp" in body


def test_me_with_invalid_token_should_401(client):
    resp = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": "Bearer invalid-token"},
    )
    assert resp.status_code == 401

    body = resp.json()
    assert body["code"] == 40101


def test_me_with_valid_token_should_success(client):
    from tests.conftest import login_and_get_token

    token = login_and_get_token(client, "owner_admin", "owner123")
    resp = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 200

    body = resp.json()
    assert body["code"] == 0
    assert body["data"]["username"] == "owner_admin"
    assert body["data"]["role"] == "owner"
