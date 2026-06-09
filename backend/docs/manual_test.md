curl调试样例

10.1 登录
curl -X POST "http://127.0.0.1:8000/api/v1/auth/login" ^
  -H "Content-Type: application/json" ^
  -d "{\"username\":\"owner_admin\",\"password\":\"owner123\"}"
10.2 获取当前用户
curl "http://127.0.0.1:8000/api/v1/auth/me" ^
  -H "Authorization: Bearer YOUR_TOKEN"
10.3 获取门店列表
curl "http://127.0.0.1:8000/api/v1/stores" ^
  -H "Authorization: Bearer YOUR_TOKEN"
10.4 获取首页概览
curl "http://127.0.0.1:8000/api/v1/stores/1001/dashboard/overview" ^
  -H "Authorization: Bearer YOUR_TOKEN"
10.5 验证无 token
curl "http://127.0.0.1:8000/api/v1/auth/me"

预期：401。

10.6 验证越权门店
curl "http://127.0.0.1:8000/api/v1/stores/1002/dashboard/overview" ^
  -H "Authorization: Bearer MANAGER_BEIJING_TOKEN"

预期：403。

## 联调前自查清单

- [ ] 服务可启动：uvicorn app.main:app --reload
- [ ] /docs 可打开
- [ ] /openapi.json 可打开
- [ ] /api/v1/health 正常
- [ ] /api/v1/auth/login 可返回 access_token
- [ ] Swagger Authorize 可用
- [ ] /api/v1/auth/me 可返回当前用户
- [ ] /api/v1/stores 可返回可访问门店
- [ ] /api/v1/stores/{store_id}/dashboard/overview 可返回 KPI
- [ ] 无 token 返回 401
- [ ] 过期 token 返回 401
- [ ] 越权门店返回 403
- [ ] 所有响应包含 code/message/data/request_id/timestamp