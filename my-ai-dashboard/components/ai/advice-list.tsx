import { SectionCard } from "@/components/ui/section-card";
import { AdviceCard } from "@/components/ai/advice-card";

export function AdviceList() {
  return (
    <article className="card">
      <div className="card-header">
        <h3>今日建议列表</h3>
        <div className="filters" id="statusFilters">
          <button className="chip active" data-status-filter="all" type="button">
            全部状态
          </button>
          <button className="chip" data-status-filter="pending" type="button">
            待处理
          </button>
          <button className="chip" data-status-filter="executing" type="button">
            执行中
          </button>
          <button className="chip" data-status-filter="done" type="button">
            已完成
          </button>
          <button className="chip" data-status-filter="ignored" type="button">
            已忽略
          </button>
        </div>
      </div>

      <div className="advice-list" id="adviceList">
        <AdviceCard empty />
      </div>
    </article>
  );
}
