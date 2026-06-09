from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.response import success_response
from app.db.session import get_db
from app.deps.permissions import require_store_access
from app.models.store import Store
from app.schemas.dashboard import DashboardOverviewResponse
from app.services.dashboard_service import get_dashboard_overview
from asgi_correlation_id import correlation_id


router = APIRouter(prefix="/stores", tags=["dashboard"])


@router.get(
    "/{store_id}/dashboard/overview",
    summary="门店 KPI 概览",
    response_model=DashboardOverviewResponse,
    responses={
        401: {"description": "未登录或 token 无效"},
        403: {"description": "无门店权限（40301）"},
        404: {"description": "门店不存在/禁用（40401）或概览不存在（40402）"},
        422: {"description": "请求参数错误"},
    },
)
async def dashboard_overview(
    request: Request,
    db: Session = Depends(get_db),
    store: Store = Depends(require_store_access),
):
    data = get_dashboard_overview(db, store)
    return success_response(
        data=data,
        message="success",
        request_id=correlation_id.get(),
    )
