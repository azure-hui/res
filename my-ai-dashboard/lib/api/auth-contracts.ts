export const authContracts = {
  login: "/api/v1/auth/login",
  me: "/api/v1/auth/me",
  refresh: "/api/v1/auth/refresh",
  logout: "/api/v1/auth/logout",
  forgotPassword: "/api/v1/auth/forgot-password",
} as const;
