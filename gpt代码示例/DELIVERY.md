# 今日交付说明

## 今日 API 可用清单

| 路径 | 方法 | 状态 | 说明 |
|---|---|---|---|
| /health | GET | 可用 | 健康检查 |
| /api/v1/auth/login | POST | 可用 | 登录并返回 access token |
| /api/v1/auth/me | GET | 可用 | 获取当前用户信息 |
| /api/v1/stores | GET | 可用 | 获取当前用户可访问门店 |
| /api/v1/stores/{store_id}/dashboard/overview | GET | 可用 | 获取指定门店首页 KPI 概览 |

## 已实现

- FastAPI 项目基础目录结构
- 环境配置统一入口
- 统一成功/失败响应结构
- 错误码常量
- request_id 中间件与日志
- JWT access token 生成与解析
- 认证依赖与门店权限校验依赖
- 全局异常处理
- 用户/门店/概览 Mock 数据
- docs/openapi 可用
- curl 联调样例

## 未实现

- refresh token 真正签发与刷新
- 数据库持久化
- 数据采集 3 接口
- 告警 2 接口
- 写接口幂等控制真正启用

## 明天优先项

1. 数据采集 3 接口
2. 告警 2 接口
3. refresh token
4. PostgreSQL + SQLAlchemy
5. 测试补齐

## 已知限制

- 当前全部为内存 Mock 数据
- 服务重启后状态不会持久化
- refresh token 仅占位
- 未接入数据库与缓存
