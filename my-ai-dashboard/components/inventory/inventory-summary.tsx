import { MetricCard } from "@/components/ui/metric-card";

export function InventorySummary() {
  return (
    <section className="summary-grid">
      <MetricCard
        variant="orange"
        title="安全库存状态"
        label="库存健康度"
        subLabel="接口待接入"
        footerButton="查看明细"
        miniStats={[
          { value: "--", label: "预警品项" },
          { value: "--", label: "安全库存" },
        ]}
        topRightLabel="今日库存"
      />

      <MetricCard
        variant="purple"
        title="采购计划执行"
        label="待采购数"
        subLabel="接口待接入"
        footerButton="查看计划"
        miniStats={[
          { value: "--", label: "待审批" },
          { value: "--", label: "待下单" },
        ]}
        topRightLabel="采购任务"
        ringSmall
      />

      <MetricCard
        variant="green"
        title="供应到货跟踪"
        label="到货完成率"
        subLabel="接口待接入"
        footerButton="查看物流"
        miniStats={[
          { value: "--", label: "在途订单" },
          { value: "--", label: "已收货" },
        ]}
        topRightLabel="到货状态"
      />

      <MetricCard
        variant="blue"
        title="周期采购成本"
        label="采购金额"
        subLabel="接口待接入"
        footerButton="成本分析"
        miniStats={[
          { value: "--", label: "本日" },
          { value: "--", label: "本周" },
        ]}
        topRightLabel="成本控制"
        ringSmall
      />
    </section>
  );
}
