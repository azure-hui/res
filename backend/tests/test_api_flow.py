def login_and_get_token(client, username: str, password: str) -> str:
    response = client.post(
        "/api/v1/auth/login",
        json={"username": username, "password": password},
    )
    assert response.status_code == 200
    body = response.json()
    assert str(body["code"]) == "0"
    return body["data"]["access_token"]


def test_login_success(client):
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "owner_admin", "password": "owner123"},
    )
    assert response.status_code == 200
    body = response.json()
    assert str(body["code"]) == "0"
    assert "access_token" in body["data"]


def test_me_success(client):
    token = login_and_get_token(client, "owner_admin", "owner123")
    response = client.get(
        "/api/v1/debug/whoami",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["data"]["username"] == "owner_admin"


def test_stores_scope(client):
    token = login_and_get_token(client, "manager_beijing", "manager123")
    response = client.get(
        "/api/v1/stores",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["data"]["total"] == 1
    assert body["data"]["items"][0]["id"] == 1001


def test_dashboard_forbidden(client):
    token = login_and_get_token(client, "manager_beijing", "manager123")
    response = client.get(
        "/api/v1/stores/1002/dashboard/overview",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403
    body = response.json()
    assert str(body["code"]) == "40301"
