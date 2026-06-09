import { SectionCard } from "@/components/ui/section-card";

export function PurchasePlanTable() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>采购计划列表</h3>
        <div className="filters">
          <button className="chip active" type="button">
            全部
          </button>
          <button className="chip" type="button">
            待审批
          </button>
          <button className="chip" type="button">
            采购中
          </button>
          <button className="chip" type="button">
            已完成
          </button>
        </div>
      </div>

      <div style={{ overflow: "auto" }}>
        <table>
          <thead>
            <tr>
              <th>计划单号</th>
              <th>供应商</th>
              <th>预计到货时间</th>
              <th>采购金额</th>
              <th>状态</th>
              <th>备注</th>
            </tr>
          </thead>
          <tbody>
            <tr className="empty-state-box-row">
              <td colSpan={6}>暂无数据，接口待接入</td>
            </tr>
          </tbody>
        </table>
      </div>
    </SectionCard>
  );
}
