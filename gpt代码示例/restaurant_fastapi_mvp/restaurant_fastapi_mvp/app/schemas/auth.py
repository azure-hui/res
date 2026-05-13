from pydantic import BaseModel, Field
from app.core.constants import Role


class LoginRequest(BaseModel):
    username: str = Field(..., examples=["owner_admin"])
    password: str = Field(..., examples=["owner123"])


class TokenPayload(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    refresh: dict


class UserMe(BaseModel):
    user_id: str
    username: str
    display_name: str
    role: Role
