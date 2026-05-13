from fastapi import status
from app.core.constants import ErrorCode


class AppException(Exception):
    def __init__(
        self,
        *,
        status_code: int,
        code: ErrorCode,
        message: str,
        data: dict | None = None,
    ) -> None:
        self.status_code = status_code
        self.code = code
        self.message = message
        self.data = data
        super().__init__(message)


class UnauthorizedException(AppException):
    def __init__(self, message: str = "认证失败") -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            code=ErrorCode.UNAUTHORIZED,
            message=message,
        )


class ForbiddenException(AppException):
    def __init__(self, message: str = "无权限访问") -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            code=ErrorCode.FORBIDDEN,
            message=message,
        )


class NotFoundException(AppException):
    def __init__(self, message: str = "资源不存在") -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            code=ErrorCode.NOT_FOUND,
            message=message,
        )
