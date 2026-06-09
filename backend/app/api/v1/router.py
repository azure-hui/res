from fastapi import APIRouter

from app.api.v1.endpoints import health
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.stores import router as stores_router
from app.api.v1.endpoints.dashboard import router as dashboard_router
from app.api.v1.endpoints.debug_auth import router as debug_auth_router
from app.api.v1.endpoints.debug_store import router as debug_store_router
from app.api.v1.endpoints.debug_whoami import router as debug_whoami_router

api_router = APIRouter()

api_router.include_router(health_router, tags=["system"])
api_router.include_router(health.router, tags=["health"])
api_router.include_router(auth_router)
api_router.include_router(stores_router)
api_router.include_router(dashboard_router)
api_router.include_router(debug_auth_router)
api_router.include_router(debug_store_router)
api_router.include_router(debug_whoami_router)
