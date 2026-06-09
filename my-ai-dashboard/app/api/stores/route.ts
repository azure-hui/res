// app/api/stores/route.ts
import { NextResponse, NextRequest } from "next/server";

interface TrendPoint {
  date: string;
  sales: number;
}

interface Store {
  id: string;
  name: string;
  sales: string;
  orders: number;
  status: string;
  trend: string;
  trendData: TrendPoint[];
}

const mockStores: Store[] = [
  {
    id: "1",
    name: "\u5357\u57ce\u4e00\u5e97",
    sales: "\u00a51,450,000",
    orders: 380,
    status: "\u589e\u957f",
    trend: "+18%",
    trendData: [
      { date: "2026-03-01", sales: 1200000 },
      { date: "2026-03-02", sales: 1350000 },
      { date: "2026-03-03", sales: 1450000 },
      { date: "2026-03-04", sales: 1380000 },
      { date: "2026-03-05", sales: 1520000 },
    ],
  },
  {
    id: "2",
    name: "\u6ee8\u6c5f\u4e8c\u5e97",
    sales: "\u00a51,120,000",
    orders: 290,
    status: "\u4e0b\u6ed1",
    trend: "-5%",
    trendData: [
      { date: "2026-03-01", sales: 950000 },
      { date: "2026-03-02", sales: 980000 },
      { date: "2026-03-03", sales: 1120000 },
      { date: "2026-03-04", sales: 1050000 },
      { date: "2026-03-05", sales: 980000 },
    ],
  },
  {
    id: "3",
    name: "\u9ad8\u65b0\u4e09\u5e97",
    sales: "\u00a5890,000",
    orders: 210,
    status: "\u589e\u957f",
    trend: "+9%",
    trendData: [
      { date: "2026-03-01", sales: 800000 },
      { date: "2026-03-02", sales: 820000 },
      { date: "2026-03-03", sales: 850000 },
      { date: "2026-03-04", sales: 870000 },
      { date: "2026-03-05", sales: 890000 },
    ],
  },
];

export async function GET(request: NextRequest) {
  const { searchParams } = request.nextUrl;
  const startDate = searchParams.get("startDate");
  const endDate = searchParams.get("endDate");

  let filteredStores = [...mockStores];

  if (startDate && endDate) {
    filteredStores = filteredStores.map((store) => ({
      ...store,
      trendData: store.trendData.filter(
        (d) => d.date >= startDate && d.date <= endDate
      ),
    }));
  }

  await new Promise((resolve) => setTimeout(resolve, 800));

  return NextResponse.json({
    data: filteredStores,
    timestamp: new Date().toISOString(),
  });
}
