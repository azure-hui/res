import { SectionCard } from "@/components/ui/section-card";

function ProgressRow({
  label,
  value = "--",
  barClassName = "bar",
}: {
  label: string;
  value?: string;
  barClassName?: string;
}) {
  return (
    <div className="progress-row">
      <div className="progress-top">
        <span>{label}</span>
        <b>{value}</b>
      </div>
      <div className={barClassName}>
        <span style={{ width: "0%" }} />
      </div>
    </div>
  );
}

export function InventoryCategoryBoard() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>库存分类看板</h3>
        <div className="filters">
          <button className="chip active" type="button">
            全部分类
          </button>
          <button className="chip" type="button">
            食材
          </button>
          <button className="chip" type="button">
            饮品
          </button>
          <button className="chip" type="button">
            耗材
          </button>
        </div>
      </div>

      <div className="progress-group">
        <ProgressRow label="核心食材" />
        <ProgressRow label="饮品原料" barClassName="bar blue" />
        <ProgressRow label="包装耗材" barClassName="bar green" />
        <ProgressRow label="冷冻库存" barClassName="bar purple" />
      </div>

      <div className="cta-box">
        <div>
          <strong>库存数据待接入</strong>
          <div className="subtle">
            可接入库存汇总、实时余量、安全阈值、周转天数等接口
          </div>
        </div>
        <button type="button">配置接口</button>
      </div>
    </SectionCard>
  );
}
