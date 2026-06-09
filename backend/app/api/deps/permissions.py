from fastapi import Depends, Path

from app.deps.auth import get_current_user
from app.core.error_codes import ErrorCode
from app.core.exceptions import AppException


def require_store_access(store_id_param: str = "store_id"):
    def dependency(
        store_id: int = Path(...),
        current_user: dict = Depends(get_current_user),
    ) -> dict:
        if current_user["role"] in {"owner", "admin"}:
            return current_user

        if store_id not in current_user.get("store_ids", []):
            raise AppException(
                code=ErrorCode.STORE_ACCESS_DENIED,
                message="无门店权限",
                status_code=403,
            )

        return current_user

    return dependency