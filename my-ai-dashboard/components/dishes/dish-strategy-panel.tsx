import { SectionCard } from "@/components/ui/section-card";

export function DishStrategyPanel() {
  return (
    <SectionCard className="insights">
      <div className="card-header">
        <h3>AI 菜品策略建议</h3>
        <button className="tiny-btn" type="button">
          应用推荐
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