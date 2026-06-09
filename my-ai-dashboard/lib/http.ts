import axios from "axios";

import { clearStoredSession, getAccessToken } from "@/lib/auth";

export const http = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000",
  timeout: 10000,
});

http.interceptors.request.use((config) => {
  const token = getAccessToken();

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

http.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error?.response?.status === 401) {
      clearStoredSession();
    }

    return Promise.reject(error);
  },
);
