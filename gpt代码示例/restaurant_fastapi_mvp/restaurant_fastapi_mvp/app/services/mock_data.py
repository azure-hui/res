from app.core.constants import Role

MOCK_USERS = {
    "u_owner_001": {
        "user_id": "u_owner_001",
        "username": "owner_admin",
        "display_name": "总店老板",
        "role": Role.OWNER,
        "password": "owner123",
    },
    "u_mgr_001": {
        "user_id": "u_mgr_001",
        "username": "manager_beijing",
        "display_name": "北京店店长",
        "role": Role.STORE_MANAGER,
        "password": "manager123",
    },
}

USERNAME_INDEX = {user["username"]: user for user in MOCK_USERS.values()}

MOCK_STORES = {
    "store_001": {
        "store_id": "store_001",
        "store_name": "朝阳旗舰店",
        "city": "北京",
        "status": "open",
    },
    "store_002": {
        "store_id": "store_002",
        "store_name": "浦东体验店",
        "city": "上海",
        "status": "open",
    },
}

USER_STORE_ACCESS = {
    "u_owner_001": ["store_001", "store_002"],
    "u_mgr_001": ["store_001"],
}

MOCK_DASHBOARD_OVERVIEW = {
    "store_001": {
        "store_id": "store_001",
        "date": "2026-03-26",
        "kpi": {
            "sales_amount": 18234.5,
            "orders_count": 268,
            "customer_count": 412,
            "table_turnover_rate": 3.8,
            "warning_count": 1,
        },
    },
    "store_002": {
        "store_id": "store_002",
        "date": "2026-03-26",
        "kpi": {
            "sales_amount": 13780.0,
            "orders_count": 201,
            "customer_count": 326,
            "table_turnover_rate": 3.2,
            "warning_count": 0,
        },
    },
}
