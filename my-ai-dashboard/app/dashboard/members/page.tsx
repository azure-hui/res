import { PageHeader } from "@/components/ui/page-header";
import { MembersSummary } from "@/components/members/members-summary";
import { MemberSegmentationPanel } from "@/components/members/member-segmentation-panel";
import { MemberMarketingTasks } from "@/components/members/member-marketing-tasks";
import { MemberActivityTable } from "@/components/members/member-activity-table";

export default function MembersPage() {
  return (
    <section className="page active" data-page="members">
      <PageHeader
        title="会员营销"
        description="查看会员增长、活跃度、复购转化与活动执行情况，当前页面数据全部预留接口接入"
        actions={[
          { label: "导出会员报表" },
          { label: "创建营销活动", primary: true },
        ]}
      />

      <MembersSummary />

      <section className="two-col">
        <MemberSegmentationPanel />
        <MemberMarketingTasks />
      </section>

      <MemberActivityTable />
    </section>
  );
}
