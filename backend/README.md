# Restaurant Analytics Backend MVP

## 项目简介
# Restaurant Analytics Backend

餐饮数字化运营支撑系统后端服务，基于 FastAPI + PostgreSQL + SQLAlchemy + Alembic。
当前已完成基础认证、健康检查、结构化日志、request_id 链路追踪、最小监控指标与基础 CI 门禁。

## 环境要求

- Python 3.12
- PostgreSQL 16/18
- Windows PowerShell 或 CMD
- 建议使用虚拟环境/conda 环境

## 关键目录

- `backend/app/`：后端主应用代码
- `backend/tests/`：测试用例
- `backend/alembic/`：数据库迁移
- `backend/scripts/`：本地启动与测试脚本
- `.github/workflows/`：CI 工作流 

## 本地启动

### 1. 克隆项目
```bash
git clone <your-repo-url>
cd restaurant-analytics/backend

---

## 3.2 创建并激活环境

你是 Windows 用户，所以 README 优先给 PowerShell / conda 版本。

### 如果你们常用 conda
```md id="gplm1x"
### 2. 创建并激活 Python 环境（conda 示例）
```bash
conda create -n restaurant-backend python=3.12 -y
conda activate restaurant-backend

### 安装依赖
```md id="2tv5fq"
### 3. 安装依赖
```bash
pip install -r requirements.txt
pip install ruff pyright

---

## 3.3 配置环境变量

```md id="lh92i9"
### 4. 配置环境变量
复制 `.env.example` 为 `.env`，并按本机数据库配置修改：

```bash
copy .env.example .env

如果你更想兼容 PowerShell，也可以补一句：

```powershell id="j53ypu"
Copy-Item .env.example .env
### 5. 创建数据库
先确保 PostgreSQL 已启动，然后创建数据库和用户，例如：

```sql
CREATE USER restaurant_user WITH PASSWORD 'your_password';
CREATE DATABASE restaurant_db;
GRANT ALL PRIVILEGES ON DATABASE restaurant_db TO restaurant_user;


如果你们现在默认已经手动创建好了，也可以写成“若本地尚未创建数据库，请执行”。

---

## 3.5 执行迁移

这块必须写清，不然新同学一启动就会报表不存在。

```md id="lm9j3a"
### 6. 执行数据库迁移
```bash
alembic upgrade head

---

## 3.6 启动服务

```md id="rwhvaj"
### 7. 启动服务
```bash
uvicorn app.main:app --reload

---

## 3.7 验证启动成功

这部分一定要写“看到什么算成功”。

```md id="sb6z9r"
### 8. 验证服务是否启动成功

打开浏览器访问：

- `http://127.0.0.1:8000/api/v1/health`
- `http://127.0.0.1:8000/metrics`

若返回健康检查结果和 Prometheus 指标文本，则说明启动成功。

## 测试与质量检查

### 运行单元测试
```bash
python -m pytest
运行代码规范检查
ruff check .
运行类型检查
pyright


---

# 第 5 步：README 里补“迁移命令”

这一段别只写 `upgrade head`，至少把最常用 3 条写出来：

```md id="x54b60"
## Alembic 迁移命令

### 执行最新迁移
```bash
alembic upgrade head
生成新迁移
alembic revision --autogenerate -m "your migration message"

回滚一步
alembic downgrade -1


---

# 第 6 步：README 里补“常见问题”

这一段很值钱，因为它最能体现“新同学 30 分钟跑通”。

建议至少补这 4 个。

---

## 6.1 数据库连接失败

```md id="4b2hyw"
## 常见问题

### 1. 数据库连接失败
请检查：

- PostgreSQL 服务是否已启动
- `.env` 中 `DATABASE_URL` 是否正确
- 数据库用户/密码是否与本机一致
- 数据库 `restaurant_db` 是否已创建

迁移失败或表不存在
### 2. 执行接口时报表不存在
说明数据库迁移尚未执行，请先运行：

```bash
alembic upgrade head

---

## 6.3 JWT 相关报错

```md id="lmj58c"
### 3. JWT 相关报错
请检查 `.env` 中以下配置是否存在：

- `JWT_SECRET_KEY`
- `JWT_ALGORITHM`
模块找不到或测试跑不起来
### 4. 本地测试无法运行
请先确认当前目录为 `backend/`，再执行：

```bash
python -m pytest

---

# 第 7 步：补最小 PowerShell 脚本

你是 Windows 环境，所以第五批很适合补两个 `.ps1` 脚本。  
不需要复杂，目标就是“少打命令”。

---

## 7.1 新建 `backend/scripts/run_local.ps1`

作用：
- 检查 `.env`
- 执行迁移
- 启动服务

先给你一版最小可用的：

```powershell id="roevpy"
Write-Host "==> Checking .env file..."
if (-Not (Test-Path ".env")) {
    Write-Host ".env not found. Please copy .env.example to .env first." -ForegroundColor Red
    exit 1
}

Write-Host "==> Running database migrations..."
alembic upgrade head
if ($LASTEXITCODE -ne 0) {
    Write-Host "Database migration failed." -ForegroundColor Red
    exit 1
}

Write-Host "==> Starting FastAPI server..."
uvicorn app.main:app --reload

## 常用脚本

### 一键本地启动
```powershell
.\scripts\run_local.ps1
一键执行质量检查
.\scripts\test.ps1

--- 