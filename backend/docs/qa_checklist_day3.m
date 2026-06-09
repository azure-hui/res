# Day3 最终验收清单

## 基本信息
- 项目名称：restaurant
- 阶段：Day3（数据层与接口稳定化）
- 验收日期：`YYYY-MM-DD`
- 验收人：`填写姓名`
- 分支：`填写分支名`
- 提交范围：`填写 commit / PR 链接或编号`

---

## 一、字段契约验收

### 1. /api/v1/stores
- [ ] 返回结构为统一响应结构
- [ ] `data.items[]` 字段固定为：
  - [ ] `id`
  - [ ] `name`
  - [ ] `city`
  - [ ] `is_active`
- [ ] 不再返回旧字段：
  - [ ] `status`
  - [ ] `address`
  - [ ] `code`
- [ ] `data.total` 存在且正确
- [ ] `data.page` 存在且正确
- [ ] `data.page_size` 存在且正确
- [ ] `data.sort_by` 存在且正确
- [ ] `data.sort_order` 存在且正确

### 2. 当前用户信息接口（如 /auth/me）
- [ ] 返回字段固定为：
  - [ ] `id`
  - [ ] `username`
  - [ ] `display_name`
  - [ ] `role`
  - [ ] `is_active`
- [ ] 不再返回旧字段：
  - [ ] `user_id`
  - [ ] `full_name`

### 3. /api/v1/stores/{store_id}/dashboard/overview
- [ ] 返回字段固定为：
  - [ ] `store_id`
  - [ ] `store_name`
  - [ ] `business_date`
  - [ ] `currency`
  - [ ] `revenue_today`
  - [ ] `orders_today`
  - [ ] `customers_today`
  - [ ] `avg_order_value`
  - [ ] `table_turnover_rate`
  - [ ] `warning_count`
- [ ] `business_date` 输出格式已统一
- [ ] `currency` 默认值已固定
- [ ] `table_turnover_rate` 默认值已固定
- [ ] `warning_count` 默认值已固定

---

## 二、分层验收（Repository / Service / Route）

### 1. Repository 层
- [ ] 已创建并使用 `store_repository.py`
- [ ] 已创建并使用 `dashboard_repository.py`
- [ ] Repository 只负责：
  - [ ] 查询
  - [ ] 过滤
  - [ ] 排序
  - [ ] 分页
  - [ ] join / scope 查询
- [ ] Repository 不负责 API 字段映射
- [ ] Repository 不负责统一响应外壳

### 2. Service 层
- [ ] `store_service` 已承接 stores 业务编排
- [ ] `store_service` 已固定 stores 输出字段
- [ ] `dashboard_service` 已承接 dashboard overview 业务编排
- [ ] `dashboard_service` 已处理默认值
- [ ] `dashboard_service` 已处理计算字段
- [ ] `dashboard_service` 已处理 API 字段映射

### 3. Route 层
- [ ] route 中不再直接写复杂查询逻辑
- [ ] route 中不再手动拼接 dashboard 返回字段
- [ ] route 中只保留：
  - [ ] 参数接收
  - [ ] 依赖注入
  - [ ] service 调用
  - [ ] 响应返回

---

## 三、/stores 分页 / 排序 / 过滤规范验收

### 1. 分页
- [ ] 支持 `page`
- [ ] 支持 `page_size`
- [ ] `page >= 1`
- [ ] `page_size` 已限制边界

### 2. 排序
- [ ] 支持 `sort_by`
- [ ] 支持 `sort_order`
- [ ] 排序字段已做白名单控制
- [ ] 非法排序字段已拦截或兜底

### 3. 过滤
- [ ] 支持 `keyword`
- [ ] 支持 `city`
- [ ] 支持 `is_active`

### 4. store scope
- [ ] owner 可查看全部门店
- [ ] 非 owner 仅可查看授权范围内门店
- [ ] `items` 与 `total` 都符合 scope 结果

---

## 四、dashboard 稳定化验收

### 1. 成功场景
- [ ] 门店存在
- [ ] 门店启用
- [ ] 当前用户有权限
- [ ] 有 snapshot 时返回 200
- [ ] 返回结构完整
- [ ] `avg_order_value` 计算正确

### 2. 错误语义
- [ ] 门店不存在 -> `40401`
- [ ] 门店禁用 -> `40401`
- [ ] 门店存在但无权限 -> `40301`
- [ ] 门店存在、有权限、但无 snapshot -> `40402`

### 3. 边界与默认值
- [ ] `orders_today = 0` 时 `avg_order_value = 0.0`
- [ ] 空值不会导致 500
- [ ] 默认值不会漂移

---

## 五、统一响应结构验收

### 1. 成功响应
- [ ] 包含 `code`
- [ ] 包含 `message`
- [ ] 包含 `data`
- [ ] 包含 `request_id`
- [ ] 包含 `timestamp`

### 2. 错误响应
- [ ] 401 为统一 JSON 结构
- [ ] 403 为统一 JSON 结构
- [ ] 404 为统一 JSON 结构
- [ ] 不出现 HTML 错误页
- [ ] 不出现纯文本 traceback
- [ ] 不出现非 JSON 错误体

---

## 六、测试与回归验收

### 1. stores
- [ ] owner 获取 stores 成功
- [ ] 非 owner 仅看到 scope 内门店
- [ ] 分页参数生效
- [ ] 排序参数生效
- [ ] 过滤参数生效
- [ ] item 字段契约正确
- [ ] total 与过滤条件一致

### 2. dashboard
- [ ] 正常返回 200
- [ ] 门店不存在 -> 40401
- [ ] 门店禁用 -> 40401
- [ ] 无权限 -> 40301
- [ ] 无 snapshot -> 40402
- [ ] `orders_today = 0` 时返回 `avg_order_value = 0.0`

### 3. auth
- [ ] 当前用户接口返回新字段契约
- [ ] 不再返回旧字段

### 4. 测试结果
- [ ] `pytest tests -q` 通过
- [ ] 关键接口无回归
- [ ] 无阻断性问题

---

## 七、文档验收

- [ ] 已更新 `docs/day3_field_mapping.md`
- [ ] 已更新 `docs/api_inventory.md`
- [ ] 已更新接口约定文档
- [ ] 已记录错误码与响应语义
- [ ] 已记录分页 / 排序 / 过滤规范

---

## 八、Day3 DoD（完成定义）
- [ ] 字段契约已锁定
- [ ] Repository / Service 分层已落地
- [ ] `/stores` 分页 / 排序 / 过滤规范已完成
- [ ] dashboard 200 / 403 / 404 行为一致
- [ ] `pytest tests -q` 通过
- [ ] 文档已同步
- [ ] 可进入 Day4