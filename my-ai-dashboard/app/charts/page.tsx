"use client";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

import { PageShell } from "@/components/PageShell";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const revenueTrend = [
  { date: "2026-03-01", revenue: 120000, orders: 320 },
  { date: "2026-03-02", revenue: 132000, orders: 345 },
  { date: "2026-03-03", revenue: 128000, orders: 338 },
  { date: "2026-03-04", revenue: 141000, orders: 360 },
  { date: "2026-03-05", revenue: 156000, orders: 392 },
  { date: "2026-03-06", revenue: 149000, orders: 381 },
  { date: "2026-03-07", revenue: 162000, orders: 405 },
];

export default function ChartsPage() {
  return (
    <PageShell
      title={"\u56fe\u8868"}
      description={"\u6536\u5165\u4e0e\u8ba2\u5355\u8d8b\u52bf\uff08\u793a\u4f8b\u6570\u636e\uff09"}
    >
      <Card className="h-[420px]">
        <CardHeader>
          <CardTitle>{"\u6536\u5165\u4e0e\u8ba2\u5355\u8d8b\u52bf"}</CardTitle>
        </CardHeader>
        <CardContent className="h-[340px]">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={revenueTrend}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line
                type="monotone"
                dataKey="revenue"
                name="\u6536\u5165"
                stroke="#4f46e5"
                strokeWidth={2}
              />
              <Line
                type="monotone"
                dataKey="orders"
                name="\u8ba2\u5355"
                stroke="#16a34a"
                strokeWidth={2}
              />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </PageShell>
  );
}
