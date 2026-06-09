# Day3 字段映射清单

## 目标
梳理接口字段、Schema 字段、数据库字段的一致性，为 Repository / Service 分层和接口稳定化做准备。


接口：GET /api/v1/stores
接口返回字段（data.items[]）	Schema 字段   DB 模型	DB 字段	  是否一致	   备注
id	                              id	      Store	     id	        是	       主键
name	                          name	      Store	     name	    是	       门店名称
city	                          city	      Store	     city	    是	       可空
is_active	                      is_active	  Store	     is_active	是	       启用状态
total（data.total）	              total     	-	       -	    是	       计算字段（items 长度）


接口：GET /api/v1/stores/{store_id}/dashboard/overview
接口返回字段（data）	Schema 字段	          DB 模型	           DB 字段/来源	        是否一致	备注
store_id	             store_id	          DashboardSnapshot	   store_id	               是	    门店ID
store_name	             store_name	          Store	               name	                   是	    来自 Store
business_date	         business_date	      DashboardSnapshot	   biz_date（映射）	       是	    命名映射
currency	             currency	            -	               常量 "CNY"	           是	    非 DB 字段
revenue_today	         revenue_today	      DashboardSnapshot	   revenue（映射）	       是	    Numeric 转 float
orders_today	         orders_today	      DashboardSnapshot	   order_count（映射）	   是	    命名映射
customers_today	         customers_today	  DashboardSnapshot	   customer_count（映射）  是	    命名映射
avg_order_value	         avg_order_value	    -	               计算：revenue/orders	   是	    订单为0时返回0.0
table_turnover_rate	     table_turnover_rate	-	               常量 0.0	               是	    占位字段
warning_count	         warning_count	        -	               常量 0	               是	    占位字段


统一响应结构（两接口通用）
字段	     说明
code	     业务码（成功=0）
message	     提示信息（成功=success）
data	     业务数据主体
request_id	 请求追踪ID
timestamp	 ISO8601 时间戳（含时区）

相关错误码（当前）
场景	             HTTP	code
未认证/无效token	 401	4010x
无门店权限	         403	40301
门店不存在或禁用	 404	40401
门店概览不存在       404	40402

