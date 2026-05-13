from typing import Annotated
from fastapi import Depends, Header, Path
from app.core.errors import UnauthorizedException
from app.core.security import decode_token, ensure_access_token
from app.services.auth_service import AuthService
from app.services.store_service import StoreService


async def get_current_user(authorization: Annotated[str | None, Header()] = None) -> dict:
    if not authorization:
        raise UnauthorizedException("缺少 Authorization 头")

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise UnauthorizedException("Authorization 格式必须为 Bearer <token>")

    payload = decode_token(token)
    ensure_access_token(payload)
    user_id = payload.get("sub")
    if not user_id:
        raise UnauthorizedException("token 缺少用户标识")
    return AuthService.get_user_by_id(user_id)


CurrentUser = Annotated[dict, Depends(get_current_user)]


async def verify_store_access(
    store_id: Annotated[str, Path()],
    current_user: CurrentUser,
) -> str:
    StoreService.validate_store_access(current_user["user_id"], store_id)
    return store_id
