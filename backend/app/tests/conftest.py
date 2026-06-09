from __future__ import annotations

import os
from datetime import date

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.base import Base
from app.db.session import get_db
from app.core.security import hash_password
from app.models.user import User
from app.models.store import Store
from app.models.user_store_rel import UserStoreRel
from app.models.dashboard_snapshot import DashboardSnapshot

TEST_DATABASE_URL = "sqlite:///./test_day2.db"

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


def seed_test_data():
    db = TestingSessionLocal()
    try:
        owner = User(
            id=1,
            username="owner_admin",
            password_hash=hash_password("owner123"),
            display_name="Owner Admin",
            role="owner",
            is_active=True,
        )
        manager = User(
            id=2,
            username="manager_beijing",
            password_hash=hash_password("manager123"),
            display_name="Beijing Manager",
            role="manager",
            is_active=True,
        )

        store_1001 = Store(id=1001, name="北京朝阳店", city="北京", is_active=True)
        store_1002 = Store(id=1002, name="上海浦东店", city="上海", is_active=True)

        rel_1 = UserStoreRel(user_id=1, store_id=1001, store_role="owner")
        rel_2 = UserStoreRel(user_id=1, store_id=1002, store_role="owner")
        rel_3 = UserStoreRel(user_id=2, store_id=1001, store_role="manager")

        snapshot = DashboardSnapshot(
            store_id=1001,
            biz_date=date.today(),
            revenue=12888.50,
            order_count=156,
            customer_count=203,
        )

        db.add_all([owner, manager, store_1001, store_1002, rel_1, rel_2, rel_3, snapshot])
        db.commit()
    finally:
        db.close()


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    if os.path.exists("./test_day2.db"):
        os.remove("./test_day2.db")

    Base.metadata.create_all(bind=engine)
    seed_test_data()

    app.dependency_overrides[get_db] = override_get_db
    yield

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)

    if os.path.exists("./test_day2.db"):
        os.remove("./test_day2.db")


@pytest.fixture
def client():
    return TestClient(app)


def login_and_get_token(client: TestClient, username: str, password: str) -> str:
    resp = client.post(
        "/api/v1/auth/login",
        json={"username": username, "password": password},
    )
    assert resp.status_code == 200
    body = resp.json()
    return body["data"]["access_token"]