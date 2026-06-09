import { MetricCard } from "@/components/ui/metric-card";

export function DishesSummary() {
  return (
    <section className="summary-grid">
      <MetricCard
        variant="purple"
        title="接口待接入"
        label="待接入"
        subLabel="接口待接入"
        footerButton="查看详情"
        miniStats={[
          { value: "--", label: "销售额" },
          { value: "--", label: "毛利率" },
        ]}
        topRightLabel="销量冠军"
      />

      <MetricCard
        variant="green"
        title="接口待接入"
        label="待接入"
        subLabel="接口待接入"
        footerButton="查看菜单"
        miniStats={[
          { value: "--", label: "综合评分" },
          { value: "--", label: "款差评集中" },
        ]}
        topRightLabel="菜单健康度"
        ringSmall
      />
    </section>
  );
}