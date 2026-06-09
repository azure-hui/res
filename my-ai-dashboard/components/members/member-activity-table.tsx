import { SectionCard } from "@/components/ui/section-card";

export function MemberActivityTable() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>活动执行列表</h3>
        <div className="filters">
          <button className="chip active" type="button">
            全部活动
          </button>
          <button className="chip" type="button">
            进行中
          </button>
          <button className="chip" type="button">
            待开始
          </button>
          <button className="chip" type="button">
            已结束
          </button>
        </div>
      </div>

      <div style={{ overflow: "auto" }}>
        <table>
          <thead>
            <tr>
              <th>活动名称</th>
              <th>触达人群</th>
              <th>开始时间</th>
              <th>结束时间</th>
              <th>状态</th>
              <th>转化结果</th>
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
