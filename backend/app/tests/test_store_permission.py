from fastapi.testclient import TestClient

from app.main import app
from app.services.mock_auth import get_user_by_username, build_access_token_for_user


client = TestClient(app)


def test_store_access_allowed():
    user = get_user_by_username("manager_beijing")
    assert user is not None
    token = build_access_token_for_user(user)

    response = client.get(
        "/api/v1/debug/stores/1001/access",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200


def test_store_access_forbidden():
    user = get_user_by_username("manager_beijing")
    assert user is not None
    token = build_access_token_for_user(user)

    response = client.get(
        "/api/v1/debug/stores/1002/access",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403
    body = response.json()
    assert body["code"] == 40301

def test_owner_can_see_all_stores(client):
    from tests.conftest import login_and_get_token

    token = login_and_get_token(client, "owner_admin", "owner123")
    resp = client.get(
        "/api/v1/stores",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 200

    body = resp.json()
    assert body["code"] == 0

    items = body["data"]["items"]
    store_ids = sorted(item["id"] for item in items)
    assert store_ids == [1001, 1002]


def test_manager_can_only_see_authorized_store(client):
    from tests.conftest import login_and_get_token

    token = login_and_get_token(client, "manager_beijing", "manager123")
    resp = client.get(
        "/api/v1/stores",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 200

    body = resp.json()
    assert body["code"] == 0

    items = body["data"]["items"]
    store_ids = [item["id"] for item in items]
    assert store_ids == [1001]


def test_manager_can_access_store_1001_dashboard(client):
    from tests.conftest import login_and_get_token

    token = login_and_get_token(client, "manager_beijing", "manager123")
    resp = client.get(
        "/api/v1/stores/1001/dashboard/overview",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 200

    body = resp.json()
    assert body["code"] == 0
    assert body["data"]["store_id"] == 1001


def test_manager_cannot_access_store_1002_dashboard(client):
    from tests.conftest import login_and_get_token

    token = login_and_get_token(client, "manager_beijing", "manager123")
    resp = client.get(
        "/api/v1/stores/1002/dashboard/overview",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 403

    body = resp.json()
    assert body["code"] == 40301
