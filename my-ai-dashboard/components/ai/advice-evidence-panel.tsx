function DetailMetric({ label }: { label: string }) {
  return (
    <div className="detail-metric">
      <span>{label}</span>
      <b>--</b>
    </div>
  );
}

function EvidenceCard({ title }: { title: string }) {
  return (
    <div className="evidence-card">
      <div className="evidence-row">
        <strong>{title}</strong>
        <span className="badge gray">接口待接入</span>
      </div>
      <div className="evidence-subtle">接口待接入</div>
    </div>
  );
}

function MiniBar({ label, barClassName = "bar" }: { label: string; barClassName?: string }) {
  return (
    <div className="mini-bar">
      <div className="progress-top">
        <span>{label}</span>
        <strong>--</strong>
      </div>
      <div className={barClassName}>
        <span style={{ width: "0%" }} />
      </div>
    </div>
  );
}

export function AdviceEvidencePanel() {
  return (
    <section className="evidence-panel">
      <div className="panel-header">
        <h4>建议依据</h4>
        <button className="tiny-btn" type="button">
          查看原始数据
        </button>
      </div>

      <DetailMetric label="影响营收" />
      <DetailMetric label="影响效率" />
      <DetailMetric label="执行成本" />

      <div className="detail-section-title">证据明细</div>
      <div className="evidence-grid">
        <EvidenceCard title="客流变化" />
        <EvidenceCard title="库存状态" />
      </div>

      <div className="detail-section-title">影响分布</div>
      <div className="mini-bars">
        <MiniBar label="收入提升" barClassName="bar green" />
        <MiniBar label="浪费下降" barClassName="bar" />
        <MiniBar label="服务优化" barClassName="bar blue" />
      </div>
    </section>
  );
}
