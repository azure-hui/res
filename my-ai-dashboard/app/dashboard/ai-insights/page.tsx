import { PageHeader } from "@/components/ui/page-header";
import { AiSummary } from "@/components/ai/ai-summary";
import { AiKpiGrid } from "@/components/ai/ai-kpi-grid";
import { AdviceFilters } from "@/components/ai/advice-filters";
import { AdviceList } from "@/components/ai/advice-list";
import { AdviceDetailPanel } from "@/components/ai/advice-detail-panel";
import { AdviceEvidencePanel } from "@/components/ai/advice-evidence-panel";
import { AdviceRecordPanel } from "@/components/ai/advice-record-panel";

export default function AiInsightsPage() {
  return (
    <section className="page active" data-page="ai-advice">
      <PageHeader
        title="AI 经营建议中心"
        description="围绕客流、桌台、菜品、库存与服务表现，输出可直接执行的经营建议"
        actions={[
          { label: "导出建议日报" },
          { label: "刷新建议" },
          { label: "一键生成任务", primary: true },
        ]}
      />

      <AiSummary />
      <AiKpiGrid />
      <AdviceFilters />

      <section className="ai-layout">
        <AdviceList />
        <aside>
          <AdviceDetailPanel />
          <AdviceEvidencePanel />
          <AdviceRecordPanel />
        </aside>
      </section>
    </section>
  );
}
