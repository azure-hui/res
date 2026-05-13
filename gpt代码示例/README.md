# Restaurant FastAPI MVP

这是一个按“今日任务清单”落地的 FastAPI MVP 骨架：

- 可运行
- 可登录
- 可鉴权
- 可查门店
- 可查首页概览
- /docs 和 /openapi.json 可用
- 统一响应结构与错误结构
- 当前使用内存 Mock 数据，不接数据库

## 目录结构

```text
app/
  api/
  core/
  deps/
  infra/
  schemas/
  services/
  main.py
tests/
requirements.txt
.env.example
README.md
```

## 安装依赖

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
```

## 启动

```bash
copy .env.example .env
uvicorn app.main:app --reload
```

启动后可访问：

- Docs: http://127.0.0.1:8000/docs
- OpenAPI: http://127.0.0.1:8000/openapi.json
- Health: http://127.0.0.1:8000/health

## 已实现接口

| 方法 | 路径 | 说明 | 状态 |
|---|---|---|---|
| GET | /health | 健康检查 | 已实现 |
| POST | /api/v1/auth/login | 登录并获取 access token | 已实现 |
| GET | /api/v1/auth/me | 当前用户信息 | 已实现 |
| GET | /api/v1/stores | 当前用户可访问门店列表 | 已实现 |
| GET | /api/v1/stores/{store_id}/dashboard/overview | 首页 KPI 概览 | 已实现 |

## 未实现/占位

- refresh token：仅预留返回结构，未落地
- 数据持久化：当前全部是内存 Mock 数据
- 写接口幂等：仅预留 Idempotency-Key 文档规范，未启用
- 数据采集接口：未实现
- 告警接口：未实现

## Mock 账号

| 用户名 | 密码 | 角色 | 可访问门店 |
|---|---|---|---|
| owner_admin | owner123 | owner | store_001, store_002 |
| manager_beijing | manager123 | store_manager | store_001 |

## 统一返回结构

```json
{
  "code": "SUCCESS",
  "message": "ok",
  "data": {},
  "request_id": "uuid",
  "timestamp": "2026-03-26T08:00:00+00:00"
}
```

## 401 / 403 规则

### 401

- 缺少 Authorization
- Authorization 格式错误
- token 无效
- token 过期
- token 缺少 sub

### 403

- 用户已登录，但无权访问对应 store_id

## 调试样例

### 1. 登录

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"owner_admin\",\"password\":\"owner123\"}"
```

### 2. 获取当前用户

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/auth/me" \
  -H "Authorization: Bearer <your_access_token>"
```

### 3. 查询门店列表

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/stores" \
  -H "Authorization: Bearer <your_access_token>"
```

### 4. 查询门店首页概览

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/stores/store_001/dashboard/overview" \
  -H "Authorization: Bearer <your_access_token>"
```

### 5. 越权场景（门店经理访问 store_002）

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"manager_beijing\",\"password\":\"manager123\"}"
```

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/stores/store_002/dashboard/overview" \
  -H "Authorization: Bearer <manager_token>"
```

## 明日优先项

1. 数据采集 3 接口
2. 告警 2 接口
3. refresh token 落地
4. PostgreSQL + SQLAlchemy 接入
5. 基础单元测试与集成测试补齐
