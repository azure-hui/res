export function AdviceRecordPanel() {
  return (
    <section className="record-panel">
      <div className="panel-header">
        <h4>执行记录</h4>
        <button className="tiny-btn" type="button">
          查看全部
        </button>
      </div>

      <div className="record-list">
        <div className="record-item">
          <div className="meta-line">
            <strong>暂无数据</strong>
            <span className="badge gray">接口待接入</span>
          </div>
          <div className="record-note">接口待接入</div>
        </div>
      </div>
    </section>
  );
}
