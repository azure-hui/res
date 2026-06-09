import { SectionCard } from "@/components/ui/section-card";

type ProgressRowProps = {
  label: string;
  value?: string;
  barClassName?: string;
};

function ProgressRow({ label, value = "--", barClassName = "bar" }: ProgressRowProps) {
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

export function KitchenEfficiency() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>运营效率</h3>
        <button className="tiny-btn" type="button">
          查看时段趋势
        </button>
      </div>

      <div className="progress-group">
        <ProgressRow label="出餐准时率" barClassName="bar green" />
        <ProgressRow label="翻台效率" barClassName="bar" />
        <ProgressRow label="前厅响应速度" barClassName="bar blue" />
        <ProgressRow label="后厨负载" barClassName="bar purple" />
      </div>

      <div className="cta-box" style={{ marginTop: 18 }}>
        接口待接入
        <span>接口待接入</span>
        <button type="button">立即处理</button>
      </div>
    </SectionCard>
  );
}
