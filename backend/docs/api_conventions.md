# API 统一约定

## 1. 响应结构
所有接口统一返回：
- `code`
- `message`
- `data`
- `request_id`
- `timestamp`

## 2. 时间格式
统一使用 ISO8601，带时区，例如：
`2026-03-28T07:34:05.260058+00:00`

## 3. 认证方式
使用 Bearer Token：
`Authorization: Bearer <access_token>`

## 4. 幂等键规范（预留）
写接口（POST/PUT/PATCH/DELETE）建议支持：
`Idempotency-Key: <uuid>`

约定：
- 同一业务动作重复提交时，客户端复用同一 `Idempotency-Key`
- 服务端后续会基于该键避免重复创建或重复扣减
- 当前 MVP 阶段仅文档保留，不做服务端校验
