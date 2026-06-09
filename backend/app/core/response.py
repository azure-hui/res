from typing import Any, Optional
from fastapi.responses import JSONResponse

from app.core.error_codes import ErrorCode
from app.core.time import now_iso


def success_response(
    data: Any = None,
    message: str = "success",
    request_id: Optional[str] = None,
    status_code: int = 200,
):
    return JSONResponse(
        status_code=status_code,
        content={
            "code": ErrorCode.SUCCESS,
            "message": message,
            "data": data,
            "request_id": request_id,
            "timestamp": now_iso(),
        },
    )


def error_response(
    code: str | int,
    message: str,
    request_id: Optional[str] = None,
    status_code: int = 400,
    data: Any = None,
):
    return JSONResponse(
        status_code=status_code,
        content={
            "code": code,
            "message": message,
            "data": data,
            "request_id": request_id,
            "timestamp": now_iso(),
        },
    )