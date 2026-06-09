"use client";

import { PageShell } from "@/components/PageShell";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";

const rows = [
  { store: "\u95e8\u5e97 A", revenue: "\u00a5128,000", orders: 338, status: "\u589e\u957f" },
  { store: "\u95e8\u5e97 B", revenue: "\u00a596,000", orders: 271, status: "\u7a33\u5b9a" },
  { store: "\u95e8\u5e97 C", revenue: "\u00a572,500", orders: 205, status: "\u98ce\u9669" },
];

export default function AnalyticsPage() {
  return (
    <PageShell
      title={"\u5206\u6790"}
      description={"\u95e8\u5e97\u7ecf\u8425\u7ed3\u679c\u5feb\u7167"}
    >
      <Card>
        <CardHeader>
          <CardTitle>{"\u95e8\u5e97\u6982\u89c8"}</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>{"\u95e8\u5e97"}</TableHead>
                <TableHead>{"\u6536\u5165"}</TableHead>
                <TableHead>{"\u8ba2\u5355"}</TableHead>
                <TableHead>{"\u72b6\u6001"}</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {rows.map((row) => (
                <TableRow key={row.store}>
                  <TableCell>{row.store}</TableCell>
                  <TableCell>{row.revenue}</TableCell>
                  <TableCell>{row.orders}</TableCell>
                  <TableCell>{row.status}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </PageShell>
  );
}
