from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.response import success_response
from app.db.session import get_db
from app.deps.auth import get_current_user
from app.schemas.store import StoreListResponse
from app.schemas.store_query import StoreListQuery
from app.services.store_service import list_stores
from asgi_correlation_id import correlation_id

router = APIRouter(prefix="/stores", tags=["stores"])


@router.get(
    "",
    summary="可访问门店列表",
    response_model=StoreListResponse,
)
async def get_stores(
    request: Request,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    query: StoreListQuery = Depends(),
):
    data = list_stores(
        db,
        current_user=current_user,
        keyword=query.keyword,
        city=query.city,
        is_active=query.is_active,
        page=query.page,
        page_size=query.page_size,
        sort_by=query.sort_by,
        sort_order=query.sort_order,
    )

    return success_response(
        data=data,
        message="success",
        request_id=correlation_id.get(),
    )
