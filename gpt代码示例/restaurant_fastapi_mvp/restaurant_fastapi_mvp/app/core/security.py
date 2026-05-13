from datetime import timedelta
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from app.core.config import settings
from app.core.errors import UnauthorizedException
from app.infra.time import now_utc


def create_access_token(subject: str) -> str:
    expire = now_utc() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": subject,
        "type": "access",
        "exp": expire,
        "iat": now_utc(),
    }
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
    except ExpiredSignatureError as exc:
        raise UnauthorizedException("token 已过期") from exc
    except InvalidTokenError as exc:
        raise UnauthorizedException("token 无效") from exc


def ensure_access_token(payload: dict) -> None:
    if payload.get("type") != "access":
        raise UnauthorizedException("token 类型错误")


def build_refresh_placeholder() -> dict:
    return {
        "supported": False,
        "message": "refresh token 暂未实现，当前仅预留字段",
    }
