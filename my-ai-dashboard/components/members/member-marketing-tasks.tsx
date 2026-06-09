import { SectionCard } from "@/components/ui/section-card";

export function MemberMarketingTasks() {
  return (
    <SectionCard className="insights">
      <div className="card-header">
        <h3>营销建议与触达任务</h3>
        <button className="tiny-btn" type="button">
          新建触达
        </button>
      </div>

      <ul>
        <li>
          <span className="dot info" />
          <div>
            <strong>暂无营销建议</strong>
            <br />
            接口待接入
          </div>
        </li>
        <li>
          <span className="dot warn" />
          <div>
            <strong>暂无待执行活动</strong>
            <br />
            接口待接入
          </div>
        </li>
        <li>
          <span className="dot danger" />
          <div>
            <strong>暂无沉默会员召回任务</strong>
            <br />
            接口待接入
          </div>
        </li>
      </ul>
    </SectionCard>
  );
}
