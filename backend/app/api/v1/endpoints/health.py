from fastapi import APIRouter, Request
from app.core.response import success_response
from app.db.session import ping_db
from asgi_correlation_id import correlation_id

router = APIRouter()


@router.get("/health", summary="健康检查")
async def health_check(request: Request):
    db_ok = ping_db()
    return success_response(
        data={
            "app": {"status": "up"},
            "db": {"status": "up" if db_ok else "down"},
        },
        message="success",
        request_id=correlation_id.get(),
    )
