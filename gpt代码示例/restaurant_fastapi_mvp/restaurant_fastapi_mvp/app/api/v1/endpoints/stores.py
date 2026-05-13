from typing import Annotated
from fastapi import APIRouter, Depends, Request
from app.core.response import success_response
from app.deps.auth import CurrentUser, verify_store_access
from app.services.dashboard_service import DashboardService
from app.services.store_service import StoreService

router = APIRouter(prefix="/stores", tags=["stores"])


@router.get("", summary="获取当前用户可访问门店列表")
async def list_stores(request: Request, current_user: CurrentUser):
    stores = StoreService.list_accessible_stores(current_user["user_id"])
    return success_response(stores, request.state.request_id)


@router.get("/{store_id}/dashboard/overview", summary="获取门店首页 KPI 概览")
async def dashboard_overview(
    request: Request,
    current_user: CurrentUser,
    _: Annotated[str, Depends(verify_store_access)],
    store_id: str,
):
    overview = DashboardService.get_overview(store_id)
    return success_response(overview, request.state.request_id)
