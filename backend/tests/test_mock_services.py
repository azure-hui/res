from app.repositories.store_repository import StoreRepository
from app.services.auth_service import AuthService
from app.services.dashboard_service import get_dashboard_overview
from app.services.store_service import list_stores


store_repo = StoreRepository()


def test_authenticate_user_success(db_session):
    auth_service = AuthService(db_session)
    user = auth_service.authenticate_user("owner_admin", "owner123")
    assert user is not None
    assert user.role == "owner"


def test_authenticate_user_fail(db_session):
    auth_service = AuthService(db_session)
    user = auth_service.authenticate_user("owner_admin", "wrong-password")
    assert user is None


def test_store_access_scope(db_session):
    auth_service = AuthService(db_session)
    user = auth_service.get_user_by_username("manager_beijing")
    assert user is not None

    current_user = {
        "id": user.id,
        "username": user.username,
        "role": user.role,
    }
    data = list_stores(db_session, current_user=current_user, page=1, page_size=20)
    assert data["total"] == 1
    assert len(data["items"]) == 1
    assert data["items"][0]["id"] == 1001


def test_get_store_by_id(db_session):
    store = store_repo.get_store_by_id(db_session, 1002)
    assert store is not None
    assert store.id == 1002


def test_get_dashboard_overview(db_session):
    store = store_repo.get_store_by_id(db_session, 1001)
    assert store is not None

    overview = get_dashboard_overview(db_session, store)
    assert overview is not None
    assert overview["store_id"] == 1001
    assert "revenue_today" in overview
