from __future__ import annotations

from datetime import datetime, timezone
import os
from pathlib import Path
import time

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

os.environ.setdefault("DATABASE_URL", "sqlite:///./test_bootstrap.db")

from app.core.config import settings
from app.core.security import create_access_token, hash_password
from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.models.dashboard_snapshot import DashboardSnapshot
from app.models.store import Store
from app.models.user import User
from app.models.user_store_rel import UserStoreRel

TEST_DB_PATH = Path(__file__).parent / "test_backend.db"
TEST_DATABASE_URL = f"sqlite:///{TEST_DB_PATH.as_posix()}"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    future=True,
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True,
)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def seed_test_data() -> None:
    db = TestingSessionLocal()
    try:
        owner = User(
            id=1,
            username="owner_admin",
            password_hash=hash_password("owner123"),
            display_name="Owner Admin",
            role="owner",
            is_active=True,
            failed_login_attempts=0,
            locked_until=None,
        )
        manager = User(
            id=2,
            username="manager_beijing",
            password_hash=hash_password("manager123"),
            display_name="Beijing Manager",
            role="manager",
            is_active=True,
            failed_login_attempts=0,
            locked_until=None,
        )

        store_1001 = Store(id=1001, name="Store 1001", city="Beijing", is_active=True)
        store_1002 = Store(id=1002, name="Store 1002", city="Shanghai", is_active=True)

        relations = [
            UserStoreRel(user_id=1, store_id=1001, store_role="owner"),
            UserStoreRel(user_id=1, store_id=1002, store_role="owner"),
            UserStoreRel(user_id=2, store_id=1001, store_role="manager"),
        ]

        snapshot = DashboardSnapshot(
            store_id=1001,
            biz_date=datetime.now(timezone.utc).date(),
            revenue=12888.50,
            order_count=156,
            customer_count=203,
        )

        db.add_all([owner, manager, store_1001, store_1002, *relations, snapshot])
        db.commit()
    finally:
        db.close()


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    if TEST_DB_PATH.exists():
        TEST_DB_PATH.unlink()

    Base.metadata.create_all(bind=engine)
    seed_test_data()
    app.dependency_overrides[get_db] = override_get_db

    yield

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
    if TEST_DB_PATH.exists():
        # On Windows, sqlite file removal can fail briefly if a handle is still closing.
        for _ in range(5):
            try:
                TEST_DB_PATH.unlink()
                break
            except PermissionError:
                time.sleep(0.2)


@pytest.fixture
def db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def reset_login_state(db_session):
    users = db_session.execute(select(User)).scalars().all()
    for user in users:
        user.failed_login_attempts = 0
        user.locked_until = None
    db_session.commit()


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture
def owner_user(db_session):
    stmt = select(User).where(User.username == "owner_admin")
    return db_session.execute(stmt).scalar_one()


@pytest.fixture
def owner_login_payload():
    return {"username": "owner_admin", "password": "owner123"}


@pytest.fixture
def manager_login_payload():
    return {"username": "manager_beijing", "password": "manager123"}


def login_and_get_token(client: TestClient, username: str, password: str) -> str:
    resp = client.post(
        "/api/v1/auth/login",
        json={"username": username, "password": password},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert str(body["code"]) == "0"
    return body["data"]["access_token"]


@pytest.fixture
def expired_access_token(owner_user):
    original_minutes = settings.jwt_access_token_expire_minutes
    settings.jwt_access_token_expire_minutes = -1
    try:
        token, _ = create_access_token(owner_user.id, owner_user.role)
        return token
    finally:
        settings.jwt_access_token_expire_minutes = original_minutes
