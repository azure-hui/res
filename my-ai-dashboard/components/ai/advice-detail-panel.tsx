export function AdviceDetailPanel() {
  return (
    <section className="detail-panel">
      <div className="panel-header">
        <h4>建议详情</h4>
        <button className="tiny-btn" id="jumpSelectedBtn" type="button">
          定位到卡片
        </button>
      </div>

      <div className="detail-banner">
        <strong id="detailTitle">--</strong>
        <div className="sub" id="detailTime">
          接口待接入
        </div>
      </div>

      <div className="advice-meta">
        <span className="badge danger" id="detailPriority">
          --
        </span>
        <span className="advice-chip warning" id="detailType">
          --
        </span>
        <span className="badge warn" id="detailStatus">
          --
        </span>
      </div>

      <div className="detail-section-title">建议说明</div>
      <div className="detail-copy" id="detailDesc">
        接口待接入
      </div>

      <div className="detail-section-title">触发原因</div>
      <div className="detail-copy" id="detailReason">
        接口待接入
      </div>

      <div className="detail-section-title">预估效果</div>
      <div className="detail-copy" id="detailEffect">
        接口待接入
      </div>
    </section>
  );
}
