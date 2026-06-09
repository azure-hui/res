from fastapi import APIRouter, Depends, Request

from app.core.response import success_response
from app.deps.auth import get_current_user
from app.deps.permissions import require_store_access
from app.models.store import Store
from asgi_correlation_id import correlation_id

router = APIRouter(prefix="/debug", tags=["debug"])


@router.get("/stores/{store_id}/access", summary="Debug store access")
async def debug_store_access(
    request: Request,
    store: Store = Depends(require_store_access),
    current_user: dict = Depends(get_current_user),
):
    return success_response(
        data={
            "store_id": store.id,
            "username": current_user["username"],
            "role": current_user["role"],
            "result": "allowed",
        },
        request_id=correlation_id.get(),
    )
