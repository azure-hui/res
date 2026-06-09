import { SectionCard } from "@/components/ui/section-card";

export function DeviceList() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>设备状态列表</h3>
        <div className="filters">
          <button className="chip active" type="button">
            全部
          </button>
          <button className="chip" type="button">
            摄像头
          </button>
          <button className="chip" type="button">
            收银设备
          </button>
          <button className="chip" type="button">
            厨房设备
          </button>
        </div>
      </div>

      <div style={{ overflow: "auto" }}>
        <table>
          <thead>
            <tr>
              <th>设备</th>
              <th>位置</th>
              <th>类型</th>
              <th>状态</th>
              <th>最近心跳</th>
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