import { OperationsSummary } from "@/components/operations/operations-summary";
import { TableStatusBoard } from "@/components/operations/table-status-board";
import { QueuePanel } from "@/components/operations/queue-panel";
import { StaffSchedule } from "@/components/operations/staff-schedule";
import { KitchenEfficiency } from "@/components/operations/kitchen-efficiency";
import { PageHeader } from "@/components/ui/page-header";

export default function StoreOpsPage() {
  return (
    <section className="page active" data-page="operations">
      <PageHeader
        title="门店运营"
        description="聚焦桌台状态、排队管理、人员排班与出餐效率"
        actions={[
          { label: "导出排班" },
          { label: "新增临时调度", primary: true },
        ]}
      />

      <OperationsSummary />

      <section className="ops-grid">
        <TableStatusBoard />
        <KitchenEfficiency />
      </section>

      <section className="two-col">
        <QueuePanel />
        <StaffSchedule />
      </section>
    </section>
  );
}
