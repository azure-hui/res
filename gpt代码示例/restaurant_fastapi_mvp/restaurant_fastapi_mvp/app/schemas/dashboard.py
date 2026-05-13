from pydantic import BaseModel


class KPIItem(BaseModel):
    sales_amount: float
    orders_count: int
    customer_count: int
    table_turnover_rate: float
    warning_count: int


class DashboardOverviewResponse(BaseModel):
    store_id: str
    date: str
    kpi: KPIItem
