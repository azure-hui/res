import type { AuthTokens, AuthUser } from "@/types/auth";

function asObject(value: unknown): Record<string, unknown> | null {
  return value && typeof value === "object" ? (value as Record<string, unknown>) : null;
}

function firstString(source: Record<string, unknown>, keys: string[]): string | undefined {
  for (const key of keys) {
    const value = source[key];
    if (typeof value === "string" && value.trim()) {
      return value;
    }
  }
  return undefined;
}

function firstNumber(source: Record<string, unknown>, keys: string[]): number | undefined {
  for (const key of keys) {
    const value = source[key];
    if (typeof value === "number" && Number.isFinite(value)) {
      return value;
    }
  }
  return undefined;
}

function unwrapEnvelope(payload: unknown): Record<string, unknown> {
  const root = asObject(payload);
  if (!root) {
    throw new Error("Auth response is not an object.");
  }

  const data = asObject(root.data);
  return data ?? root;
}

function requireString(value: string | undefined, label: string): string {
  if (!value) {
    throw new Error(`Missing auth field: ${label}`);
  }
  return value;
}

export function mapLoginTokens(payload: unknown): AuthTokens {
  const data = unwrapEnvelope(payload);

  const accessToken = requireString(
    firstString(data, [
      "access_token",
      "accessToken",
      // TODO: replace with your real access-token field if different.
    ]),
    "access token",
  );

  const refreshToken = firstString(data, [
    "refresh_token",
    "refreshToken",
    // TODO: replace with your real refresh-token field if different.
  ]);

  const tokenType =
    firstString(data, [
      "token_type",
      "tokenType",
      // TODO: replace with your real token-type field if different.
    ]) ?? "Bearer";

  const expiresInSeconds = firstNumber(data, [
    "expires_in",
    "access_expires_in",
    "expiresIn",
    // TODO: replace with your real expiry field if different.
  ]);

  return {
    accessToken,
    refreshToken,
    tokenType,
    expiresAt:
      typeof expiresInSeconds === "number"
        ? new Date(Date.now() + expiresInSeconds * 1000).toISOString()
        : undefined,
  };
}

export function mapAuthUser(payload: unknown): AuthUser {
  const data = unwrapEnvelope(payload);
  const candidate = asObject(data.user) ?? data;

  const idValue = candidate.id ?? candidate.user_id ?? candidate.userId;
  const id = typeof idValue === "string" || typeof idValue === "number" ? String(idValue) : "";

  const username = requireString(
    firstString(candidate, [
      "username",
      "account",
      "login_name",
      // TODO: replace with your real username/account field if different.
    ]),
    "username",
  );

  return {
    id: id || username,
    username,
    displayName:
      firstString(candidate, [
        "display_name",
        "displayName",
        "nickname",
        "name",
        // TODO: replace with your real display-name field if different.
      ]) ?? username,
    role:
      firstString(candidate, [
        "role",
        "role_name",
        "roleName",
        // TODO: replace with your real role field if different.
      ]) ?? "operator",
    email: firstString(candidate, [
      "email",
      "mail",
      // TODO: replace with your real email field if different.
    ]),
  };
}
