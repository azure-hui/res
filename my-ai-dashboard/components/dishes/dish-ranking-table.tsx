import { SectionCard } from "@/components/ui/section-card";

export function DishRankingTable() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>菜品表现排行</h3>
        <div className="filters">
          <button className="chip active" type="button">
            销量
          </button>
          <button className="chip" type="button">
            毛利
          </button>
          <button className="chip" type="button">
            好评率
          </button>
        </div>
      </div>

      <div style={{ overflow: "auto" }}>
        <table>
          <thead>
            <tr>
              <th>菜品</th>
              <th>分类</th>
              <th>销量</th>
              <th>销售额</th>
              <th>毛利率</th>
              <th>评价</th>
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