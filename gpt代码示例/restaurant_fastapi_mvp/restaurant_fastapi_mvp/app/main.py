import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.api.v1.router import api_router
from app.api.v1.endpoints.health import router as health_router
from app.core.config import settings
from app.core.constants import ErrorCode
from app.core.errors import AppException
from app.core.logging import RequestContextMiddleware, setup_logging
from app.core.response import error_response

setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("application starting")
    yield
    logger.info("application shutting down")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
    description=(
        "Restaurant Analytics FastAPI MVP。"
        "当前版本使用内存 Mock 数据，无持久化、无 refresh token，"
        "并预留 Idempotency-Key 文档规范。"
    ),
)

app.add_middleware(RequestContextMiddleware)
app.include_router(health_router)
app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(exc.code, exc.message, request.state.request_id, exc.data),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=error_response(
            ErrorCode.VALIDATION_ERROR,
            "请求参数校验失败",
            request.state.request_id,
            {"errors": exc.errors()},
        ),
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    code = ErrorCode.BAD_REQUEST
    if exc.status_code == status.HTTP_401_UNAUTHORIZED:
        code = ErrorCode.UNAUTHORIZED
    elif exc.status_code == status.HTTP_403_FORBIDDEN:
        code = ErrorCode.FORBIDDEN
    elif exc.status_code == status.HTTP_404_NOT_FOUND:
        code = ErrorCode.NOT_FOUND

    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(code, exc.detail, request.state.request_id),
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("unhandled exception: %s", exc)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=error_response(
            ErrorCode.INTERNAL_SERVER_ERROR,
            "服务器内部错误",
            request.state.request_id,
        ),
    )
