import { SectionCard } from "@/components/ui/section-card";

export function AdviceFilters() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>建议筛选</h3>
        <div className="filters" id="adviceFilters">
          <button className="chip active" data-filter="all" type="button">
            全部
          </button>
          <button className="chip" data-filter="high" type="button">
            高优先级
          </button>
          <button className="chip" data-filter="tables" type="button">
            桌台
          </button>
          <button className="chip" data-filter="inventory" type="button">
            库存
          </button>
          <button className="chip" data-filter="dishes" type="button">
            菜品
          </button>
          <button className="chip" data-filter="service" type="button">
            服务
          </button>
        </div>
      </div>
    </SectionCard>
  );
}
