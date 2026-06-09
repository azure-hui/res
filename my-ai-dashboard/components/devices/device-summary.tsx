import { MetricCard } from "@/components/ui/metric-card";

export function DeviceSummary() {
  return (
    <section className="summary-grid">
      <MetricCard
        variant="blue"
        title="接口待接入"
        label="待接入"
        subLabel="接口待接入"
        footerButton="查看拓扑"
        miniStats={[
          { value: "--", label: "离线" },
          { value: "--", label: "告警" },
        ]}
        topRightLabel="设备在线率"
      />

      <MetricCard
        variant="orange"
        title="接口待接入"
        label="待接入"
        subLabel="接口待接入"
        footerButton="服务详情"
        miniStats={[
          { value: "--", label: "存储占用" },
          { value: "--", label: "今日可用率" },
        ]}
        topRightLabel="系统性能"
        ringSmall
      />
    </section>
  );
}