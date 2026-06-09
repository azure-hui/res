export type UserRole = "admin" | "manager" | "operator" | string;

export type AuthMessage = {
  type: "success" | "error";
  text: string;
} | null;

export type AuthUser = {
  id: string;
  username: string;
  displayName: string;
  role: UserRole;
  email?: string;
};

export type AuthTokens = {
  accessToken: string;
  refreshToken?: string;
  tokenType: string;
  expiresAt?: string;
};

export type AuthSession = {
  user: AuthUser;
  tokens: AuthTokens;
  remember: boolean;
  loggedInAt: string;
};
