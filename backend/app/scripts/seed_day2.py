from __future__ import annotations

from datetime import date

from sqlalchemy import select

from app.core.security import hash_password
from app.db.session import SessionLocal
from app.models.dashboard_snapshot import DashboardSnapshot
from app.models.store import Store
from app.models.user import User
from app.models.user_store_rel import UserStoreRel


def upsert_user(db, username: str, password: str, display_name: str, role: str) -> User:
    user = db.execute(select(User).where(User.username == username)).scalar_one_or_none()
    if user is None:
        user = User(
            username=username,
            password_hash=hash_password(password),
            display_name=display_name,
            role=role,
            is_active=True,
        )
        db.add(user)
        db.flush()
        return user

    user.password_hash = hash_password(password)
    user.display_name = display_name
    user.role = role
    user.is_active = True
    db.flush()
    return user


def upsert_store(db, store_id: int, name: str, city: str) -> Store:
    store = db.get(Store, store_id)
    if store is None:
        store = Store(
            id=store_id,
            name=name,
            city=city,
            is_active=True,
        )
        db.add(store)
        db.flush()
        return store

    store.name = name
    store.city = city
    store.is_active = True
    db.flush()
    return store


def upsert_user_store_rel(db, user_id: int, store_id: int, store_role: str) -> None:
    rel = db.execute(
        select(UserStoreRel).where(
            UserStoreRel.user_id == user_id,
            UserStoreRel.store_id == store_id,
        )
    ).scalar_one_or_none()
    if rel is None:
        db.add(
            UserStoreRel(
                user_id=user_id,
                store_id=store_id,
                store_role=store_role,
            )
        )
        db.flush()
        return

    rel.store_role = store_role
    db.flush()


def upsert_snapshot(
    db,
    store_id: int,
    biz_date: date,
    revenue: float,
    order_count: int,
    customer_count: int,
) -> None:
    snapshot = db.execute(
        select(DashboardSnapshot).where(
            DashboardSnapshot.store_id == store_id,
            DashboardSnapshot.biz_date == biz_date,
        )
    ).scalar_one_or_none()

    if snapshot is None:
        db.add(
            DashboardSnapshot(
                store_id=store_id,
                biz_date=biz_date,
                revenue=revenue,
                order_count=order_count,
                customer_count=customer_count,
            )
        )
        db.flush()
        return

    snapshot.revenue = revenue
    snapshot.order_count = order_count
    snapshot.customer_count = customer_count
    db.flush()


def main() -> None:
    db = SessionLocal()
    try:
        owner = upsert_user(
            db,
            username="owner_admin",
            password="owner123",
            display_name="Owner Admin",
            role="owner",
        )
        manager = upsert_user(
            db,
            username="manager_beijing",
            password="manager123",
            display_name="Beijing Manager",
            role="manager",
        )

        store_1001 = upsert_store(db, 1001, "Beijing Guomao Store", "Beijing")
        store_1002 = upsert_store(db, 1002, "Shanghai Lujiazui Store", "Shanghai")

        upsert_user_store_rel(db, owner.id, store_1001.id, "owner")
        upsert_user_store_rel(db, owner.id, store_1002.id, "owner")
        upsert_user_store_rel(db, manager.id, store_1001.id, "manager")

        upsert_snapshot(
            db,
            store_id=store_1001.id,
            biz_date=date.today(),
            revenue=12888.50,
            order_count=156,
            customer_count=203,
        )

        db.commit()
        print("seed day2 success")
        print("owner_admin / owner123")
        print("manager_beijing / manager123")
        print("stores: 1001, 1002")
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
