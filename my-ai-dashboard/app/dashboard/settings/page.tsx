import { PageHeader } from "@/components/ui/page-header";
import { SettingsPanels } from "@/components/settings/settings-panels";

export default function SettingsPage() {
  return (
    <section className="page active" data-page="settings">
      <PageHeader
        title="系统设置"
        description="管理门店基础信息、账号权限、通知方式与系统偏好"
        actions={[
          { label: "重置修改" },
          { label: "保存设置", primary: true },
        ]}
      />

      <SettingsPanels />
    </section>
  );
}