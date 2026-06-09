type HeaderAction = {
  label: string;
  primary?: boolean;
};

export function PageHeader({
  title,
  description,
  actions = [],
}: {
  title: string;
  description: string;
  actions?: HeaderAction[];
}) {
  return (
    <div className="title-row">
      <div>
        <h2>{title}</h2>
        <p>{description}</p>
      </div>

      <div className="actions">
        {actions.map((action) => (
          <button
            key={action.label}
            className={action.primary ? "btn primary" : "btn"}
            type="button"
          >
            {action.label}
          </button>
        ))}
      </div>
    </div>
  );
}
