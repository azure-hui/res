from __future__ import annotations

from contextlib import asynccontextmanager

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.handlers import register_exception_handlers
from app.core.logging import setup_logging
from app.db.session import ping_db
from app.middleware.logging_middleware import LoggingMiddleware
from app.monitoring.metrics import setup_metrics


def create_app() -> FastAPI:
    setup_logging()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        _ = ping_db()
        yield

    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        docs_url="/docs",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    # 顺序关键：先加 Logging（内层），后加 CorrelationId（外层）
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(
        CorrelationIdMiddleware,
        header_name="X-Request-ID",
    )

    # 如果你已有 allow_origins，请替换为你原来的列表，仅补 X-Request-ID 相关项
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
        expose_headers=["X-Request-ID"],
    )

    register_exception_handlers(app)
    app.include_router(api_router, prefix=settings.api_v1_prefix)
    setup_metrics(app)


    @app.get("/", include_in_schema=False)
    async def root():
        return {
            "app": settings.app_name,
            "env": settings.app_env,
            "docs": "/docs",
        }

    return app


app = create_app()
