import { http } from "@/lib/http"
import { unwrapResponse } from "@/lib/api"
import { StoreListData } from "@/types/store"
import { ApiResponse } from "@/types/api"

export async function getStores(): Promise<StoreListData> {
  const res = await http.get<ApiResponse<StoreListData>>("/api/v1/stores")
  return unwrapResponse(res)
}