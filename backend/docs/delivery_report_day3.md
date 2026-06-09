# Day3 交付报告

## 1. 基本信息

- 项目名称：restaurant
- 开发阶段：Day3（数据层与接口稳定化）
- 开发日期：`YYYY-MM-DD`
- 分支名称：`填写分支名`
- 开发人：`填写姓名`
- 验收人：`填写姓名`
- 关联任务：`填写任务单 / issue / 看板链接`

---

## 2. 今日目标

根据 Day3 任务清单，今日目标如下：

1. 梳理现有 schema 与接口字段对齐，输出字段映射清单
2. 补齐 Repository / Service 分层，完成查询逻辑下沉
3. 统一 `/stores` 分页 / 排序 / 过滤规范
4. 稳定 dashboard 概览查询的空数据、异常与边界行为
5. 补测试并完成回归，确保关键接口无回归

---

## 3. 本次交付范围

### 3.1 Schema / 字段契约
- `backend/app/schemas/store.py`
- `backend/app/schemas/auth.py`
- `backend/app/schemas/dashboard.py`

### 3.2 Repository / Service
- `backend/app/repositories/store_repository.py`
- `backend/app/repositories/dashboard_repository.py`
- `backend/app/services/store_service.py`
- `backend/app/services/auth_service.py`
- `backend/app/services/dashboard_service.py`

### 3.3 API / 权限 / 错误处理
- `backend/app/api/v1/endpoints/stores.py`
- `backend/app/api/v1/endpoints/dashboard.py`
- `backend/app/deps/permissions.py`
- `backend/app/core/error_codes.py`
- `backend/app/core/handlers.py`

### 3.4 测试 / 文档
- `backend/tests/test_health.py`
- `backend/tests/test_mock_services.py`
- `backend/tests/test_api_flow.py`
- `docs/day3_field_mapping.md`
- `docs/api_inventory.md`
- `docs/api_conventions.md`

---

## 4. 本次完成内容

### 4.1 字段契约收口
本次已完成 stores、auth、dashboard 三类核心接口字段契约收口。

#### stores
- 对外字段固定为：`id / name / city / is_active`
- 已移除旧字段：`status / address / code`
- 已明确列表返回结构：`data.items / data.total / data.page / data.page_size / data.sort_by / data.sort_order`

#### auth
- 当前用户字段固定为：`id / username / display_name / role / is_active`
- 已移除旧字段：`user_id / full_name`

#### dashboard overview
- 对外字段固定为：
  - `store_id`
  - `store_name`
  - `business_date`
  - `currency`
  - `revenue_today`
  - `orders_today`
  - `customers_today`
  - `avg_order_value`
  - `table_turnover_rate`
  - `warning_count`
- 已明确 API 字段与 DB 字段映射关系
- 已明确默认值字段与计算字段来源

---

### 4.2 Repository / Service 分层落地
已将原本位于 route 中的主要查询逻辑下沉到 Repository / Service 层。

#### Repository 层职责
- 负责查询、过滤、排序、分页、scope、join
- 不负责接口字段映射
- 不负责统一响应结构

#### Service 层职责
- 负责业务编排
- 负责 DB -> API 字段映射
- 负责默认值处理
- 负责计算字段处理

#### Route 层结果
- route 逻辑已显著收敛
- endpoint 仅保留参数接收、依赖注入、service 调用和统一响应返回

---

### 4.3 `/stores` 分页 / 排序 / 过滤规范统一
本次已统一 `/stores` 查询规范，支持以下参数：

- `page`
- `page_size`
- `sort_by`
- `sort_order`
- `keyword`
- `city`
- `is_active`

返回结构已固定为：

- `data.items`
- `data.total`
- `data.page`
- `data.page_size`
- `data.sort_by`
- `data.sort_order`

同时已完成 store scope 控制：

- owner 可查看全部门店
- 非 owner 仅可查看授权范围内门店

---

### 4.4 dashboard 概览稳定化
本次已统一 dashboard overview 的成功 / 失败语义：

- 门店不存在 -> `40401`
- 门店禁用 -> `40401`
- 门店存在但无权限 -> `40301`
- 门店存在、有权限、但无 snapshot -> `40402`
- 正常返回 -> `200`

同时已处理以下边界：

- `business_date` 输出格式统一
- `orders_today = 0` 时，`avg_order_value = 0.0`
- `currency` 固定默认值
- `table_turnover_rate`、`warning_count` 固定占位值
- 空值场景不会触发 500

---

### 4.5 测试与回归
本次已完成关键接口测试与回归验证，覆盖：

#### stores
- owner 获取 stores
- 非 owner scope 控制
- 分页 / 排序 / 过滤
- 返回字段契约

#### dashboard
- 正常返回
- 门店不存在
- 门店禁用
- 无权限
- 无 snapshot
- `avg_order_value` 边界处理

#### auth
- 当前用户字段契约

测试结果：

- `pytest tests -q`：`填写结果`
- 关键接口：`通过 / 未通过`
- 回归问题：`无 / 有（填写说明）`

---

## 5. 产出文档

本次已更新 / 新增文档如下：

- `docs/day3_field_mapping.md`
- `docs/api_inventory.md`
- `docs/api_conventions.md`
- `docs/implementation_status.md`
- `docs/qa_checklist.md`

如有补充：
- `填写其他文档名`

---

## 6. 验收结果

### 6.1 验收结论
- [ ] 通过
- [ ] 有条件通过
- [ ] 不通过

### 6.2 验收说明
`填写验收结论说明`

---

## 7. 已知问题 / 风险

### 当前已知问题
1. `填写问题 1`
2. `填写问题 2`
3. `填写问题 3`

### 风险说明
- `填写风险说明`
- `填写影响范围`
- `填写规避建议`

如无：
- 当前无阻断性已知问题

---

## 8. 后续建议（Day4 输入）

建议 Day4 优先推进以下内容：

1. `填写 Day4 方向 1`
2. `填写 Day4 方向 2`
3. `填写 Day4 方向 3`

可选示例：
- 补充更多接口的统一分页规范
- 扩展 dashboard 数据来源
- 完善错误码体系
- 增强集成测试与测试夹具
- 推进接口文档与前后端联调

---

## 9. 附录

### 9.1 关键接口清单
- `GET /api/v1/stores`
- `GET /api/v1/stores/{store_id}/dashboard/overview`
- `GET /api/v1/auth/me`（如有）

### 9.2 关键错误码
- `40301`：门店存在但无权限
- `40401`：门店不存在或禁用
- `40402`：门店概览不存在

### 9.3 关键测试命令
```bash
pytest tests -q