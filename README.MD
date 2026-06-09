# 水果店会员管理系统

基于 FastAPI + Vue 3 的水果店会员管理系统，包含会员等级、积分兑换、预售活动、新鲜水果推荐等功能。项目按前后端模块化拆分，便于后续接入数据库、登录鉴权或门店收银系统。

## 功能模块

- 会员管理：会员列表、新增会员、等级与偏好分类维护。
- 会员等级：等级规则、最低积分、折扣与权益配置。
- 积分兑换：兑换商品列表、会员积分扣减、积分记录查询。
- 预售活动：活动发布、库存名额、会员预约。
- 新鲜水果推荐：按新鲜度和会员偏好生成推荐列表。
- 经营概览：汇总会员、预售、积分兑换和推荐数据。

## 项目结构

```text
.
├── backend
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   └── modules
│   │       ├── levels
│   │       ├── members
│   │       ├── points
│   │       ├── presales
│   │       └── recommendations
│   ├── Dockerfile
│   └── requirements.txt
├── frontend
│   ├── src
│   │   ├── api
│   │   ├── components
│   │   ├── router
│   │   ├── styles
│   │   └── views
│   ├── Dockerfile
│   ├── nginx.conf
│   └── package.json
└── docker-compose.yml
```

## Docker 启动

```bash
docker compose up --build
```

启动后访问：

- 前端：http://localhost:18073
- 后端健康检查：http://localhost:18000/health
- API 文档：http://localhost:18000/docs

## 本地开发

后端：

```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

前端：

```bash
cd frontend
npm install
npm run dev
```

本地 Vite 开发时如需直连后端，可创建 `frontend/.env`：

```text
VITE_API_BASE_URL=http://127.0.0.1:8000/api
```

## 主要接口

- `GET /api/members`：会员列表
- `POST /api/members`：新增会员
- `GET /api/levels`：等级列表
- `POST /api/levels`：新增等级
- `GET /api/points/rewards`：兑换商品
- `POST /api/points/redeem`：积分兑换
- `GET /api/presales`：预售活动
- `POST /api/presales/orders`：预约预售
- `GET /api/recommendations`：新鲜水果推荐

## 说明

当前版本使用内存数据存储，重启后会恢复为示例数据。生产环境可在 `backend/app/core/store.py` 之后替换为数据库仓储层。
