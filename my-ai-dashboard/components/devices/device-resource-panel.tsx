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

export function DeviceResourcePanel() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>监控任务与资源</h3>
        <button className="tiny-btn" type="button">
          巡检面板
        </button>
      </div>

      <div className="progress-group">
        <ProgressRow label="客流识别任务负载" barClassName="bar blue" />
        <ProgressRow label="桌态识别任务负载" barClassName="bar purple" />
        <ProgressRow label="本地存储使用率" barClassName="bar" />
        <ProgressRow label="网络带宽占用" barClassName="bar green" />
      </div>

      <div className="mini-grid" style={{ marginTop: 18 }}>
        <div className="metric-mini">
          <strong>--</strong>
          <span>今日告警</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>需人工处理</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>服务可用率</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>自动恢复次数</span>
        </div>
      </div>
    </SectionCard>
  );
}