from app.db.base_class import Base

# 为了让 Alembic 扫描到模型，必须在这里导入所有 model
from app.models.user import User
from app.models.store import Store
from app.models.user_store_rel import UserStoreRel
from app.models.dashboard_snapshot import DashboardSnapshot
from app.models.refresh_token import RefreshToken
from app.models.auth_audit_log import AuthAuditLog


__all__ = [
    "Base",
    "User",
    "Store",
    "UserStoreRel",
    "DashboardSnapshot",
    "RefreshToken",
    "AuthAuditLog",
]
