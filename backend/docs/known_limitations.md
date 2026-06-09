# 当前限制

- 数据为 Mock，未接数据库
- 无 refresh token
- 无权限模型/角色体系的完整管理界面
- 报表数据为演示用途，非真实计算

# Known Limitations

# Known Limitations

## 一、dashboard 当前为最小实现
当前 `dashboard overview` 仅接入以下字段：

- `biz_date`
- `revenue`
- `order_count`
- `customer_count`

尚未覆盖更复杂的业务指标，例如：
- 客单价
- 同比 / 环比
- 上座率
- 菜品分析
- 时段分析

---

## 二、权限模型为最小可用版
当前权限模型规则如下：

- `owner` 视为全局门店访问角色
- `manager` 依赖 `user_store_rel` 进行门店访问控制

当前尚未支持：
- 更细粒度菜单/按钮级权限
- 多角色叠加策略
- 店长/区域经理/总部分析员等更复杂角色矩阵

---

## 三、seed 数据仅用于本地开发联调
`seed_day2.py` 当前用途为：
- 本地开发
- Swagger / Postman 联调
- 测试环境最小数据注入

不建议直接用于：
- 生产环境初始化
- 正式用户管理

---

## 四、测试以集成测试为主
当前自动化测试重点覆盖：
- 登录
- 当前用户
- 门店权限
- dashboard forbidden

尚未完整覆盖：
- service 层单测
- repository / query 层单测
- seed 幂等性专项测试
- migration 回归测试

---

## 五、迁移文件仍需人工复核
Alembic 自动生成虽然已可用，但仍存在误判历史表删除的风险。

每次生成 migration 后，建议人工检查：
- 是否误删旧表
- 是否误删旧索引
- 是否误删旧约束