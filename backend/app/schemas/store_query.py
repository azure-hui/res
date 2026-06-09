from typing import Optional, Literal

from pydantic import BaseModel, Field


class StoreListQuery(BaseModel):
    page: int = Field(default=1, ge=1, description="页码，从 1 开始")
    page_size: int = Field(default=20, ge=1, le=100, description="每页数量，1-100")
    sort_by: Literal["id", "name", "city"] = Field(default="id", description="排序字段")
    sort_order: Literal["asc", "desc"] = Field(default="asc", description="排序方向")
    keyword: Optional[str] = Field(default=None, description="门店名模糊搜索")
    city: Optional[str] = Field(default=None, description="城市过滤")
    is_active: Optional[bool] = Field(default=None, description="启用状态过滤")
