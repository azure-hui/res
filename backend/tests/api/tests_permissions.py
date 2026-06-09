def _login_and_get_access_token(client, payload):
    resp = client.post("/api/v1/auth/login", json=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert str(body["code"]) == "0"
    return body["data"]["access_token"]


def test_owner_can_list_all_stores(client, owner_login_payload):
    owner_token = _login_and_get_access_token(client, owner_login_payload)
    resp = client.get(
        "/api/v1/stores",
        headers={"Authorization": f"Bearer {owner_token}"},
    )
    assert resp.status_code == 200
    data = resp.json()["data"]
    assert data["total"] == 2
    assert len(data["items"]) == 2


def test_manager_only_sees_assigned_store(client, manager_login_payload):
    manager_token = _login_and_get_access_token(client, manager_login_payload)
    resp = client.get(
        "/api/v1/stores",
        headers={"Authorization": f"Bearer {manager_token}"},
    )
    assert resp.status_code == 200
    data = resp.json()["data"]
    assert data["total"] == 1
    assert len(data["items"]) == 1
    assert data["items"][0]["id"] == 1001
