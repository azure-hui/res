import { MetricCard } from "@/components/ui/metric-card";

export function AiSummary() {
  return (
    <section className="summary-grid">
      <MetricCard
        variant="orange"
        valueId="adviceCount"
        title="待处理建议"
        label="今日建议数"
        subLabel="接口待接入"
        footerButton="聚焦高优先级"
        miniStats={[
          { value: "--", label: "高优先级" },
          { value: "--", label: "待处理" },
          { value: "--", label: "已执行" },
        ]}
      />

      <MetricCard
        variant="green"
        title="今日优化空间"
        label="预计收益"
        subLabel="接口待接入"
        footerButton="查看收益型"
        ringSmall
        miniStats={[
          { value: "--", label: "客单价" },
          { value: "--", label: "浪费率" },
          { value: "--", label: "排队桌数" },
        ]}
      />
    </section>
  );
}
