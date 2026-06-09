export function getErrorMessage(error: unknown): string {
  const fallback = "System busy, please try again later.";
  const networkMessage = "Network error, please check your connection.";

  if (!error || typeof error !== "object") return networkMessage;

  const err = error as Record<string, unknown>;
  const response = err["response"];
  const responseObj =
    response && typeof response === "object"
      ? (response as Record<string, unknown>)
      : undefined;

  const status = responseObj?.["status"] as number | undefined;
  const data = responseObj?.["data"];
  const dataObj =
    data && typeof data === "object" ? (data as Record<string, unknown>) : undefined;

  const backendMessage = dataObj?.["message"];
  if (typeof backendMessage === "string" && backendMessage.trim()) {
    return backendMessage;
  }

  const code = err["code"];
  const message = err["message"];
  if (code === "ERR_NETWORK" || message === "Network Error") return networkMessage;

  const request = err["request"];
  if (request && response === undefined) return networkMessage;

  if (status === 401) return "Authentication failed. Please log in again.";
  if (status === 403) return "You do not have permission for this action.";
  if (status === 404) return "Requested resource was not found.";
  if (typeof status === "number" && status >= 500) return "Service is temporarily unavailable.";

  return fallback;
}
