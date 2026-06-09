import { PageHeader } from "@/components/ui/page-header";
import { InventorySummary } from "@/components/inventory/inventory-summary";
import { InventoryCategoryBoard } from "@/components/inventory/inventory-category-board";
import { InventoryAlerts } from "@/components/inventory/inventory-alerts";
import { PurchasePlanTable } from "@/components/inventory/purchase-plan-table";

export default function InventoryPage() {
  return (
    <section className="page active" data-page="inventory">
      <PageHeader
        title="库存采购"
        description="查看库存健康度、采购计划、预警与到货进度，当前页面数据全部预留接口接入"
        actions={[
          { label: "导出采购单" },
          { label: "新建采购计划", primary: true },
        ]}
      />

      <InventorySummary />

      <section className="ops-grid">
        <InventoryCategoryBoard />
        <InventoryAlerts />
      </section>

      <PurchasePlanTable />
    </section>
  );
}
