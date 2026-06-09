from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.response import success_response
from app.db.session import get_db
from app.deps.auth import get_current_user
from app.schemas.auth import (
    CurrentUserResponse,
    LoginRequest,
    RefreshTokenRequest,
    TokenPairResponse,
)
from app.services.auth_service import AuthService
from asgi_correlation_id import correlation_id

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", summary="登录", response_model=TokenPairResponse)
def login(payload: LoginRequest, request: Request, db: Session = Depends(get_db)):
    service = AuthService(db)
    ip = request.client.host if request.client else None
    user_agent = request.headers.get("user-agent")

    result = service.login(
        payload.username,
        payload.password,
        ip=ip,
        user_agent=user_agent,
    )

    return success_response(
        data=result,
        message="success",
        request_id=correlation_id.get(),
    )


@router.get("/me", summary="当前用户信息", response_model=CurrentUserResponse)
def get_me(
    request: Request,
    current_user: dict = Depends(get_current_user),
):
    return success_response(
        data={
            "id": current_user["id"],
            "username": current_user["username"],
            "display_name": current_user.get("display_name"),
            "role": current_user["role"],
            "is_active": current_user["is_active"],
        },
        message="success",
        request_id=correlation_id.get(),
    )


@router.post("/refresh", summary="刷新 token", response_model=TokenPairResponse)
def refresh_token(
    payload: RefreshTokenRequest,
    request: Request,
    db: Session = Depends(get_db),
):
    service = AuthService(db)
    ip = request.client.host if request.client else None
    user_agent = request.headers.get("user-agent")

    result = service.refresh_tokens(
        payload.refresh_token,
        ip=ip,
        user_agent=user_agent,
    )

    return success_response(
        data=result,
        message="success",
        request_id=correlation_id.get(),
    )

