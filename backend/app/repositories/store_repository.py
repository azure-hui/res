from __future__ import annotations

from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.store import Store
from app.models.user_store_rel import UserStoreRel


class StoreRepository:
    SORT_FIELD_MAP = {
        "id": Store.id,
        "name": Store.name,
        "city": Store.city,
    }

    def _base_stmt_for_scope(self, *, user_id: int, role: str):
        if role == "owner":
            return select(Store)

        return (
            select(Store)
            .join(UserStoreRel, UserStoreRel.store_id == Store.id)
            .where(UserStoreRel.user_id == user_id)
        )

    def _apply_filters(
        self,
        stmt,
        *,
        keyword: Optional[str] = None,
        city: Optional[str] = None,
        is_active: Optional[bool] = None,
    ):
        if keyword:
            stmt = stmt.where(Store.name.ilike(f"%{keyword.strip()}%"))
        if city:
            stmt = stmt.where(Store.city == city)
        if is_active is not None:
            stmt = stmt.where(Store.is_active == is_active)
        return stmt

    def _apply_sort(self, stmt, *, sort_by: str, sort_order: str):
        sort_col = self.SORT_FIELD_MAP.get(sort_by, Store.id)
        if sort_order.lower() == "desc":
            return stmt.order_by(sort_col.desc())
        return stmt.order_by(sort_col.asc())

    def list_stores(
        self,
        db: Session,
        *,
        user_id: int,
        role: str,
        keyword: Optional[str] = None,
        city: Optional[str] = None,
        is_active: Optional[bool] = None,
        sort_by: str = "id",
        sort_order: str = "asc",
        offset: int = 0,
        limit: int = 20,
    ) -> list[Store]:
        stmt = self._base_stmt_for_scope(user_id=user_id, role=role)
        stmt = self._apply_filters(stmt, keyword=keyword, city=city, is_active=is_active)
        stmt = self._apply_sort(stmt, sort_by=sort_by, sort_order=sort_order)
        stmt = stmt.offset(offset).limit(limit)
        return list(db.execute(stmt).scalars().all())

    def count_stores(
        self,
        db: Session,
        *,
        user_id: int,
        role: str,
        keyword: Optional[str] = None,
        city: Optional[str] = None,
        is_active: Optional[bool] = None,
    ) -> int:
        stmt = self._base_stmt_for_scope(user_id=user_id, role=role)
        stmt = self._apply_filters(stmt, keyword=keyword, city=city, is_active=is_active)
        count_stmt = select(func.count()).select_from(stmt.subquery())
        return int(db.execute(count_stmt).scalar_one())

    def get_store_by_id(self, db: Session, store_id: int) -> Optional[Store]:
        return db.get(Store, store_id)
    
    def get_store_by_id_in_scope(
        self,
        db: Session,
        *,
        store_id: int,
        user_id: int,
        role: str,
    ) -> Optional[Store]:
        if role == "owner":
            stmt = select(Store).where(Store.id == store_id)
            return db.execute(stmt).scalar_one_or_none()

        stmt = (
            select(Store)
            .join(UserStoreRel, UserStoreRel.store_id == Store.id)
            .where(
                Store.id == store_id,
                UserStoreRel.user_id == user_id
            )
        )
        return db.execute(stmt).scalar_one_or_none()


