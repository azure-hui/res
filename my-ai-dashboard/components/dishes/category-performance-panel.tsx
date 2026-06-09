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

export function CategoryPerformancePanel() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>分类经营表现</h3>
        <button className="tiny-btn" type="button">
          查看趋势
        </button>
      </div>

      <div className="progress-group">
        <ProgressRow label="锅底类贡献" />
        <ProgressRow label="招牌菜贡献" barClassName="bar purple" />
        <ProgressRow label="饮品加购率" barClassName="bar blue" />
        <ProgressRow label="甜品转化率" barClassName="bar green" />
      </div>

      <div className="mini-grid" style={{ marginTop: 18 }}>
        <div className="metric-mini">
          <strong>--</strong>
          <span>售罄预警</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>滞销菜品</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>加饮转化</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>人均加购额</span>
        </div>
      </div>
    </SectionCard>
  );
}