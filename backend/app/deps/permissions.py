from fastapi import Depends, Path
from sqlalchemy.orm import Session

from app.core.error_codes import ErrorCode
from app.core.exceptions import AppException
from app.db.session import get_db
from app.deps.auth import get_current_user
from app.models.store import Store
from app.repositories.store_repository import StoreRepository


store_repo = StoreRepository()


def require_store_access(
    store_id: int = Path(...),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
) -> Store:
    # Rule 1: 门店不存在或禁用统一返回 40401
    store = store_repo.get_store_by_id(db, store_id)
    if not store or not store.is_active:
        raise AppException(
            code=ErrorCode.STORE_NOT_FOUND,  # 40401
            message=f"门店 {store_id} 不存在或已禁用",
            status_code=404,
        )

    # Rule 2: 门店存在但无权限统一返回 40301
    scoped_store = store_repo.get_store_by_id_in_scope(
        db,
        store_id=store_id,
        user_id=int(current_user["id"]),
        role=str(current_user["role"]),
    )
    if not scoped_store:
        raise AppException(
            code=ErrorCode.STORE_FORBIDDEN,  # 40301
            message=f"无权访问门店 {store_id}",
            status_code=403,
        )

    return store
