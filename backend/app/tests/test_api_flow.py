def test_login_success(client):
    resp = client.post(
        "/api/v1/auth/login",
        json={"username": "owner_admin", "password": "owner123"},
    )
    assert resp.status_code == 200

    body = resp.json()
    assert body["code"] == 0
    assert "access_token" in body["data"]
    assert body["data"]["user"]["username"] == "owner_admin"


def test_login_wrong_password_should_40101(client):
    resp = client.post(
        "/api/v1/auth/login",
        json={"username": "owner_admin", "password": "wrong-password"},
    )
    assert resp.status_code == 401

    body = resp.json()
    assert body["code"] == 40101


def test_owner_flow_login_me_stores_dashboard(client):
    resp = client.post(
        "/api/v1/auth/login",
        json={"username": "owner_admin", "password": "owner123"},
    )
    assert resp.status_code == 200
    token = resp.json()["data"]["access_token"]

    me_resp = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert me_resp.status_code == 200
    assert me_resp.json()["data"]["username"] == "owner_admin"

    stores_resp = client.get(
        "/api/v1/stores",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert stores_resp.status_code == 200
    store_ids = sorted(item["id"] for item in stores_resp.json()["data"]["items"])
    assert store_ids == [1001, 1002]

    dashboard_resp = client.get(
        "/api/v1/stores/1001/dashboard/overview",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert dashboard_resp.status_code == 200
    dashboard_data = dashboard_resp.json()["data"]
    assert dashboard_data["store_id"] == 1001