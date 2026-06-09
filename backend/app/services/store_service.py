from __future__ import annotations

from typing import Optional

from sqlalchemy.orm import Session

from app.repositories.store_repository import StoreRepository


store_repo = StoreRepository()


def _to_store_list_item(store) -> dict:
    return {
        "id": store.id,
        "name": store.name,
        "city": store.city,
        "is_active": store.is_active,
    }


def list_stores(
    db: Session,
    *,
    current_user: dict,
    keyword: Optional[str] = None,
    city: Optional[str] = None,
    is_active: Optional[bool] = None,
    page: int = 1,
    page_size: int = 20,
    sort_by: str = "id",
    sort_order: str = "asc",
) -> dict:
    page = max(page, 1)
    page_size = max(min(page_size, 100), 1)
    offset = (page - 1) * page_size

    stores = store_repo.list_stores(
        db,
        user_id=int(current_user["id"]),
        role=str(current_user["role"]),
        keyword=keyword,
        city=city,
        is_active=is_active,
        sort_by=sort_by,
        sort_order=sort_order,
        offset=offset,
        limit=page_size,
    )

    total = store_repo.count_stores(
        db,
        user_id=int(current_user["id"]),
        role=str(current_user["role"]),
        keyword=keyword,
        city=city,
        is_active=is_active,
    )

    items = [_to_store_list_item(s) for s in stores]

    return {
        "items": items,
        "total": total,
        "page": page,
        "page_size": page_size,
        "sort_by": sort_by,
        "sort_order": sort_order,
    }
