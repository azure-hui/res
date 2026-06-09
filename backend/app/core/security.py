from datetime import datetime, timedelta, timezone
import hashlib
import uuid

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import settings


pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def generate_jti() -> str:
    return uuid.uuid4().hex


def hash_token(raw_token: str) -> str:
    return hashlib.sha256(raw_token.encode("utf-8")).hexdigest()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(user_id: int, role: str) -> tuple[str, datetime]:
    expire_at = datetime.now(timezone.utc) + timedelta(
        minutes=settings.jwt_access_token_expire_minutes
    )
    payload = {
        "sub": str(user_id),
        "type": "access",
        "role": role,
        "exp": expire_at,
    }
    token = jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return token, expire_at


def create_refresh_token(user_id: int, jti: str) -> tuple[str, datetime]:
    expire_at = datetime.now(timezone.utc) + timedelta(
        days=settings.jwt_refresh_token_expire_days
    )
    payload = {
        "sub": str(user_id),
        "type": "refresh",
        "jti": jti,
        "exp": expire_at,
    }
    token = jwt.encode(
        payload,
        settings.jwt_refresh_secret_key,
        algorithm=settings.jwt_algorithm,
    )
    return token, expire_at


def decode_token(token: str, token_type: str) -> dict:
    secret = (
        settings.jwt_secret_key
        if token_type == "access"
        else settings.jwt_refresh_secret_key
    )
    payload = jwt.decode(token, secret, algorithms=[settings.jwt_algorithm])

    if payload.get("type") != token_type:
        raise ValueError("Invalid token type")

    return payload


#def decode_access_token(token: str) -> dict:
#    return decode_token(token, "access")
def decode_access_token(token: str) -> dict:
    payload = jwt.decode(
        token,
        settings.jwt_secret_key,
        algorithms=[settings.jwt_algorithm],
    )

    if payload.get("type") != "access":
        raise JWTError("Invalid access token type")

    return payload