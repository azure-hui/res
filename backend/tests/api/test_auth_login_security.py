from sqlalchemy import select

from app.models.user import User


def _reset_owner_login_state(db_session) -> User:
    owner = db_session.execute(
        select(User).where(User.username == "owner_admin")
    ).scalar_one()
    owner.failed_login_attempts = 0
    owner.locked_until = None
    db_session.add(owner)
    db_session.commit()
    return owner


def test_login_rejects_unknown_username(client):
    resp = client.post(
        "/api/v1/auth/login",
        json={"username": "not_exists_user", "password": "wrongpass123"},
    )
    assert resp.status_code == 401
    assert str(resp.json()["code"]) == "40110"


def test_login_rejects_wrong_password(client, db_session):
    owner = _reset_owner_login_state(db_session)
    resp = client.post(
        "/api/v1/auth/login",
        json={"username": owner.username, "password": "wrongpass123"},
    )
    assert resp.status_code == 401
    assert str(resp.json()["code"]) == "40110"


def test_login_locks_after_max_failures(client, db_session):
    owner = _reset_owner_login_state(db_session)

    last_resp = None
    for _ in range(5):
        last_resp = client.post(
            "/api/v1/auth/login",
            json={"username": owner.username, "password": "wrongpass123"},
        )

    assert last_resp is not None
    assert last_resp.status_code == 401
    assert str(last_resp.json()["code"]) == "40111"

    locked_resp = client.post(
        "/api/v1/auth/login",
        json={"username": owner.username, "password": "owner123"},
    )
    assert locked_resp.status_code == 401
    assert str(locked_resp.json()["code"]) == "40111"
