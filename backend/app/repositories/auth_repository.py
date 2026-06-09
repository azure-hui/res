from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.refresh_token import RefreshToken
from app.models.auth_audit_log import AuthAuditLog


class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def _ensure_aware_utc(dt: datetime | None) -> datetime | None:
        if dt is None:
            return None
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)

    def get_user_by_username(self, username: str) -> Optional[User]:
        stmt = select(User).where(User.username == username)
        return self.db.execute(stmt).scalar_one_or_none()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        stmt = select(User).where(User.id == user_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def create_refresh_token(
        self,
        *,
        user_id: int,
        jti: str,
        token_hash: str,
        expires_at: datetime,
    ) -> RefreshToken:
        token = RefreshToken(
            user_id=user_id,
            jti=jti,
            token_hash=token_hash,
            expires_at=expires_at,
        )
        self.db.add(token)
        self.db.flush()
        return token

    def get_refresh_token_by_jti(self, jti: str) -> RefreshToken | None:
        stmt = select(RefreshToken).where(RefreshToken.jti == jti)
        return self.db.execute(stmt).scalar_one_or_none()

    def revoke_refresh_token(self, token: RefreshToken) -> None:
        token.revoked_at = datetime.now(timezone.utc)
        self.db.flush()

    def is_refresh_token_active(self, token: RefreshToken) -> bool:
        if token.revoked_at is not None:
            return False

        expires_at = self._ensure_aware_utc(token.expires_at)
        if expires_at is None:
            return False

        if expires_at < datetime.now(timezone.utc):
            return False

        return True

    def create_audit_log(
        self,
        *,
        user_id: int | None,
        email: str | None,
        event_type: str,
        result: str,
        reason_code: str | None,
        ip: str | None,
        user_agent: str | None,
    ) -> None:
        log = AuthAuditLog(
            user_id=user_id,
            email=email,
            event_type=event_type,
            result=result,
            reason_code=reason_code,
            ip=ip,
            user_agent=user_agent,
        )
        self.db.add(log)
        self.db.flush()