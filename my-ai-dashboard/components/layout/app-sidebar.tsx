"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

type NavItem = {
  label: string;
  icon: string;
  href?: string;
  pageKey?: string;
};

const overviewItems: NavItem[] = [
  { label: "仪表盘", icon: "▣", href: "/dashboard/overview", pageKey: "dashboard" },
  { label: "门店运营", icon: "◔", href: "/dashboard/store-ops", pageKey: "operations" },
  { label: "订单中心", icon: "🧾", href: "/dashboard/orders", pageKey: "orders" },
  { label: "桌台管理", icon: "☷", href: "/dashboard/tables", pageKey: "tables" },
  { label: "菜品分析", icon: "🍜", href: "/dashboard/dishes", pageKey: "dishes" },
  { label: "AI 建议", icon: "✦", href: "/dashboard/ai-insights", pageKey: "ai-advice" },
];

const managementItems: NavItem[] = [
  { label: "库存采购", icon: "📦", href: "/dashboard/inventory", pageKey: "inventory" },
  { label: "会员营销", icon: "👥", href: "/dashboard/members", pageKey: "members" },
  { label: "设备监控", icon: "📷", href: "/dashboard/devices", pageKey: "devices" },
  { label: "系统设置", icon: "⚙", href: "/dashboard/settings", pageKey: "settings" },
];

function SidebarNavItem({ item, active }: { item: NavItem; active: boolean }) {
  const content = (
    <>
      <span className="icon">{item.icon}</span>
      {item.label}
    </>
  );

  if (!item.href) {
    return (
      <a className={active ? "active" : undefined} data-page={item.pageKey} aria-disabled="true">
        {content}
      </a>
    );
  }

  return (
    <Link
      href={item.href}
      className={active ? "active" : undefined}
      data-page={item.pageKey}
    >
      {content}
    </Link>
  );
}

export function AppSidebar() {
  const pathname = usePathname();

  return (
    <aside className="sidebar">
      <div className="brand">
        <div className="brand-badge">🍽</div>
        <div>
          <h1>RestaurantOS</h1>
          <p>智能运营中心</p>
        </div>
      </div>

      <div>
        <div className="nav-section-title">Overview</div>
        <nav className="nav" id="mainNav">
          {overviewItems.map((item) => (
            <SidebarNavItem
              key={item.label}
              item={item}
              active={Boolean(item.href && pathname === item.href)}
            />
          ))}
        </nav>
      </div>

      <div>
        <div className="nav-section-title">Management</div>
        <nav className="nav">
          {managementItems.map((item) => (
            <SidebarNavItem
              key={item.label}
              item={item}
              active={Boolean(item.href && pathname === item.href)}
            />
          ))}
        </nav>
      </div>

      <div className="sidebar-footer">
        <h3>AI 今日建议</h3>
        <p>接口待接入</p>
        <button id="aiActionBtn" type="button">
          查看建议
        </button>
      </div>
    </aside>
  );
}
