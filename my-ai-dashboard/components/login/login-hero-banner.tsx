export function LoginHeroBanner() {
  return (
    <div className="hero-banner">
      <div>
        <div className="eyebrow">✨ 与你当前 Restaurant 项目后台风格统一</div>
        <h2 className="hero-title">
          登录后快速进入经营仪表盘，
          <br />
          统一查看门店、订单与 AI 建议。
        </h2>
        <p className="hero-desc">
          这是一版为你的 restaurant 项目单独设计的登录页，延续你现有后台的暖米色底、
          橙色品牌强调、大圆角卡片和轻玻璃质感，适合直接作为独立登录页面接入。
        </p>
      </div>

      <div className="hero-stats">
        <div className="hero-stat">
          <div className="label">今日营业额</div>
          <div className="value">¥12,860</div>
          <div className="hint">较昨日 +12.4%</div>
        </div>
        <div className="hero-stat">
          <div className="label">在店人数</div>
          <div className="value">46</div>
          <div className="hint">大厅 32 / 包间 14</div>
        </div>
        <div className="hero-stat">
          <div className="label">门店状态</div>
          <div className="value">营业中</div>
          <div className="hint">3 条提醒待处理</div>
        </div>
      </div>
    </div>
  );
}
