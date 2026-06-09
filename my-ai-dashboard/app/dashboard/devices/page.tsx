import { PageHeader } from "@/components/ui/page-header";
import { DeviceSummary } from "@/components/devices/device-summary";
import { DeviceList } from "@/components/devices/device-list";
import { DeviceResourcePanel } from "@/components/devices/device-resource-panel";
import { DeviceAlerts } from "@/components/devices/device-alerts";
import { DeviceMaintenancePlan } from "@/components/devices/device-maintenance-plan";

export default function DevicesPage() {
  return (
    <section className="page active" data-page="devices">
      <PageHeader
        title="设备监控"
        description="统一监控摄像头、POS、打印机、后厨屏、网络与识别服务状态"
        actions={[
          { label: "导出巡检" },
          { label: "新增告警规则", primary: true },
        ]}
      />

      <DeviceSummary />

      <section className="orders-grid">
        <DeviceList />
        <DeviceResourcePanel />
      </section>

      <section className="two-col">
        <DeviceAlerts />
        <DeviceMaintenancePlan />
      </section>
    </section>
  );
}