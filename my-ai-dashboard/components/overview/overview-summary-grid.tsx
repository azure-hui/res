import { MetricCard } from "@/components/ui/metric-card";

export function OverviewSummaryGrid() {
  return (
    <section className="summary-grid">
      <MetricCard
        variant="orange"
        title="门店营业额"
        label="今日经营额"
        valueId="revenueNumber"
        footerButton="查看详情"
        miniStats={[
          { label: "订单" },
          { label: "到店" },
          { label: "客单价" },
        ]}
      />

      <MetricCard
        variant="purple"
        title="当前在店人数"
        label="门店实时状态"
        valueId="liveNumber"
        ringSmall
        footerButton="查看桌态"
        miniStats={[
          { label: "空桌" },
          { label: "占用" },
          { label: "排队" },
        ]}
      />
    </section>
  );
}
