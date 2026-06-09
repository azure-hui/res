import { SectionCard } from "@/components/ui/section-card";

export function OverviewLivePanel() {
  return (
    <SectionCard>
      <div className="card-header">
        <h3>门店实时状态</h3>
        <div className="filters">
          <button className="chip active" type="button">
            大厅 A 区
          </button>
          <button className="chip" type="button">
            大厅 B 区
          </button>
          <button className="chip" type="button">
            后厨
          </button>
        </div>
      </div>

      <div className="live-panel">
        <div className="play-btn">▶</div>

        <div className="live-meta">
          <div>
            <strong>实时画面</strong>
            <span>接口待接入</span>
          </div>

          <button className="tiny-btn" type="button">
            查看详情
          </button>
        </div>
      </div>
    </SectionCard>
  );
}
