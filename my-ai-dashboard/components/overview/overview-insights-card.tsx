import { SectionCard } from "@/components/ui/section-card";

export function OverviewInsightsCard() {
  return (
    <SectionCard className="insights">
      <div className="card-header">
        <h3>AI 运营摘要</h3>
        <button className="tiny-btn" type="button">
          刷新建议
        </button>
      </div>

      <ul>
        <li>
          <span className="dot info" />
          <div>
            <strong>暂无数据</strong>
            <br />
            接口待接入
          </div>
        </li>
      </ul>
    </SectionCard>
  );
}
