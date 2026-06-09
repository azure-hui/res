type ChannelBlockProps = {
  title: string;
  withCta?: boolean;
};

function ChannelBlock({ title, withCta = false }: ChannelBlockProps) {
  return (
    <div className="stat-block">
      <h4>{title}</h4>

      <div className="kpi-row">
        <span>订单数</span>
        <b>--</b>
      </div>
      <div className="kpi-row">
        <span>营业额</span>
        <b>--</b>
      </div>
      <div className="kpi-row">
        <span>客单价</span>
        <b>--</b>
      </div>
      <div className="kpi-row">
        <span>退款数</span>
        <b>--</b>
      </div>

      {withCta ? (
        <div className="cta-box">
          接口待接入
          <span>晚高峰前建议重点关注堂食翻台与外卖出餐效率</span>
          <button type="button">查看明细</button>
        </div>
      ) : null}
    </div>
  );
}

export function OverviewBottomStats() {
  return (
    <section className="card bottom-card">
      <div className="card-header">
        <h3>渠道经营数据</h3>
        <div className="filters">
          <button className="chip active" type="button">
            今日
          </button>
          <button className="chip" type="button">
            近 7 天
          </button>
          <button className="chip" type="button">
            近 30 天
          </button>
        </div>
      </div>

      <div className="stats-tabs">
        <ChannelBlock title="堂食" />
        <ChannelBlock title="外卖" />
        <ChannelBlock title="自提" withCta />
      </div>
    </section>
  );
}
