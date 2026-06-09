import { MetricCard } from "@/components/ui/metric-card";
import { SectionCard } from "@/components/ui/section-card";

function ProgressRow({
  label,
  value = "--",
  barClassName = "bar",
}: {
  label: string;
  value?: string;
  barClassName?: string;
}) {
  return (
    <div className="progress-row">
      <div className="progress-top">
        <span>{label}</span>
        <strong>{value}</strong>
      </div>
      <div className={barClassName}>
        <span style={{ width: "0%" }} />
      </div>
    </div>
  );
}

export function OrdersSummaryCards() {
  return (
    <section className="summary-grid">
      <MetricCard
        variant="orange"
        title="订单处理状态"
        label="今日订单"
        subLabel="接口待接入"
        footerButton="查看订单流"
        miniStats={[
          { value: "--", label: "异常" },
          { value: "--", label: "催单" },
          { value: "--", label: "退款" },
        ]}
      />

      <MetricCard
        variant="purple"
        title="渠道占比"
        label="订单价值"
        subLabel="接口待接入"
        footerButton="渠道分析"
        ringSmall
        miniStats={[
          { value: "--", label: "总收入" },
          { value: "--", label: "履约率" },
        ]}
      />
    </section>
  );
}

export function OrdersMetricsCard() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>订单指标</h3>
        <button className="tiny-btn" type="button">
          查看趋势
        </button>
      </div>

      <div className="mini-grid">
        <div className="metric-mini">
          <strong>--</strong>
          <span>异常订单</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>催单数量</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>退款申请</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>履约成功率</span>
        </div>
      </div>

      <div className="progress-group" style={{ marginTop: 18 }}>
        <ProgressRow label="堂食履约" value="--" barClassName="bar green" />
        <ProgressRow label="外卖履约" value="--" barClassName="bar blue" />
        <ProgressRow label="自提履约" value="--" barClassName="bar purple" />
      </div>
    </SectionCard>
  );
}
