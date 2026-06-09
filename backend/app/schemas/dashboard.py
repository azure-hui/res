from typing import Optional

from pydantic import BaseModel


class DashboardOverviewData(BaseModel):
    store_id: int
    store_name: str
    business_date: str
    currency: str
    revenue_today: float
    orders_today: int
    customers_today: int
    avg_order_value: float
    table_turnover_rate: float
    warning_count: int


class DashboardOverviewResponse(BaseModel):
    code: int
    message: str
    data: DashboardOverviewData
    request_id: Optional[str] = None
    timestamp: str
