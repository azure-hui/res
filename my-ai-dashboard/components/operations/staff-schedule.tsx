import { EmptyState } from "@/components/ui/empty-state";
import { SectionCard } from "@/components/ui/section-card";

export function StaffSchedule() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>员工排班与岗位</h3>
        <button className="tiny-btn" type="button">
          排班管理
        </button>
      </div>

      <div className="tasks">
        <EmptyState message="暂无数据，接口待接入" />
      </div>
    </SectionCard>
  );
}
