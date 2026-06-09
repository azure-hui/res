type AdviceCardProps = {
  empty?: boolean;
};

export function AdviceCard({ empty = false }: AdviceCardProps) {
  if (empty) {
    return <div className="empty-state-box">暂无 AI 建议，接口待接入</div>;
  }

  return (
    <article className="advice-card active">
      <div className="advice-head">
        <div className="advice-title">
          <strong>--</strong>
          <span>接口待接入</span>
        </div>
        <span className="badge danger">--</span>
      </div>

      <div className="advice-desc">接口待接入</div>

      <div className="advice-meta">
        <span className="advice-chip warning">--</span>
        <span className="badge warn">--</span>
      </div>

      <div className="advice-actions">
        <button className="btn" type="button">
          查看详情
        </button>
        <button className="btn primary" type="button">
          执行建议
        </button>
      </div>
    </article>
  );
}
