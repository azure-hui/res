from typing import Optional

from pydantic import BaseModel


class StoreListItem(BaseModel):
    id: int
    name: str
    city: Optional[str] = None
    is_active: bool


class StoreListData(BaseModel):
    items: list[StoreListItem]
    total: int
    page: int
    page_size: int
    sort_by: str
    sort_order: str


class StoreListResponse(BaseModel):
    code: int
    message: str
    data: StoreListData
    request_id: Optional[str] = None
    timestamp: str
