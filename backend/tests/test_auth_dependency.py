from app.services.mock_auth import get_user_by_username, build_access_token_for_user


def test_whoami_unauthorized(client):
    response = client.get("/api/v1/debug/whoami")
    assert response.status_code == 401
    body = response.json()
    assert str(body["code"]) == "40101"


def test_whoami_success(client):
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
