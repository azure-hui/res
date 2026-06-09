from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.dashboard_snapshot import DashboardSnapshot


class DashboardRepository:
    def get_latest_snapshot_by_store_id(
        self,
        db: Session,
        store_id: int,
    ) -> DashboardSnapshot | None:
        stmt = (
            select(DashboardSnapshot)
            .where(DashboardSnapshot.store_id == store_id)
            .order_by(DashboardSnapshot.biz_date.desc())
        )
        return db.execute(stmt).scalars().first()
