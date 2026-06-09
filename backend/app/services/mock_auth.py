from typing import Optional

from app.core.security import create_access_token, verify_password
from app.services.mock_data import MOCK_USERS


def get_user_by_username(username: str) -> Optional[dict]:
    for user in MOCK_USERS:
        if user["username"] == username:
            return user
    return None


def get_user_by_id(user_id: int) -> Optional[dict]:
    for user in MOCK_USERS:
        if user["id"] == user_id:
            return user
    return None


def authenticate_user(username: str, password: str) -> Optional[dict]:
    user = get_user_by_username(username)
    if not user:
        return None

    if not verify_password(password, user["password_hash"]):
        return None

    return user


def user_can_access_store(user: dict, store_id: int) -> bool:
    if user["role"] == "owner":
        return True
    return store_id in user.get("store_ids", [])


def build_access_token_for_user(user: dict) -> str:
    token, _ = create_access_token(user["id"], user["role"])
    return token

def build_me_data(user: dict) -> dict:
    return {
        "id": user["id"],
        "username": user["username"],
        "full_name": user.get("full_name"),
        "role": user["role"],
    }
