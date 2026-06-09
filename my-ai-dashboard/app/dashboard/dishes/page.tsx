import { PageHeader } from "@/components/ui/page-header";
import { DishesSummary } from "@/components/dishes/dishes-summary";
import { DishRankingTable } from "@/components/dishes/dish-ranking-table";
import { CategoryPerformancePanel } from "@/components/dishes/category-performance-panel";
import { DishStrategyPanel } from "@/components/dishes/dish-strategy-panel";
import { StockRiskPanel } from "@/components/dishes/stock-risk-panel";

export default function DishesPage() {
  return (
    <section className="page active" data-page="dishes">
      <PageHeader
        title="菜品分析"
        description="查看菜品销量、毛利、口味反馈、售罄风险与推荐组合"
        actions={[
          { label: "导出菜品报表" },
          { label: "更新菜单策略", primary: true },
        ]}
      />

      <DishesSummary />

      <section className="orders-grid">
        <DishRankingTable />
        <CategoryPerformancePanel />
      </section>

      <section className="two-col">
        <DishStrategyPanel />
        <StockRiskPanel />
      </section>
    </section>
  );
}