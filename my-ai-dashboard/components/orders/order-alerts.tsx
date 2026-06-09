import { SectionCard } from "@/components/ui/section-card";

export function OrderAlerts() {
  return (
    <SectionCard className="insights">
      <div className="card-header">
        <h3>异常处理建议</h3>
        <button className="tiny-btn" type="button">
          一键派单
        </button>
      </div>

      <ul>
        <li>
          <span className="dot info" />
          <div>
            <strong>暂无数据</strong>
            <br />
            接口待接入
          </div>
        </li>
      </ul>
    </SectionCard>
  );
}