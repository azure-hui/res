export const storeOpsPageContract = {
  summary: "/api/store-ops/summary",
  tableMap: "/api/store-ops/tables",
  queue: "/api/store-ops/queue",
  staffSchedule: "/api/store-ops/staff-schedule",
  efficiency: "/api/store-ops/efficiency",
} as const;

export const ordersPageContract = {
  summary: "/api/orders/summary",
  list: "/api/orders",
  board: "/api/orders/board",
  metrics: "/api/orders/metrics",
  alerts: "/api/orders/alerts",
} as const;

export const tablesPageContract = {
  summary: "/api/tables/summary",
  layout: "/api/tables/layout",
  efficiency: "/api/tables/efficiency",
  queue: "/api/tables/queue",
  advice: "/api/tables/advice",
} as const;

export const dishesPageContract = {
  summary: "/api/dishes/summary",
  ranking: "/api/dishes/ranking",
  categoryPerformance: "/api/dishes/category-performance",
  strategy: "/api/dishes/strategy",
  stockRisk: "/api/dishes/stock-risk",
} as const;

export const aiInsightsPageContract = {
  summary: "/api/ai-insights/summary",
  kpis: "/api/ai-insights/kpis",
  filters: "/api/ai-insights/filters",
  list: "/api/ai-insights/list",
  detail: "/api/ai-insights/detail",
  evidence: "/api/ai-insights/evidence",
  records: "/api/ai-insights/records",
} as const;

export const devicesPageContract = {
  summary: "/api/devices/summary",
  list: "/api/devices",
  resources: "/api/devices/resources",
  alerts: "/api/devices/alerts",
  maintenance: "/api/devices/maintenance",
} as const;

export const inventoryPageContract = {
  summary: "/api/inventory/summary",
  categories: "/api/inventory/categories",
  alerts: "/api/inventory/alerts",
  purchasePlans: "/api/inventory/purchase-plans",
} as const;

export const membersPageContract = {
  summary: "/api/members/summary",
  segmentation: "/api/members/segmentation",
  tasks: "/api/members/tasks",
  campaigns: "/api/members/campaigns",
} as const;

export const settingsPageContract = {
  storeProfile: "/api/settings/store-profile",
  notifications: "/api/settings/notifications",
  roles: "/api/settings/roles",
  preferences: "/api/settings/preferences",
} as const;