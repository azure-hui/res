from app.core.errors import ForbiddenException, NotFoundException
from app.services.mock_data import MOCK_STORES, USER_STORE_ACCESS


class StoreService:
    @staticmethod
    def list_accessible_stores(user_id: str) -> list[dict]:
        store_ids = USER_STORE_ACCESS.get(user_id, [])
        return [MOCK_STORES[store_id] for store_id in store_ids if store_id in MOCK_STORES]

    @staticmethod
    def validate_store_access(user_id: str, store_id: str) -> None:
        if store_id not in MOCK_STORES:
            raise NotFoundException("门店不存在")
        allowed_store_ids = USER_STORE_ACCESS.get(user_id, [])
        if store_id not in allowed_store_ids:
            raise ForbiddenException("无权限访问该门店")
