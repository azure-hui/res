import { SectionCard } from "@/components/ui/section-card";

function EmptyKanbanColumn() {
  return (
    <div className="kanban-col">
      <h4>接口待接入</h4>
      <div className="kanban-stack">
        <div className="empty-state-box full-width">暂无数据，接口待接入</div>
      </div>
    </div>
  );
}

export function OrdersTableSection() {
  return (
    <section className="orders-grid">
      <SectionCard>
        <div className="card-header">
          <h3>订单列表</h3>
          <div className="filters">
            <button className="chip active" type="button">
              全部
            </button>
            <button className="chip" type="button">
              堂食
            </button>
            <button className="chip" type="button">
              外卖
            </button>
            <button className="chip" type="button">
              自提
            </button>
          </div>
        </div>

        <div style={{ overflow: "auto" }}>
          <table>
            <thead>
              <tr>
                <th>订单号</th>
                <th>渠道</th>
                <th>桌号/用户</th>
                <th>金额</th>
                <th>状态</th>
                <th>时间</th>
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

      <SectionCard>
        <div className="card-header">
          <h3>订单看板</h3>
          <button className="tiny-btn" type="button">
            自动刷新
          </button>
        </div>

        <div className="kanban">
          <EmptyKanbanColumn />
          <EmptyKanbanColumn />
          <EmptyKanbanColumn />
        </div>
      </SectionCard>
    </section>
  );
}