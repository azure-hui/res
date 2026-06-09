from datetime import datetime, timedelta, timezone

from jose import jwt

from app.core.config import settings

def test_validation_error_structure(client):
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "owner_admin"},
    )
    assert response.status_code == 422
    body = response.json()
    assert str(body["code"]) == "40022"
    assert "request_id" in body
    assert "timestamp" in body


def test_missing_auth_header(client):
    response = client.get("/api/v1/debug/whoami")
    assert response.status_code == 401
    body = response.json()
    assert str(body["code"]) == "40101"
    assert "request_id" in body
    assert "timestamp" in body


def test_expired_token(client):
    payload = {
        "sub": "1",
        "role": "owner",
        "type": "access",
        "exp": datetime.now(timezone.utc) - timedelta(minutes=10),
    }
    token = jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )

    response = client.get(
        "/api/v1/debug/whoami",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 401
    body = response.json()
    assert str(body["code"]) == "40103"


def test_not_found_structure(client):
    response = client.get("/api/v1/not-exist")
    assert response.status_code == 404
    body = response.json()
    assert "code" in body
    assert "message" in body
    assert "request_id" in body
    assert "timestamp" in body
