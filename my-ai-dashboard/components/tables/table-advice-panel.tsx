import { SectionCard } from "@/components/ui/section-card";

export function TableAdvicePanel() {
  return (
    <SectionCard className="insights">
      <div className="card-header">
        <h3>桌台运营建议</h3>
        <button className="tiny-btn" type="button">
          生成报告
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
