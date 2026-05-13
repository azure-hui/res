from typing import Any, Generic, TypeVar
from pydantic import BaseModel, Field
from app.core.constants import ErrorCode
from app.infra.time import isoformat_utc

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    code: str = Field(default=ErrorCode.SUCCESS.value)
    message: str = Field(default="ok")
    data: T | None = None
    request_id: str
    timestamp: str = Field(default_factory=isoformat_utc)


def success_response(data: Any, request_id: str, message: str = "ok") -> dict[str, Any]:
    return APIResponse[Any](
        code=ErrorCode.SUCCESS.value,
        message=message,
        data=data,
        request_id=request_id,
    ).model_dump()


def error_response(code: ErrorCode, message: str, request_id: str, data: Any = None) -> dict[str, Any]:
    return APIResponse[Any](
        code=code.value,
        message=message,
        data=data,
        request_id=request_id,
    ).model_dump()
