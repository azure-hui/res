from fastapi import APIRouter, Depends, Request
from asgi_correlation_id import correlation_id
from sqlalchemy.orm import Session

from app.core.error_codes import ErrorCode
from app.core.exceptions import AppException
from app.core.response import success_response
from app.db.session import get_db
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService


router = APIRouter(prefix="/debug", tags=["debug"])


@router.post("/auth/login", summary="调试登录（DB 用户）")
async def debug_login(
    payload: LoginRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    auth_service = AuthService(db)
    user = auth_service.authenticate_user(payload.username, payload.password)
    if not user:
        raise AppException(
            code=ErrorCode.INVALID_CREDENTIALS,
            message="账号或密码错误",
            status_code=401,
        )

    token = auth_service.build_access_token_for_user(user)
    return success_response(
        data={
            "access_token": token,
            "token_type": "bearer",
            "expires_in": 3600,
            "user": auth_service.build_me_data(user),
        },
        message="success",
        request_id=correlation_id.get(),
    )
