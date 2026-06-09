from __future__ import annotations

import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from asgi_correlation_id import correlation_id

from app.core.logging import get_logger

logger = get_logger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()

        client_ip = request.client.host if request.client else None
        method = request.method
        path = request.url.path
        req_id = correlation_id.get()

        logger.info(
            "request started",
            extra={
                "event": "request_started",
                "request_id": req_id,
                "method": method,
                "path": path,
                "client_ip": client_ip,
            },
        )

        response = await call_next(request)

        duration_ms = round((time.perf_counter() - start) * 1000, 2)

        logger.info(
            "request finished",
            extra={
                "event": "request_finished",
                "request_id": correlation_id.get(),
                "method": method,
                "path": path,
                "status_code": response.status_code,
                "duration_ms": duration_ms,
                "client_ip": client_ip,
            },
        )

        return response
