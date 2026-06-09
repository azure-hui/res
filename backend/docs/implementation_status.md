# 实现状态

## 已完成
1. `GET /api/v1/health`
2. `POST /api/v1/auth/login`
3. `GET /api/v1/auth/me`
4. `GET /api/v1/stores`
5. `GET /api/v1/stores/{store_id}/dashboard/overview`
6. 统一响应结构（`code/message/data/request_id/timestamp`）
7. Bearer Token 鉴权与门店权限校验

## 待完成
- 数据库持久化与迁移
- Refresh Token
- 实时事件与告警链路
- 报表/图表更多维度与指标

# Day2 交付报告

## 一、交付概述

Day2 目标是完成后端从基础数据库接入到核心认证、门店权限、最小业务数据联通的落地，使系统从“可启动 + Mock 接口”推进到“可迁移 + 可鉴权 + 可按权限访问真实数据”。

本次交付完成了以下核心内容：

- 建立数据库基础层
- 建立核心业务模型并完成首轮迁移
- 将登录链路切换到数据库
- 将门店权限链路切换到数据库
- 提供最小可用 seed 数据
- 完成关键接口自动化测试
- 完成联调所需文档同步

---

## 二、本次交付范围

### 1. 数据库基础层
已完成：
- `backend/app/db/session.py`
- `backend/app/db/base.py`
- 数据库会话依赖 `get_db`
- 数据库健康检查 `ping_db`

结果：
- 服务启动时可正常加载数据库配置
- `GET /api/v1/health` 可返回应用状态与数据库状态

---

### 2. 核心模型
已完成以下核心模型定义：

- `backend/app/models/user.py`
- `backend/app/models/store.py`
- `backend/app/models/user_store_rel.py`
- `backend/app/models/dashboard_snapshot.py`

对应核心表：

- `users`
- `stores`
- `user_store_rel`
- `dashboard_snapshots`

结果：
- 4 张核心表已纳入统一 `Base.metadata`
- 可被 Alembic 正常扫描

---

### 3. Alembic 首迁移
已完成：
- Alembic `env.py` 接入项目配置
- 自动生成首轮迁移脚本
- 执行 `alembic upgrade head`

结果：
- 核心表已成功落库
- 服务在迁移完成后可正常启动

---

### 4. 认证链路切 DB
已完成：
- `POST /api/v1/auth/login` 从数据库查询用户并校验密码
- `GET /api/v1/auth/me` 通过 token 解码后从数据库回查用户

结果：
- 登录接口已脱离 Mock
- `/auth/me` 已脱离 Mock
- 错误密码返回统一错误码 `40101`
- 统一响应结构保持不变

---

### 5. 门店权限切 DB
已完成：
- `backend/app/deps/permissions.py`
- `GET /api/v1/stores` 按用户权限返回门店
- `GET /api/v1/stores/{store_id}/dashboard/overview` 接入 `require_store_access`

结果：
- owner 用户可访问全部门店
- manager 用户仅可访问授权门店
- 未授权访问返回统一错误码 `40301`

---

### 6. 数据初始化
已完成：
- `backend/app/scripts/seed_day2.py`

最小测试数据包括：
- 2 个用户
- 2 个门店
- 用户与门店权限关系
- 1 条 dashboard snapshot

联调账号：
- `owner_admin / owner123`
- `manager_beijing / manager123`

结果：
- 重复执行 seed 不会因唯一约束报错
- 关键接口可进行本地联调与手工验证

---

### 7. 自动化测试
已完成测试文件：
- `backend/tests/test_api_flow.py`
- `backend/tests/test_auth_dependency.py`
- `backend/tests/test_store_permission.py`

测试结果：
- `pytest tests -q` 通过
- 当前结果：`18 passed`

覆盖范围包括：
- 登录成功
- 错密返回 `40101`
- `/auth/me` 未登录 / 无效 token / 正常访问
- `/stores` 权限范围
- dashboard 无权限访问返回 `40301`

---

## 三、当前已可用正式接口

### 1. 健康检查
- `GET /api/v1/health`

说明：
- 返回应用状态
- 返回数据库状态

---

### 2. 登录
- `POST /api/v1/auth/login`

说明：
- 使用数据库用户进行认证
- 成功返回 access token
- 失败返回 `40101`

---

### 3. 当前用户
- `GET /api/v1/auth/me`

说明：
- 需要 Bearer Token
- 通过 token + DB 回查当前用户

---

### 4. 门店列表
- `GET /api/v1/stores`

说明：
- 需要 Bearer Token
- 按当前用户权限返回可访问门店

---

### 5. 门店 dashboard 概览
- `GET /api/v1/stores/{store_id}/dashboard/overview`

说明：
- 需要 Bearer Token
- 校验门店访问权限
- 无权限返回 `40301`

---

## 四、已脱离 Mock 的接口

本阶段已明确脱离 Mock 的接口包括：

- `POST /api/v1/auth/login`
- `GET /api/v1/auth/me`
- `GET /api/v1/stores`
- `GET /api/v1/stores/{store_id}/dashboard/overview`（最小数据版）

说明：
其中至少 3 个正式接口已脱离 Mock，满足 Day2 DoD 要求。

---

## 五、Day2 验收结果

### DoD 验收项

- [x] `alembic upgrade head` 成功
- [x] 5 个正式接口可用
- [x] 至少 3 个接口已脱离 Mock
- [x] 鉴权与门店权限无回归
- [x] `pytest tests -q` 全绿
- [ ] 文档完成并可交接

> 如果你 5 份文档已经都补齐，这里最后一项也可以改成 `[x]`

---

## 六、重点联调说明

### 测试账号

#### 账号 1：Owner
- 用户名：`owner_admin`
- 密码：`owner123`

能力：
- 可查看全部门店
- 可访问全部门店 dashboard

#### 账号 2：Manager
- 用户名：`manager_beijing`
- 密码：`manager123`

能力：
- 仅可查看门店 `1001`
- 访问 `1002` 时返回 `40301`

---

### 关键联调路径

推荐联调顺序：

1. `GET /api/v1/health`
2. `POST /api/v1/auth/login`
3. `GET /api/v1/auth/me`
4. `GET /api/v1/stores`
5. `GET /api/v1/stores/1001/dashboard/overview`

权限验证补充：
- 使用 `manager_beijing` 访问 `GET /api/v1/stores/1002/dashboard/overview`
- 预期返回 `40301`

---

## 七、风险与注意事项

### 1. 历史 migration 风险
在自动生成迁移时，曾检测到历史表删除提示，例如：
- `orders`
- `occupancy_logs`

交付前需确认：
- migration 文件中不存在误删仍需保留的旧表操作
- 若旧表后续仍需使用，应移除对应 `drop_table(...)`

---

### 2. 当前 dashboard 为最小数据版
当前 dashboard 仅接入最小字段：
- `biz_date`
- `revenue`
- `order_count`
- `customer_count`

如前端已有更多指标字段依赖，需在后续阶段继续补齐。

---

## 八、后续建议

建议 Day3 优先推进以下方向：

1. 扩展 dashboard 指标体系
2. 完善权限模型与角色能力矩阵
3. 补充分页、筛选、schema 校验
4. 继续替换剩余 Mock
5. 增加更细粒度单元测试
6. 完善接口示例与联调说明

day4
1. Day4 认证安全增强主链路已打通：
   - 登录双 token：已完成
   - refresh 闭环：已完成
   - 401 错误码收口：已完成主要分支，40101 / 40103 仍建议补最终验证
   - 权限依赖增强：已完成样板接口接入
   - 登录安全增强：已完成基础实现，锁定链路建议补最终验证
   - 审计日志：已完成基础落库
   - 测试结果：主链路手工验证通过，自动化测试待进一步补齐

2. 当前已完成的关键验证：
   - 登录成功返回 access_token + refresh_token
   - /api/v1/stores 鉴权通过
   - /api/v1/stores/{store_id}/dashboard/overview 鉴权通过
   - 非法 token 返回 40102，不再出现 500
   - 用户名不存在与密码错误场景不再崩溃
   - 登录响应已补齐统一返回结构

3. 遗留收尾项：
   - 补测 40101（缺少 token）
   - 补测 40103（过期 token）
   - 补测 40111（账号锁定）
   - 补测 40302 / 40301 权限拒绝分支
   - 视情况补齐 pytest 自动化测试记录

4. 结论：
   Day4 已达到“有条件通过”状态。主链路已具备进入下一阶段的基础，建议在进入 Day5 前完成剩余错误分支与权限拒绝分支的最终验收。