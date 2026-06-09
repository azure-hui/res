import { PageHeader } from "@/components/ui/page-header";
import { TablesSummary } from "@/components/tables/tables-summary";
import { TableMap } from "@/components/tables/table-map";
import { TurnoverMetrics } from "@/components/tables/turnover-metrics";
import { ReservationPanel } from "@/components/tables/reservation-panel";
import { TableAdvicePanel } from "@/components/tables/table-advice-panel";

export default function TablesPage() {
  return (
    <section className="page active" data-page="tables">
      <PageHeader
        title="桌台管理"
        description="统一查看桌台占用、预订、排队、清台与翻台效率"
        actions={[
          { label: "导出桌态" },
          { label: "新增预订", primary: true },
        ]}
      />

      <TablesSummary />

      <section className="ops-grid">
        <TableMap />
        <TurnoverMetrics />
      </section>

      <section className="two-col">
        <ReservationPanel />
        <TableAdvicePanel />
      </section>
    </section>
  );
}
