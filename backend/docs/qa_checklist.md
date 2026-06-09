检查说明（验收版）

时间格式统一
目标：所有响应 timestamp 必须是 ISO8601 且带时区。
样例应类似：2026-03-28T07:34:05.260058+00:00
验证点：任意接口响应都包含 timestamp，并带 +00:00 或 +08:00。
统一响应结构
目标：成功/失败都必须包含：
code / message / data / request_id / timestamp
验证方法：/health、/auth/login、/auth/me、/stores、/stores/{id}/dashboard/overview 都检查结构一致。
错误码常量一致
目标：业务 code 与 HTTP 状态分离：
401 对应 40104/40105/40103/40102
403 对应 40301
422 对应 42200
验证方法：用测试或手动请求触发对应错误，看返回结构里 code。
异常处理统一
目标：所有异常走统一结构：
AppException（业务错误）
RequestValidationError（参数校验）
StarletteHTTPException（404 等）
Exception（兜底 500）
验证：做 4 次错误请求，看返回字段是否统一。
request_id 贯穿
目标：响应体里 request_id 必须存在；响应头里应有 X-Request-ID。
验证：对任意接口看响应头与响应体。
鉴权依赖生效
目标：无 token 和错 token 必须 401，合法 token 可访问 /me。
验证：
/api/v1/debug/whoami 不带 token -> 401
Authorization: abc -> 401
Authorization: Bearer <token> -> 200
门店权限生效
目标：manager 访问无权限门店 -> 403。
验证：
GET /api/v1/debug/stores/1001/access -> 200
GET /api/v1/debug/stores/1002/access -> 403
测试覆盖
执行：
pytest tests -q
目标：全部通过，至少覆盖：
登录成功/失败
whoami 鉴权
门店权限
422 校验失败
404 结构统一
token 过期