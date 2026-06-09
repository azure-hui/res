from fastapi import APIRouter

# 创建路由对象
router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}