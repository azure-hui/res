def test_login_returns_token_pair(client, owner_login_payload):
    resp = client.post("/api/v1/auth/login", json=owner_login_payload)
    assert resp.status_code == 200

    body = resp.json()
    assert str(body["code"]) == "0"
    data = body["data"]
    assert data["token_type"] == "bearer"
    assert data["access_token"]
    assert data["refresh_token"]
    assert data["access_expires_in"] > 0
    assert data["refresh_expires_in"] > 0


def test_refresh_success_and_rotate(client, owner_login_payload):
    login_resp = client.post("/api/v1/auth/login", json=owner_login_payload)
    assert login_resp.status_code == 200
    login_data = login_resp.json()["data"]

    refresh_resp = client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": login_data["refresh_token"]},
    )
    assert refresh_resp.status_code == 200

    new_data = refresh_resp.json()["data"]
    assert new_data["refresh_token"] != login_data["refresh_token"]
    assert new_data["access_token"]
    assert new_data["token_type"] == "bearer"


def test_old_refresh_token_cannot_be_reused(client, owner_login_payload):
    login_resp = client.post("/api/v1/auth/login", json=owner_login_payload)
    assert login_resp.status_code == 200
    old_refresh = login_resp.json()["data"]["refresh_token"]

    first_refresh = client.post("/api/v1/auth/refresh", json={"refresh_token": old_refresh})
    assert first_refresh.status_code == 200

    reuse_resp = client.post("/api/v1/auth/refresh", json={"refresh_token": old_refresh})
    assert reuse_resp.status_code == 401
    assert str(reuse_resp.json()["code"]) == "40102"
