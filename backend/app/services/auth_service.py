from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, NoReturn, Optional

from jose import ExpiredSignatureError, JWTError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.error_codes import ErrorCode
from app.core.exceptions import AppException
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    generate_jti,
    hash_token,
    verify_password,
)
from app.models.user import User
from app.repositories.auth_repository import AuthRepository
from asgi_correlation_id import correlation_id
from app.monitoring.metrics import inc_auth_failure

from app.core.logging import get_logger


logger = get_logger(__name__)


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.auth_repo = AuthRepository(db)

    def _now(self) -> datetime:
        return datetime.now(timezone.utc)

    def _ensure_aware_utc(self, dt: datetime | None) -> datetime | None:
        if dt is None:
            return None
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)

    def _is_user_locked(self, user: User) -> bool:
        locked_until = self._ensure_aware_utc(getattr(user, "locked_until", None))
        if locked_until is None:
            return False
        return locked_until > self._now()

    def get_user_by_username(self, username: str) -> Optional[User]:
        return self.auth_repo.get_user_by_username(username)

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.auth_repo.get_user_by_id(user_id)

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = self.get_user_by_username(username)
        if not user or not user.is_active:
            return None
        if not verify_password(password, user.password_hash):
            return None
        return user

    def build_me_data(self, user: User) -> dict:
        return {
            "id": user.id,
            "username": user.username,
            "display_name": user.display_name,
            "role": user.role,
            "is_active": user.is_active,
        }

    def build_access_token_for_user(self, user: User) -> str:
        access_token, _access_expire_at = create_access_token(user.id, user.role)
        return access_token

    def build_token_pair(self, user: User) -> dict:
        access_token, _access_expire_at = create_access_token(user.id, user.role)

        jti = generate_jti()
        refresh_token, refresh_expire_at = create_refresh_token(user.id, jti)
        refresh_token_hash = hash_token(refresh_token)

        self.auth_repo.create_refresh_token(
            user_id=user.id,
            jti=jti,
            token_hash=refresh_token_hash,
            expires_at=refresh_expire_at,
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "access_expires_in": settings.jwt_access_token_expire_minutes * 60,
            "refresh_expires_in": settings.jwt_refresh_token_expire_days * 24 * 60 * 60,
        }

    def login(
        self,
        username: str,
        password: str,
        ip: str | None = None,
        user_agent: str | None = None,
    ) -> dict:
        max_failed_attempts = int(
            getattr(
                settings,
                "LOGIN_MAX_FAILED_ATTEMPTS",
                getattr(settings, "auth_max_login_failures", 5),
            )
        )
        lock_minutes = int(
            getattr(
                settings,
                "LOGIN_LOCK_MINUTES",
                getattr(settings, "auth_lock_minutes", 1),
            )
        )

        try:
            user = self.get_user_by_username(username)

            if not user:
                logger.warning(
                    "authentication failed",
                    extra={
                        "event": "auth_failed",
                        "request_id": correlation_id.get(),
                        "reason_code": "USER_NOT_FOUND",
                        "client_ip": ip,
                        "error_code": str(ErrorCode.INVALID_CREDENTIALS),
                        "status_code": 401,
                    },
                )
                inc_auth_failure("USER_NOT_FOUND")
                self.auth_repo.create_audit_log(
                    user_id=None,
                    email=username,
                    event_type="login_failed",
                    result="failed",
                    reason_code="USER_NOT_FOUND",
                    ip=ip,
                    user_agent=user_agent,
                )
                self.db.commit()
                raise AppException(
                    code=ErrorCode.INVALID_CREDENTIALS,
                    message="用户名或密码错误",
                    status_code=401,
                )

            if not user.is_active:
                logger.warning(
                    "authentication failed",
                    extra={
                        "event": "auth_failed",
                        "request_id": correlation_id.get(),
                        "reason_code": "PERMISSION_DENIED",
                        "client_ip": ip,
                        "user_id": user.id,
                        "error_code": str(ErrorCode.PERMISSION_DENIED),
                        "status_code": 403,
                    },
                )
                inc_auth_failure("USER_DISABLED")
                self.auth_repo.create_audit_log(
                    user_id=user.id,
                    email=user.username,
                    event_type="login_failed",
                    result="failed",
                    reason_code="PERMISSION_DENIED",
                    ip=ip,
                    user_agent=user_agent,
                )
                self.db.commit()
                raise AppException(
                    code=ErrorCode.PERMISSION_DENIED,
                    message="用户已禁用",
                    status_code=403,
                )

            if self._is_user_locked(user):
                logger.warning(
                    "authentication failed",
                    extra={
                        "event": "auth_failed",
                        "request_id": correlation_id.get(),
                        "reason_code": "ACCOUNT_LOCKED",
                        "client_ip": ip,
                        "user_id": user.id,
                        "error_code": str(ErrorCode.ACCOUNT_LOCKED),
                        "status_code": 401,
                    },
                )
                inc_auth_failure("ACCOUNT_LOCKED")
                self.auth_repo.create_audit_log(
                    user_id=user.id,
                    email=user.username,
                    event_type="login_failed",
                    result="failed",
                    reason_code="ACCOUNT_LOCKED",
                    ip=ip,
                    user_agent=user_agent,
                )
                self.db.commit()
                raise AppException(
                    code=ErrorCode.ACCOUNT_LOCKED,
                    message="账户已锁定，请稍后重试",
                    status_code=401,
                )

            if not verify_password(password, user.password_hash):
                current_failed = int(user.failed_login_attempts or 0) + 1
                user.failed_login_attempts = current_failed

                reason_code = "INVALID_PASSWORD"
                error_code = ErrorCode.INVALID_CREDENTIALS
                error_message = "用户名或密码错误"

                if current_failed >= max_failed_attempts:
                    user.locked_until = self._now() + timedelta(minutes=lock_minutes)
                    reason_code = "ACCOUNT_LOCKED"
                    error_code = ErrorCode.ACCOUNT_LOCKED
                    error_message = "账户已锁定，请稍后重试"
                    inc_auth_failure("ACCOUNT_LOCKED")
                else:
                    inc_auth_failure("INVALID_PASSWORD")

                logger.warning(
                    "authentication failed",
                    extra={
                        "event": "auth_failed",
                        "request_id": correlation_id.get(),
                        "reason_code": reason_code,
                        "client_ip": ip,
                        "user_id": user.id,
                        "error_code": str(error_code),
                        "status_code": 401,
                    },
                )

                self.db.add(user)
                self.auth_repo.create_audit_log(
                    user_id=user.id,
                    email=user.username,
                    event_type="login_failed",
                    result="failed",
                    reason_code=reason_code,
                    ip=ip,
                    user_agent=user_agent,
                )
                self.db.commit()

                raise AppException(
                    code=error_code,
                    message=error_message,
                    status_code=401,
                )

            user.failed_login_attempts = 0
            user.locked_until = None
            user.last_login_at = self._now()
            user.last_login_ip = ip
            self.db.add(user)

            result = self.build_token_pair(user)

            self.auth_repo.create_audit_log(
                user_id=user.id,
                email=user.username,
                event_type="login_success",
                result="success",
                reason_code=None,
                ip=ip,
                user_agent=user_agent,
            )
            self.db.commit()

            logger.info(
                "authentication succeeded",
                extra={
                    "event": "auth_login_success",
                    "request_id": correlation_id.get(),
                    "client_ip": ip,
                    "user_id": user.id,
                    "status_code": 200,
                },
            )

            result["user"] = self.build_me_data(user)
            return result

        except AppException:
            raise
        except Exception:
            self.db.rollback()
            logger.exception(
                "unhandled exception occurred",
                extra={
                    "event": "unhandled_exception",
                    "request_id": correlation_id.get(),
                    "client_ip": ip,
                    "status_code": 500,
                },
            )
            raise


    def _raise_token_invalid(self, message: str = "Refresh token 无效") -> NoReturn:
        raise AppException(
            code=ErrorCode.TOKEN_INVALID,
            message=message,
            status_code=401,
        )

    def _raise_token_expired(self, message: str = "Refresh token 已过期") -> NoReturn:
        raise AppException(
            code=ErrorCode.TOKEN_EXPIRED,
            message=message,
            status_code=401,
        )

    def _log_refresh_failed(
        self,
        *,
        reason_code: str,
        ip: str | None = None,
        user_agent: str | None = None,
        user_id: int | None = None,
        email: str | None = None,
    ) -> None:
        self.auth_repo.create_audit_log(
            event_type="refresh_failed",
            result="failed",
            user_id=user_id,
            email=email,
            reason_code=reason_code,
            ip=ip,
            user_agent=user_agent,
        )

    def refresh_tokens(
        self,
        refresh_token: str,
        ip: str | None = None,
        user_agent: str | None = None,
    ) -> dict:
        current_user_id: int | None = None
        current_email: str | None = None

        try:
            payload: dict[str, Any] = decode_token(refresh_token, "refresh")

            sub_raw = payload.get("sub")
            jti_raw = payload.get("jti")
            if sub_raw is None or not isinstance(jti_raw, str) or not jti_raw:
                self._raise_token_invalid()

            sub = str(sub_raw)
            jti = jti_raw

            try:
                user_id = int(sub)
            except (TypeError, ValueError):
                self._raise_token_invalid()

            current_user_id = user_id

            token_obj = self.auth_repo.get_refresh_token_by_jti(jti)
            if token_obj is None:
                self._raise_token_invalid()

            if token_obj.revoked_at is not None:
                self._raise_token_invalid("Refresh token 已失效")

            expires_at = self._ensure_aware_utc(token_obj.expires_at)
            if expires_at is None or expires_at < self._now():
                self._raise_token_expired()

            incoming_hash = hash_token(refresh_token)
            if incoming_hash != token_obj.token_hash:
                self._raise_token_invalid()

            user = self.get_user_by_id(user_id)
            if user is None or not user.is_active:
                self._raise_token_invalid()

            current_email = user.username

            self.auth_repo.revoke_refresh_token(token_obj)
            token_pair = self.build_token_pair(user)

            self.auth_repo.create_audit_log(
                event_type="refresh_success",
                result="success",
                user_id=user.id,
                email=current_email,
                reason_code=None,
                ip=ip,
                user_agent=user_agent,
            )

            self.db.commit()

            return {
                **token_pair,
                "user": self.build_me_data(user),
            }

        except ExpiredSignatureError:
            self.db.rollback()
            self._log_refresh_failed(
                reason_code="token_expired",
                ip=ip,
                user_agent=user_agent,
                user_id=current_user_id,
                email=current_email,
            )
            self.db.commit()
            self._raise_token_expired()

        except JWTError:
            self.db.rollback()
            self._log_refresh_failed(
                reason_code="token_invalid",
                ip=ip,
                user_agent=user_agent,
                user_id=current_user_id,
                email=current_email,
            )
            self.db.commit()
            self._raise_token_invalid()

        except AppException:
            self.db.rollback()
            reason_code = "token_invalid"
            self._log_refresh_failed(
                reason_code=reason_code,
                ip=ip,
                user_agent=user_agent,
                user_id=current_user_id,
                email=current_email,
            )
            self.db.commit()
            raise

        except Exception:
            self.db.rollback()
            raise
