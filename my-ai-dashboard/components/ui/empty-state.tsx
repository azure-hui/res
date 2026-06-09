export function EmptyState({
  message = "暂无数据，接口待接入",
  fullWidth = false,
}: {
  message?: string;
  fullWidth?: boolean;
}) {
  return (
    <div className={fullWidth ? "empty-state-box full-width" : "empty-state-box"}>
      {message}
    </div>
  );
}
