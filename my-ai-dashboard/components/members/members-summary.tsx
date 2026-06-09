import { MetricCard } from "@/components/ui/metric-card";

export function MembersSummary() {
  return (
    <section className="summary-grid">
      <MetricCard
        variant="purple"
        title="会员增长趋势"
        label="会员总数"
        subLabel="接口待接入"
        footerButton="查看增长"
        miniStats={[
          { value: "--", label: "新增" },
          { value: "--", label: "净增长" },
        ]}
        topRightLabel="会员规模"
      />

      <MetricCard
        variant="orange"
        title="到店活跃度"
        label="活跃会员"
        subLabel="接口待接入"
        footerButton="查看活跃"
        miniStats={[
          { value: "--", label: "到店" },
          { value: "--", label: "沉默" },
        ]}
        topRightLabel="近周期活跃"
        ringSmall
      />

      <MetricCard
        variant="green"
        title="会员复购表现"
        label="复购率"
        subLabel="接口待接入"
        footerButton="查看复购"
        miniStats={[
          { value: "--", label: "本周" },
          { value: "--", label: "本月" },
        ]}
        topRightLabel="复购转化"
      />

      <MetricCard
        variant="blue"
        title="优惠活动效果"
        label="营销转化"
        subLabel="接口待接入"
        footerButton="查看活动"
        miniStats={[
          { value: "--", label: "触达" },
          { value: "--", label: "核销" },
        ]}
        topRightLabel="活动表现"
        ringSmall
      />
    </section>
  );
}
