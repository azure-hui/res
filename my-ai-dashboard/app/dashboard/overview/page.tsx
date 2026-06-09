import { PageHeader } from "@/components/ui/page-header";
import { OverviewSummaryGrid } from "@/components/overview/overview-summary-grid";
import { OverviewLivePanel } from "@/components/overview/overview-live-panel";
import { OverviewInsightsCard } from "@/components/overview/overview-insights-card";
import { OverviewBottomStats } from "@/components/overview/overview-bottom-stats";

export default function OverviewPage() {
  return (
    <section className="page active" data-page="dashboard">
      <PageHeader
        title="经营仪表盘"
        description="实时查看门店营收、客流、桌台状态与 AI 运营建议"
        actions={[
          { label: "导出日报" },
          { label: "新增运营任务", primary: true },
        ]}
      />

      <OverviewSummaryGrid />

      <section className="content-grid">
        <OverviewLivePanel />
        <OverviewInsightsCard />
      </section>

      <OverviewBottomStats />
    </section>
  );
}
