import type { AuthSession } from "@/types/auth";

const AUTH_STORAGE_KEY = "restaurantos_auth_session";

function isBrowser() {
  return typeof window !== "undefined";
}

function safeParse(raw: string | null): AuthSession | null {
  if (!raw) return null;

  try {
    return JSON.parse(raw) as AuthSession;
  } catch {
    return null;
  }
}

export function getStoredSession(): AuthSession | null {
  if (!isBrowser()) return null;

  const localSession = safeParse(window.localStorage.getItem(AUTH_STORAGE_KEY));
  if (localSession) return localSession;

  const sessionSession = safeParse(window.sessionStorage.getItem(AUTH_STORAGE_KEY));
  if (sessionSession) return sessionSession;

  clearStoredSession();
  return null;
}

export function saveStoredSession(session: AuthSession) {
  if (!isBrowser()) return;

  clearStoredSession();
  const storage = session.remember ? window.localStorage : window.sessionStorage;
  storage.setItem(AUTH_STORAGE_KEY, JSON.stringify(session));
}

export function clearStoredSession() {
  if (!isBrowser()) return;

  window.localStorage.removeItem(AUTH_STORAGE_KEY);
  window.sessionStorage.removeItem(AUTH_STORAGE_KEY);
}

export function getAccessToken(): string | null {
  return getStoredSession()?.tokens.accessToken ?? null;
}
