def _login_and_get_token(client, username: str, password: str) -> str:
    resp = client.post(
        "/api/v1/auth/login",
        json={"username": username, "password": password},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert str(body["code"]) == "0"
    return body["data"]["access_token"]


def test_store_access_allowed(client):
    token = _login_and_get_token(client, "manager_beijing", "manager123")
    response = client.get(
        "/api/v1/debug/stores/1001/access",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200


def test_store_access_forbidden(client):
    token = _login_and_get_token(client, "manager_beijing", "manager123")
    response = client.get(
        "/api/v1/debug/stores/1002/access",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403
    body = response.json()
    assert str(body["code"]) == "40301"


def test_dashboard_overview_allows_store_owner(client):
    token = _login_and_get_token(client, "owner_admin", "owner123")
    resp = client.get(
        "/api/v1/stores/1001/dashboard/overview",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 200


def test_dashboard_overview_rejects_user_without_store_access(client):
    token = _login_and_get_token(client, "manager_beijing", "manager123")
    resp = client.get(
        "/api/v1/stores/1002/dashboard/overview",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 403
    assert str(resp.json()["code"]) == "40301"
