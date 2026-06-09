import { EmptyState } from "@/components/ui/empty-state";

export function AppRightbar() {
  return (
    <aside className="rightbar">
      <h3>运营动态</h3>

      <section className="panel">
        <div className="panel-header">
          <h4>实时动态</h4>
          <button className="tiny-btn" type="button">
            查看全部
          </button>
        </div>

        <div className="feed" id="activityFeed">
          <EmptyState message="暂无数据，接口待接入" />
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <h4>自动任务与告警</h4>
          <button className="tiny-btn" type="button">
            任务配置
          </button>
        </div>

        <div className="tasks">
          <EmptyState message="暂无数据，接口待接入" />
        </div>
      </section>

      <div className="footer-note">页面结构保留，数据接口待接入</div>
    </aside>
  );
}
