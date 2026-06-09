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

export function TurnoverMetrics() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>清台与翻台效率</h3>
        <button className="tiny-btn" type="button">
          实时刷新
        </button>
      </div>

      <div className="progress-group">
        <ProgressRow label="大厅 A 区翻台完成率" />
        <ProgressRow label="大厅 B 区翻台完成率" value="--" barClassName="bar blue" />
        <ProgressRow label="包间清洁合格率" value="--" barClassName="bar green" />
        <ProgressRow label="预订准时到座率" value="--" barClassName="bar purple" />
      </div>

      <div className="cta-box" style={{ marginTop: 18 }}>
        接口待接入
        <span>接口待接入</span>
        <button type="button">执行调度</button>
      </div>
    </SectionCard>
  );
}
