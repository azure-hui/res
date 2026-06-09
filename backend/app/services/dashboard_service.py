from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.error_codes import ErrorCode
from app.core.exceptions import AppException
from app.models.dashboard_snapshot import DashboardSnapshot
from app.models.store import Store
from app.repositories.dashboard_repository import DashboardRepository


dashboard_repo = DashboardRepository()


def _build_overview_data(store: Store, snapshot: DashboardSnapshot) -> dict:
    # Rule 4: 快照字段为 None 时统一兜底
    revenue_today = float(snapshot.revenue or 0)
    orders_today = int(snapshot.order_count or 0)
    customers_today = int(snapshot.customer_count or 0)

    # Rule 5: 计算字段不抛异常（orders=0 时固定 0.0）
    avg_order_value = 0.0 if orders_today == 0 else round(revenue_today / orders_today, 2)

    return {
        "store_id": store.id,
        "store_name": store.name,
        "business_date": snapshot.biz_date.isoformat(),
        "currency": "CNY",
        "revenue_today": revenue_today,
        "orders_today": orders_today,
        "customers_today": customers_today,
        "avg_order_value": avg_order_value,
        # 非 DB 字段：当前占位，后续接真实数据
        "table_turnover_rate": 0.0,
        # 非 DB 字段：当前占位，后续接告警系统
        "warning_count": 0,
    }


def get_dashboard_overview(db: Session, store: Store) -> dict:
    snapshot = dashboard_repo.get_latest_snapshot_by_store_id(db, store.id)

    # Rule 3: 门店存在 + 有权限 + 无概览数据 => 40402
    if snapshot is None:
        raise AppException(
            code=ErrorCode.DASHBOARD_NOT_FOUND,  # 40402
            message=f"门店 {store.id} 暂无概览数据",
            status_code=404,
        )

    return _build_overview_data(store, snapshot)
