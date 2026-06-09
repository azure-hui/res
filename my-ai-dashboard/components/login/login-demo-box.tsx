export function LoginDemoBox() {
  return (
    <div className="demo-box">
      <div className="demo-top">
        <h3 className="demo-title">演示账号</h3>
        <span className="demo-tag">Demo</span>
      </div>

      <div className="demo-grid">
        <div className="demo-item">
          <div className="k">管理员账号</div>
          <div className="v">admin</div>
        </div>
        <div className="demo-item">
          <div className="k">管理员密码</div>
          <div className="v">123456</div>
        </div>
        <div className="demo-item">
          <div className="k">经理账号</div>
          <div className="v">manager01</div>
        </div>
        <div className="demo-item">
          <div className="k">经理密码</div>
          <div className="v">123456</div>
        </div>
      </div>
    </div>
  );
}
