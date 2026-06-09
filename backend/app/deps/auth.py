from __future__ import annotations

from asgi_correlation_id import correlation_id
from fastapi import Depends, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import ExpiredSignatureError, JWTError
from sqlalchemy.orm import Session

from app.core.error_codes import ErrorCode
from app.core.exceptions import AppException
from app.core.logging import get_logger
from app.core.security import decode_access_token
from app.db.session import get_db
from app.services.auth_service import AuthService
from app.monitoring.metrics import inc_auth_failure


security = HTTPBearer(auto_error=False)
logger = get_logger(__name__)


def _log_auth_failed(
    request: Request,
    *,
    reason_code: str,
    error_code: str,
    status_code: int,
) -> None:
    logger.warning(
        "authentication failed",
        extra={
            "event": "auth_failed",
            "request_id": correlation_id.get(),
            "method": request.method,
            "path": request.url.path,
            "status_code": status_code,
            "error_code": error_code,
            "reason_code": reason_code,
            "client_ip": request.client.host if request.client else None,
        },
    )


def get_current_user(
    request: Request,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> dict:
    if credentials is None:
        _log_auth_failed(
            request,
            reason_code="TOKEN_MISSING",
            error_code=str(ErrorCode.AUTH_HEADER_MISSING),
            status_code=401,
        )
        inc_auth_failure("TOKEN_MISSING")
        raise AppException(
            code=ErrorCode.AUTH_HEADER_MISSING,
            message="缺少 Authorization 头",
            status_code=401,
        )

    if credentials.scheme.lower() != "bearer" or not credentials.credentials:
        _log_auth_failed(
            request,
            reason_code="TOKEN_INVALID",
            error_code=str(ErrorCode.TOKEN_INVALID),
            status_code=401,
        )
        inc_auth_failure("TOKEN_INVALID")
        raise AppException(
            code=ErrorCode.TOKEN_INVALID,
            message="Authorization 格式错误，应为 Bearer <token>",
            status_code=401,
        )

    try:
        payload = decode_access_token(credentials.credentials)
    except ExpiredSignatureError:
        _log_auth_failed(
            request,
            reason_code="TOKEN_EXPIRED",
            error_code=str(ErrorCode.TOKEN_EXPIRED),
            status_code=401,
        )
        inc_auth_failure("TOKEN_EXPIRED")
        raise AppException(
            code=ErrorCode.TOKEN_EXPIRED,
            message="token 已过期",
            status_code=401,
        )
    except JWTError:
        _log_auth_failed(
            request,
            reason_code="TOKEN_INVALID",
            error_code=str(ErrorCode.TOKEN_INVALID),
            status_code=401,
        )
        inc_auth_failure("TOKEN_INVALID")
        raise AppException(
            code=ErrorCode.TOKEN_INVALID,
            message="无效 token",
            status_code=401,
        )

    user_id = payload.get("sub")
    token_type = payload.get("type")

    if not user_id:
        _log_auth_failed(
            request,
            reason_code="TOKEN_INVALID",
            error_code=str(ErrorCode.TOKEN_INVALID),
            status_code=401,
        )
        inc_auth_failure("TOKEN_INVALID")
        raise AppException(
            code=ErrorCode.TOKEN_INVALID,
            message="token 缺少用户标识",
            status_code=401,
        )

    if token_type != "access":
        _log_auth_failed(
            request,
            reason_code="PERMISSION_DENIED",
            error_code=str(ErrorCode.PERMISSION_DENIED),
            status_code=403,
        )
        inc_auth_failure("PERMISSION_DENIED")
        raise AppException(
            code=ErrorCode.PERMISSION_DENIED,
            message="token 类型不允许访问该资源",
            status_code=403,
        )

    auth_service = AuthService(db)
    user = auth_service.get_user_by_id(int(user_id))
    if not user or not user.is_active:
        _log_auth_failed(
            request,
            reason_code="USER_NOT_FOUND",
            error_code=str(ErrorCode.TOKEN_INVALID),
            status_code=401,
        )
        inc_auth_failure("USER_NOT_FOUND")
        raise AppException(
            code=ErrorCode.TOKEN_INVALID,
            message="用户不存在或已禁用",
            status_code=401,
        )

    store_ids = [rel.store_id for rel in getattr(user, "store_relations", [])]

    return {
        "id": user.id,
        "username": user.username,
        "display_name": user.display_name,
        "role": user.role,
        "is_active": user.is_active,
        "store_ids": store_ids,
    }
