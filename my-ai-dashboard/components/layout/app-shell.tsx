import type { ReactNode } from "react";
import { AppSidebar } from "./app-sidebar";
import { AppTopbar } from "./app-topbar";
import { AppRightbar } from "./app-rightbar";

export function AppShell({ children }: { children: ReactNode }) {
  return (
    <div className="app">
      <AppSidebar />

      <main className="main">
        <AppTopbar />
        {children}
      </main>

      <AppRightbar />
    </div>
  );
}
