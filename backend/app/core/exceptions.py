class AppException(Exception):
    def __init__(self, code: str | int, message: str, status_code: int = 400, data=None):
        self.code = code
        self.message = message
        self.status_code = status_code
        self.data = data
        super().__init__(message)