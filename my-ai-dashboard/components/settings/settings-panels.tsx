"use client";

import { SectionCard } from "@/components/ui/section-card";
import { clearStoredSession, getStoredSession } from "@/lib/auth";
import type { AuthSession } from "@/types/auth";
import { useEffect, useState } from "react";

function FieldRow({
  label,
  placeholder,
}: {
  label: string;
  placeholder: string;
}) {
  return (
    <div className="field" style={{ marginBottom: 16 }}>
      <label>{label}</label>
      <div className="input-wrap">
        <input className="input" placeholder={placeholder} readOnly />
      </div>
    </div>
  );
}

function SwitchRow({
  title,
  desc,
}: {
  title: string;
  desc: string;
}) {
  return (
    <div
      style={{
        padding: "14px 0",
        borderBottom: "1px solid var(--line)",
        display: "flex",
        justifyContent: "space-between",
        gap: 12,
        alignItems: "center",
      }}
    >
      <div>
        <strong style={{ display: "block", fontSize: 14, marginBottom: 4 }}>{title}</strong>
        <span style={{ fontSize: 12, color: "var(--muted)", lineHeight: 1.7 }}>{desc}</span>
      </div>

      <button className="tiny-btn" type="button">
        enabled
      </button>
    </div>
  );
}

export function SettingsPanels() {
  const [session, setSession] = useState<AuthSession | null>(null);

  useEffect(() => {
    setSession(getStoredSession());
  }, []);

  function handleLogout() {
    clearStoredSession();
    window.location.href = "/login";
  }

  return (
    <>
      <section className="two-col">
        <SectionCard>
          <div className="card-header">
            <h3>Store profile</h3>
            <button className="tiny-btn" type="button">
              edit
            </button>
          </div>

          <FieldRow label="Store name" placeholder="API pending" />
          <FieldRow label="Contact" placeholder="API pending" />
          <FieldRow label="Phone" placeholder="API pending" />
          <FieldRow label="Address" placeholder="API pending" />
        </SectionCard>

        <SectionCard>
          <div className="card-header">
            <h3>Business notifications</h3>
            <button className="tiny-btn" type="button">
              rules
            </button>
          </div>

          <FieldRow label="Business hours" placeholder="API pending" />
          <FieldRow label="Time zone" placeholder="API pending" />

          <div className="progress-group" style={{ marginTop: 8 }}>
            <SwitchRow title="Order alerts" desc="Notify on timeout, refund, or urgent orders" />
            <SwitchRow title="Inventory alerts" desc="Notify on low stock or sellout risk" />
            <SwitchRow title="Device alerts" desc="Notify when POS or edge devices go offline" />
          </div>
        </SectionCard>
      </section>

      <section className="two-col">
        <SectionCard>
          <div className="card-header">
            <h3>Account and access</h3>
            <button className="tiny-btn" type="button">
              permissions
            </button>
          </div>

          <div className="tasks">
            <div className="task-item">
              <div className="task-top">
                <strong>Current account</strong>
                <span className="badge success">connected</span>
              </div>
              <p>
                Account: {session?.user.username ?? "--"}
                <br />
                Role: {session?.user.role ?? "--"}
                <br />
                Display name: {session?.user.displayName ?? "--"}
              </p>
            </div>

            <div className="task-item">
              <div className="task-top">
                <strong>Admin</strong>
                <span className="badge success">enabled</span>
              </div>
              <p>Full system configuration, account management, and reporting access.</p>
            </div>

            <div className="task-item">
              <div className="task-top">
                <strong>Manager</strong>
                <span className="badge info">enabled</span>
              </div>
              <p>Operational access for store data and day-to-day management.</p>
            </div>

            <div className="task-item">
              <div className="task-top">
                <strong>Operator</strong>
                <span className="badge gray">pending</span>
              </div>
              <p>Limited access for assigned modules and workflow tasks.</p>
            </div>
          </div>
        </SectionCard>

        <SectionCard>
          <div className="card-header">
            <h3>System preferences</h3>
            <button className="tiny-btn" type="button">
              more
            </button>
          </div>

          <div className="mini-grid">
            <div className="metric-mini">
              <strong>--</strong>
              <span>Refresh rate</span>
            </div>
            <div className="metric-mini">
              <strong>--</strong>
              <span>Log retention</span>
            </div>
            <div className="metric-mini">
              <strong>--</strong>
              <span>Default landing page</span>
            </div>
            <div className="metric-mini">
              <strong>--</strong>
              <span>Theme mode</span>
            </div>
          </div>

          <div className="cta-box" style={{ marginTop: 18 }}>
            Auth session is now stored in one place
            <span>Use this button to clear the local session and return to the login page.</span>
            <button type="button" onClick={handleLogout}>
              Log out
            </button>
          </div>
        </SectionCard>
      </section>
    </>
  );
}
