import { SectionCard } from "@/components/ui/section-card";
import { TableFilters } from "@/components/tables/table-filters";

export function TableMap() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>桌台分布总览</h3>
        <TableFilters />
      </div>

      <div className="table-map">
        <div className="empty-state-box full-width">暂无数据，接口待接入</div>
      </div>
    </SectionCard>
  );
}
