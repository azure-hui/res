from app.core.errors import UnauthorizedException
from app.core.config import settings
from app.core.security import build_refresh_placeholder, create_access_token
from app.services.mock_data import USERNAME_INDEX, MOCK_USERS


class AuthService:
    @staticmethod
    def login(username: str, password: str) -> dict:
        user = USERNAME_INDEX.get(username)
        if not user or user["password"] != password:
            raise UnauthorizedException("用户名或密码错误")

        token = create_access_token(user["user_id"])
        return {
            "access_token": token,
            "token_type": "bearer",
            "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            "refresh": build_refresh_placeholder(),
        }

    @staticmethod
    def get_user_by_id(user_id: str) -> dict:
        user = MOCK_USERS.get(user_id)
        if not user:
            raise UnauthorizedException("用户不存在或 token 无效")
        return {k: v for k, v in user.items() if k != "password"}
