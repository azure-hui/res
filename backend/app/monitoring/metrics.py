# backend/app/monitoring/metrics.py
from __future__ import annotations

from prometheus_client import Counter
from prometheus_fastapi_instrumentator import Instrumentator


AUTH_FAILURES_TOTAL = Counter(
    "auth_failures_total",
    "Total number of authentication failures",
    ["reason"],
)


def setup_metrics(app) -> None:
    instrumentator = Instrumentator(
        should_group_status_codes=True,
        excluded_handlers=[
            "/metrics",
            "/docs",
            "/openapi.json",
            "/redoc",
        ],
    )

    instrumentator.instrument(app).expose(
        app,
        include_in_schema=False,
        should_gzip=True,
    )


def inc_auth_failure(reason: str) -> None:
    AUTH_FAILURES_TOTAL.labels(reason=reason).inc()