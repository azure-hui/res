import { SectionCard } from "@/components/ui/section-card";

export function StockRiskPanel() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>库存与售罄风险</h3>
        <button className="tiny-btn" type="button">
          同步采购
        </button>
      </div>

      <div className="tasks">
        <div className="empty-state-box">暂无数据，接口待接入</div>
      </div>
    </SectionCard>
  );
}