export function toDisplayValue(value?: string | number | null) {
  if (value === null || value === undefined || value === "") {
    return "--";
  }

  return String(value);
}
