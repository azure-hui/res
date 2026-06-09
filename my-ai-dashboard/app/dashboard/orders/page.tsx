import { MetricCard } from "@/components/ui/metric-card";
import { PageHeader } from "@/components/ui/page-header";
import { OrdersSummaryCards, OrdersMetricsCard } from "@/components/orders/orders-metrics";
import { OrdersTableSection } from "@/components/orders/orders-table";
import { OrderAlerts } from "@/components/orders/order-alerts";

export default function OrdersPage() {
  return (
    <section className="page active" data-page="orders">
      <PageHeader
        title="订单中心"
        description="统一查看堂食、外卖、自提订单状态与异常处理"
        actions={[
          { label: "导出订单" },
          { label: "手动录入订单", primary: true },
        ]}
      />

      <OrdersSummaryCards />

      <OrdersTableSection />

      <section className="two-col">
        <OrdersMetricsCard />
        <OrderAlerts />
      </section>
    </section>
  );
}
