from fastapi import APIRouter, Depends, Request

from app.core.response import success_response
from app.deps.auth import get_current_user
from asgi_correlation_id import correlation_id


router = APIRouter(prefix="/debug", tags=["debug"])


@router.get("/whoami", summary="\u8c03\u8bd5\u5f53\u524d\u7528\u6237")
async def debug_whoami(
    request: Request,
    current_user: dict = Depends(get_current_user),
):
    return success_response(
        data={
            "user_id": current_user["id"],
            "username": current_user["username"],
            "role": current_user["role"],
        },
        request_id=correlation_id.get(),
    )
