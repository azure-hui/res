import { SectionCard } from "@/components/ui/section-card";

export function ReservationPanel() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>候位与预订队列</h3>
        <button className="tiny-btn" type="button">
          叫号设置
        </button>
      </div>

      <div className="tasks">
        <div className="empty-state-box">暂无数据，接口待接入</div>
      </div>
    </SectionCard>
  );
}
