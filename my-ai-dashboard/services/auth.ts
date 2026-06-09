import { AxiosError } from "axios";

import { authContracts } from "@/lib/api/auth-contracts";
import { mapAuthUser, mapLoginTokens } from "@/lib/api/auth-mappers";
import { clearStoredSession, getStoredSession, saveStoredSession } from "@/lib/auth";
import { http } from "@/lib/http";
import type { AuthSession } from "@/types/auth";

export async function login(account: string, password: string, remember: boolean): Promise<AuthSession> {
  const response = await http.post(authContracts.login, {
    username: account,
    password,
    // TODO: if your backend uses different request fields, adjust only this request body.
  });

  const tokens = mapLoginTokens(response.data);
  const user = mapAuthUser(response.data);

  const session: AuthSession = {
    user,
    tokens,
    remember,
    loggedInAt: new Date().toISOString(),
  };

  saveStoredSession(session);
  return session;
}

export async function getMe() {
  const response = await http.get(authContracts.me);
  const user = mapAuthUser(response.data);

  const currentSession = getStoredSession();
  if (!currentSession) return user;

  saveStoredSession({
    ...currentSession,
    user,
  });

  return user;
}

export async function refreshSession(): Promise<AuthSession | null> {
  const currentSession = getStoredSession();
  const refreshToken = currentSession?.tokens.refreshToken;

  if (!currentSession || !refreshToken) {
    return null;
  }

  const response = await http.post(authContracts.refresh, {
    refresh_token: refreshToken,
    // TODO: if your backend uses a different refresh field, adjust only this request body.
  });

  const tokens = mapLoginTokens(response.data);
  const session: AuthSession = {
    ...currentSession,
    tokens: {
      ...currentSession.tokens,
      ...tokens,
      refreshToken: tokens.refreshToken ?? currentSession.tokens.refreshToken,
    },
  };

  saveStoredSession(session);
  return session;
}

export async function logout() {
  const session = getStoredSession();

  try {
    if (session?.tokens.refreshToken) {
      await http.post(authContracts.logout, {
        refresh_token: session.tokens.refreshToken,
      });
    }
  } catch (error) {
    if (!(error instanceof AxiosError)) {
      throw error;
    }
  } finally {
    clearStoredSession();
  }
}
