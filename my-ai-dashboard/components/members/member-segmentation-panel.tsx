import { SectionCard } from "@/components/ui/section-card";

export function MemberSegmentationPanel() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>会员分层概览</h3>
        <button className="tiny-btn" type="button">
          查看分层规则
        </button>
      </div>

      <div className="mini-grid">
        <div className="metric-mini">
          <strong>--</strong>
          <span>普通会员</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>活跃会员</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>高价值会员</span>
        </div>
        <div className="metric-mini">
          <strong>--</strong>
          <span>沉默会员</span>
        </div>
      </div>

      <div className="cta-box">
        <div>
          <strong>会员画像接口待接入</strong>
          <div className="subtle">
            可接入等级、标签、生命周期、偏好品类、消费频次等字段
          </div>
        </div>
        <button type="button">配置接口</button>
      </div>
    </SectionCard>
  );
}
