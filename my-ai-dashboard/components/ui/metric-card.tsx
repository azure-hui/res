import type { ReactNode } from "react";

type MetricCardProps = {
  variant: "orange" | "purple" | "green" | "blue";
  title: string;
  label: string;
  value?: string;
  valueId?: string;
  subLabel?: string;
  ringSmall?: boolean;
  footerButton: string;
  miniStats: Array<{ value?: string; label: string }>;
  extra?: ReactNode;
};

export function MetricCard({
  variant,
  title,
  label,
  value = "--",
  valueId,
  subLabel = "接口待接入",
  ringSmall = false,
  footerButton,
  miniStats,
  extra,
}: MetricCardProps) {
  return (
    <article className={`metric-card ${variant}`}>
      <div className="metric-inner">
        <div className={ringSmall ? "ring small" : "ring"} />

        <div className="metric-content">
          <div className="metric-top">
            <div>
              <h3 id={valueId}>{value}</h3>
              <span>待接入</span>
            </div>
            <span>{label}</span>
          </div>

          <div>
            <h4>{title}</h4>
            <div className="metric-sub">{subLabel}</div>
          </div>

          <div className="metric-footer">
            <div className="mini-stats">
              {miniStats.map((item) => (
                <span key={item.label}>
                  <b>{item.value ?? "--"}</b> {item.label}
                </span>
              ))}
            </div>

            {extra ?? (
              <button className="btn-white" type="button">
                {footerButton}
              </button>
            )}
          </div>
        </div>
      </div>
    </article>
  );
}
