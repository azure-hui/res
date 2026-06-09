import { EmptyState } from "@/components/ui/empty-state";
import { SectionCard } from "@/components/ui/section-card";

export function QueuePanel() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>当前排队列表</h3>
        <button className="tiny-btn" type="button">
          叫号设置
        </button>
      </div>

      <div className="tasks">
        <EmptyState message="暂无数据，接口待接入" />
      </div>
    </SectionCard>
  );
}
