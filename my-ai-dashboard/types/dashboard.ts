export type DashboardOverview = {
  store_id: number;
  store_name: string;
  business_date: string;
  currency: string;
  revenue_today: number;
  orders_today: number;
  customers_today: number;
  avg_order_value: number;
  table_turnover_rate: number;
  warning_count: number;
};

export type MetricMiniStat = {
  value?: string | number | null;
  label: string;
};

export type OverviewMetricCardData = {
  value?: string | number | null;
  valueId?: string;
  label: string;
  title: string;
  subLabel?: string;
  footerButton: string;
  miniStats: MetricMiniStat[];
};

export type OperationProgressMetric = {
  label: string;
  value?: string | number | null;
  tone?: "default" | "green" | "blue" | "purple";
};

export type OrderChannel = "all" | "dine_in" | "takeaway" | "pickup";

export type OrderTableItem = {
  id: string;
  channel: string;
  target: string;
  amount: string | number;
  status: string;
  time: string;
};

export type OrderBoardColumn = {
  title: string;
  items: Array<{
    id: string;
    title: string;
    description?: string;
    badge?: string;
  }>;
};

export type TableAreaFilter = "all" | "hall_a" | "private_room";

export type TableQueueItem = {
  id: string;
  type: "waiting" | "reservation";
  title: string;
  subtitle?: string;
  badge?: string;
};

export type TableEfficiencyMetric = {
  label: string;
  value?: string | number | null;
  tone?: "default" | "blue" | "green" | "purple";
};

export type DishRankingMode = "销量" | "毛利" | "好评率";

export type DishRankingItem = {
  id: string;
  name: string;
  category: string;
  sales: string | number;
  revenue: string | number;
  margin: string | number;
  rating: string | number;
};

export type CategoryPerformanceMetric = {
  label: string;
  value: string;
  tone?: "default" | "purple" | "blue" | "green";
};

export type DishRiskItem = {
  id: string;
  title: string;
  description?: string;
  level?: "info" | "warn" | "danger";
};

export type AdviceFilterKey =
  | "all"
  | "high"
  | "tables"
  | "inventory"
  | "dishes"
  | "service";

export type AdviceStatusFilterKey =
  | "all"
  | "pending"
  | "executing"
  | "done"
  | "ignored";

export type AdviceCardItem = {
  id: string;
  title: string;
  time: string;
  desc: string;
  priority: string;
  type: string;
  status: string;
};

export type AdviceEvidenceItem = {
  id: string;
  title: string;
  desc: string;
  badge?: string;
};

export type AdviceRecordItem = {
  id: string;
  title: string;
  note: string;
  status: string;
};

export type DeviceCategory = "全部" | "摄像头" | "收银设备" | "厨房设备";

export type DeviceListItem = {
  id: string;
  name: string;
  location: string;
  type: string;
  status: string;
  lastHeartbeat: string;
  remark: string;
};

export type DeviceResourceMetric = {
  label: string;
  value: string;
  tone?: "default" | "blue" | "purple" | "green";
};

export type DeviceAlertItem = {
  id: string;
  title: string;
  description?: string;
  level?: "info" | "warn" | "danger";
};

export type DeviceMaintenanceItem = {
  id: string;
  title: string;
  description?: string;
  status?: string;
};

export type InventoryCategory =
  | "全部分类"
  | "食材"
  | "饮品"
  | "耗材";

export type InventoryProgressMetric = {
  label: string;
  value: string;
  tone?: "default" | "blue" | "green" | "purple";
};

export type PurchasePlanItem = {
  id: string;
  supplier: string;
  eta: string;
  amount: string | number;
  status: string;
  remark: string;
};

export type InventoryAlertItem = {
  id: string;
  title: string;
  description?: string;
  level?: "info" | "warn" | "danger";
};

export type MemberSegmentKey =
  | "普通会员"
  | "活跃会员"
  | "高价值会员"
  | "沉默会员";

export type MemberSummaryMetric = {
  value: string | number;
  label: string;
  title: string;
  topRightLabel: string;
  buttonLabel: string;
  miniStats: Array<{
    value: string | number;
    label: string;
  }>;
};

export type MemberSegmentMetric = {
  key: MemberSegmentKey;
  value: string | number;
};

export type MemberTaskItem = {
  id: string;
  title: string;
  description?: string;
  level?: "info" | "warn" | "danger";
};

export type MemberCampaignStatus = "全部活动" | "进行中" | "待开始" | "已结束";

export type MemberCampaignItem = {
  id: string;
  name: string;
  audience: string;
  startTime: string;
  endTime: string;
  status: string;
  result: string;
};