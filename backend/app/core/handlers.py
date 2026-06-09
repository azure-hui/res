from __future__ import annotations

from asgi_correlation_id import correlation_id
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.error_codes import ErrorCode
from app.core.exceptions import AppException
from app.core.logging import get_logger
from app.core.response import error_response

logger = get_logger(__name__)


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        req_id = correlation_id.get() or ""

        logger.warning(
            "business exception occurred",
            extra={
                "event": "business_exception",
                "request_id": req_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": exc.status_code,
                "error_code": str(exc.code),
            },
        )

        resp = error_response(
            code=exc.code,
            message=exc.message,
            request_id=req_id,
            status_code=exc.status_code,
            data=exc.data,
        )
        resp.headers["X-Request-ID"] = req_id
        return resp

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        req_id = correlation_id.get() or ""

        logger.warning(
            "request validation failed",
            extra={
                "event": "validation_error",
                "request_id": req_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": 422,
                "error_code": str(ErrorCode.VALIDATION_ERROR),
            },
        )

        resp = error_response(
            code=ErrorCode.VALIDATION_ERROR,
            message="请求参数校验失败",
            request_id=req_id,
            status_code=422,
            data={"errors": exc.errors()},
        )
        resp.headers["X-Request-ID"] = req_id
        return resp

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        req_id = correlation_id.get() or ""

        status_map = {
            400: ErrorCode.BAD_REQUEST,
            401: ErrorCode.UNAUTHORIZED,
            403: ErrorCode.FORBIDDEN,
            404: ErrorCode.NOT_FOUND,
        }
        mapped_code = status_map.get(exc.status_code, ErrorCode.BAD_REQUEST)

        logger.warning(
            "http exception",
            extra={
                "event": "http_exception",
                "request_id": req_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": exc.status_code,
                "error_code": str(mapped_code),
            },
        )

        resp = error_response(
            code=mapped_code,
            message=str(exc.detail),
            request_id=req_id,
            status_code=exc.status_code,
        )
        resp.headers["X-Request-ID"] = req_id
        return resp

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        req_id = correlation_id.get() or ""

        logger.exception(
            "unhandled exception occurred",
            extra={
                "event": "unhandled_exception",
                "request_id": req_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": 500,
                "error_code": str(ErrorCode.INTERNAL_SERVER_ERROR),
            },
        )

        resp = error_response(
            code=ErrorCode.INTERNAL_SERVER_ERROR,
            message="服务器内部错误",
            request_id=req_id,
            status_code=500,
        )
        # 第二批关键点：500 也显式补上 X-Request-ID
        resp.headers["X-Request-ID"] = req_id
        return resp
