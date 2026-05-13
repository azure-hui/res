from fastapi import APIRouter, Request
from app.core.response import success_response
from app.deps.auth import CurrentUser
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", summary="登录并获取 access token")
async def login(payload: LoginRequest, request: Request):
    result = AuthService.login(payload.username, payload.password)
    return success_response(result, request.state.request_id, message="login success")


@router.get("/me", summary="获取当前用户信息")
async def me(request: Request, current_user: CurrentUser):
    return success_response(current_user, request.state.request_id)
