from pydantic import BaseModel, Field


class IdempotencyNote(BaseModel):
    header: str = Field(default="Idempotency-Key")
    status: str = Field(default="reserved")
    description: str = Field(default="幂等键规范已预留，今日版本仅文档占位，写接口暂未启用")
