from fastapi import APIRouter, Request
from app.core.config import settings
from app.core.response import success_response

router = APIRouter(tags=["health"])


@router.get("/health", summary="健康检查")
async def health_check(request: Request):
    return success_response(
        {
            "app_name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "env": settings.APP_ENV,
            "status": "ok",
        },
        request.state.request_id,
    )
