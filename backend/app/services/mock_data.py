from app.core.security import hash_password


MOCK_USERS = [
    {
        "id": 1,
        "username": "owner_admin",
        "full_name": "\u7cfb\u7edf\u62e5\u6709\u8005",
        "role": "owner",
        "password_hash": hash_password("owner123"),
        "store_ids": [1001, 1002, 1003],
    },
    {
        "id": 2,
        "username": "manager_beijing",
        "full_name": "\u5317\u4eac\u95e8\u5e97\u7ecf\u7406",
        "role": "store_manager",
        "password_hash": hash_password("manager123"),
        "store_ids": [1001],
    },
]

MOCK_STORES = [
    {
        "id": 1001,
        "code": "BJ001",
        "name": "\u5317\u4eac\u56fd\u8d38\u5e97",
        "city": "\u5317\u4eac",
        "status": "open",
        "address": "\u5317\u4eac\u5e02\u671d\u9633\u533a\u56fd\u8d38\u8def 1 \u53f7",
    },
    {
        "id": 1002,
        "code": "SH001",
        "name": "\u4e0a\u6d77\u9646\u5bb6\u5634\u5e97",
        "city": "\u4e0a\u6d77",
        "status": "open",
        "address": "\u4e0a\u6d77\u5e02\u6d66\u4e1c\u65b0\u533a\u9646\u5bb6\u5634\u73af\u8def 88 \u53f7",
    },
    {
        "id": 1003,
        "code": "SZ001",
        "name": "\u6df1\u5733\u5357\u5c71\u5e97",
        "city": "\u6df1\u5733",
        "status": "renovation",
        "address": "\u6df1\u5733\u5e02\u5357\u5c71\u533a\u79d1\u6280\u8def 66 \u53f7",
    },
]

MOCK_DASHBOARD_OVERVIEW = {
    1001: {
        "store_id": 1001,
        "store_name": "\u5317\u4eac\u56fd\u8d38\u5e97",
        "business_date": "2026-03-26",
        "currency": "CNY",
        "revenue_today": 12880.50,
        "orders_today": 156,
        "customers_today": 312,
        "avg_order_value": 82.57,
        "table_turnover_rate": 3.4,
        "warning_count": 2,
    },
    1002: {
        "store_id": 1002,
        "store_name": "\u4e0a\u6d77\u9646\u5bb6\u5634\u5e97",
        "business_date": "2026-03-26",
        "currency": "CNY",
        "revenue_today": 16820.00,
        "orders_today": 188,
        "customers_today": 376,
        "avg_order_value": 89.47,
        "table_turnover_rate": 3.9,
        "warning_count": 1,
    },
    1003: {
        "store_id": 1003,
        "store_name": "\u6df1\u5733\u5357\u5c71\u5e97",
        "business_date": "2026-03-26",
        "currency": "CNY",
        "revenue_today": 0,
        "orders_today": 0,
        "customers_today": 0,
        "avg_order_value": 0,
        "table_turnover_rate": 0,
        "warning_count": 0,
    },
}
