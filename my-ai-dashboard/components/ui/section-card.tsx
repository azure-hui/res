import type { ReactNode } from "react";

export function SectionCard({
  className = "",
  children,
}: {
  className?: string;
  children: ReactNode;
}) {
  return <article className={`card ${className}`.trim()}>{children}</article>;
}
