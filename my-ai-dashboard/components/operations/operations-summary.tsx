import { MetricCard } from "@/components/ui/metric-card";

export function OperationsSummary() {
  return (
    <section className="summary-grid">
      <MetricCard
        variant="green"
        title="桌台使用情况"
        label="桌台总数"
        subLabel="接口待接入"
        footerButton="桌态详情"
        miniStats={[
          { value: "--", label: "利用率" },
          { value: "--", label: "平均翻台" },
        ]}
      />

      <MetricCard
        variant="blue"
        title="接口待接入"
        label="等位状态"
        subLabel="接口待接入"
        footerButton="排队详情"
        ringSmall
        miniStats={[
          { value: "--", label: "组 2 人" },
          { value: "--", label: "组 4 人" },
          { value: "--", label: "组 6 人" },
        ]}
      />
    </section>
  );
}
