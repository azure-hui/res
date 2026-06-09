import { http } from "@/lib/http"
import { unwrapResponse } from "@/lib/api"
import { DashboardOverview } from "@/types/dashboard"
import { ApiResponse } from "@/types/api"

export async function getDashboardOverview(storeId: number): Promise<DashboardOverview> {
  const res = await http.get<ApiResponse<DashboardOverview>>(
    `/api/v1/stores/${storeId}/dashboard/overview`
  )
  return unwrapResponse(res)
}