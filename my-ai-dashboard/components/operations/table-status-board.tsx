import { EmptyState } from "@/components/ui/empty-state";
import { SectionCard } from "@/components/ui/section-card";

export function TableStatusBoard() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>桌台分布图</h3>
        <div className="filters">
          <button className="chip active" type="button">
            大厅 A
          </button>
          <button className="chip" type="button">
            大厅 B
          </button>
          <button className="chip" type="button">
            包间
          </button>
        </div>
      </div>

      <div className="table-map">
        <EmptyState message="暂无数据，接口待接入" fullWidth />
      </div>
    </SectionCard>
  );
}
