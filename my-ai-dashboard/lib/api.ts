import type { AxiosResponse } from "axios";

import { ApiResponse } from "@/types/api";

export function unwrapResponse<T>(response: AxiosResponse<ApiResponse<T>>): T {
  const payload = response.data;

  if (payload.code !== "0") {
    throw new Error(payload.message || "请求失败");
  }

  return payload.data;
}
