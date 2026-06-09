import { SectionCard } from "@/components/ui/section-card";

export function InventoryAlerts() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>采购与预警</h3>
        <button className="tiny-btn" type="button">
          查看全部
        </button>
      </div>

      <div className="tasks">
        <div className="empty-state-box">暂无数据，接口待接入</div>
      </div>
    </SectionCard>
  );
}
