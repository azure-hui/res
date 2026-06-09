from typing import Optional, Any
from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    code: int = 0
    message: str = "success"
    data: Optional[Any] = None
    request_id: Optional[str] = None
    timestamp: Optional[str] = None


class LoginRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=128)


class RefreshTokenRequest(BaseModel):
    refresh_token: str = Field(..., min_length=1)


class CurrentUser(BaseModel):
    id: int
    username: str
    display_name: Optional[str] = None
    role: str
    is_active: bool


class TokenPairData(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    access_expires_in: int
    refresh_expires_in: int
    user: CurrentUser


class TokenPairResponse(BaseResponse):
    data: Optional[TokenPairData] = None


class CurrentUserResponse(BaseResponse):
    data: Optional[CurrentUser] = None
