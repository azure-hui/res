# API 清单（MVP）

## 认证与健康检查
- `GET /api/v1/health` 健康检查
- `POST /api/v1/auth/login` 登录获取 access token
- `GET /api/v1/auth/me` 当前登录用户信息

## 门店与看板
- `GET /api/v1/stores` 获取当前用户可访问门店列表
- `GET /api/v1/stores/{store_id}/dashboard/overview` 门店看板概览

## 统一约定
- 认证：`Authorization: Bearer <access_token>`
- 响应结构：`code / message / data / request_id / timestamp`

#-------------------------------------------------------------------------------------------------#
接口                                         方法     状态    认证   说明
                                                    
/api/v1/health                                GET    可用    否    健康检查，返回 app/db 状态
                                             
/api/v1/auth/login                            POST    可用    否    用户登录，返回 access token

/api/v1/auth/me                               GET     可用    是    获取当前登录用户

/api/v1/stores                                GET     可用    是    获取当前用户可访问的门店

/api/v1/stores/{store_id}/dashboard/overview  GET     可用    是    获取指定门店 dashboard 概览
#-------------------------------------------------------------------------------------------------#
 
#-------------------------------------------------------------------------------------------------#
错误码表

错误码    HTTP状态       含义

40101     401       未登录、token 无效、用户名或密码错误        

40301     403       无权访问该门店

40401     404       门店不存在

#------------------------------------------------------------------------------------------------#

