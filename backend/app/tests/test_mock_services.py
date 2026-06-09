from app.services.mock_auth import (
    authenticate_user,
    get_user_by_username,
    user_can_access_store,
)
from app.services.mock_data import MOCK_DASHBOARD_OVERVIEW, MOCK_STORES


def test_authenticate_user_success():
    user = authenticate_user("owner_admin", "owner123")
    assert user is not None
    assert user["role"] == "owner"


def test_authenticate_user_fail():
    user = authenticate_user("owner_admin", "wrong-password")
    assert user is None


def test_store_access_scope():
    user = get_user_by_username("manager_beijing")
    assert user is not None
    stores = [store for store in MOCK_STORES if user_can_access_store(user, store["id"])]
    assert len(stores) == 1
    assert stores[0]["id"] == 1001


def test_get_store_by_id():
    store = next((s for s in MOCK_STORES if s["id"] == 1002), None)
    assert store is not None
    assert store["name"] == "\u4e0a\u6d77\u9646\u5bb6\u5634\u5e97"


def test_get_dashboard_overview():
    overview = MOCK_DASHBOARD_OVERVIEW.get(1001)
    assert overview is not None
    assert overview["store_id"] == 1001
    assert "revenue_today" in overview
