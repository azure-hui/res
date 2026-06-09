import { MetricCard } from "@/components/ui/metric-card";

export function TablesSummary() {
  return (
    <section className="summary-grid">
      <MetricCard
        variant="orange"
        title="接口待接入"
        label="桌台总览"
        subLabel="接口待接入"
        footerButton="查看布局"
        miniStats={[
          { value: "--", label: "平均翻台" },
          { value: "--", label: "桌待清台" },
        ]}
      />

      <MetricCard
        variant="blue"
        title="接口待接入"
        label="排队与预订"
        subLabel="接口待接入"
        footerButton="查看队列"
        ringSmall
        miniStats={[
          { value: "--", label: "组到店候位" },
          { value: "--", label: "单预约即将到店" },
        ]}
      />
    </section>
  );
}
