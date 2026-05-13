from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_and_me():
    login_response = client.post(
        "/api/v1/auth/login",
        json={"username": "owner_admin", "password": "owner123"},
    )
    assert login_response.status_code == 200
    token = login_response.json()["data"]["access_token"]

    me_response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert me_response.status_code == 200
    assert me_response.json()["data"]["username"] == "owner_admin"
