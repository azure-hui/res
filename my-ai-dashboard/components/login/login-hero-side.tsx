export function LoginHeroSide() {
  return (
    <div className="hero-side">
      <div className="mini-card">
        <h3>登录后可进入模块</h3>
        <p>与你当前后台菜单结构保持一致，方便后续直接接真实接口与权限控制。</p>
        <div className="module-grid">
          <div className="module-item">经营仪表盘</div>
          <div className="module-item">门店运营</div>
          <div className="module-item">订单中心</div>
          <div className="module-item">桌台管理</div>
          <div className="module-item">菜品分析</div>
          <div className="module-item">AI 建议</div>
        </div>
      </div>

      <div className="mini-card">
        <h3>页面适配说明</h3>
        <p>当前文件为纯前端静态演示版，可先直接预览，再替换成你的真实登录逻辑。</p>
        <ul className="tips-list">
          <li>
            <span className="dot" />
            <span>已内置账号输入、密码显隐、角色切换、记住我、模拟登录反馈。</span>
          </li>
          <li>
            <span className="dot" />
            <span>
              后续可把登录按钮接到 <strong>/api/v1/auth/login</strong>。
            </span>
          </li>
          <li>
            <span className="dot" />
            <span>登录成功后可跳转到你的 dashboard 页面。</span>
          </li>
        </ul>
      </div>
    </div>
  );
}
