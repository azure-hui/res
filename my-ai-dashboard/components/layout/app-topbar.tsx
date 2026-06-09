export function AppTopbar() {
  return (
    <div className="topbar">
      <div className="userbox">
        <div className="avatar">--</div>
        <div className="store-meta">
          <strong>门店名称</strong>
          <span>视图待接入</span>
        </div>
      </div>

      <div className="top-meta">
        <span id="todayText">日期待接入</span>
        <span className="pill" id="currentTimeText">
          时间待接入
        </span>
        <span className="pill" id="weatherText">
          天气待接入
        </span>
        <span className="pill status-open" id="businessStatusText">
          ● 状态待接入
        </span>
        <span className="pill" id="noticeText">
          提醒待接入
        </span>
      </div>
    </div>
  );
}
