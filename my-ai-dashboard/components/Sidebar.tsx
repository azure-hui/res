"use client";

// components/Sidebar.tsx
import Link from "next/link";
import { usePathname } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Menu, Home, BarChart3, Users, Settings } from "lucide-react";

const navItems = [
  { icon: Home, label: "\u4eea\u8868\u76d8", href: "/" },
  { icon: BarChart3, label: "\u5206\u6790", href: "/analytics" },
  { icon: BarChart3, label: "\u56fe\u8868", href: "/charts" },
  { icon: Users, label: "\u95e8\u5e97", href: "/stores" },
  { icon: Settings, label: "\u8bbe\u7f6e", href: "/settings" },
];

export function Sidebar() {
  const pathname = usePathname();

  if (pathname === "/login") {
    return null;
  }

  return (
    <>
      <aside className="hidden md:block w-64 border-r bg-background">
        <div className="flex h-full flex-col">
          <div className="p-6">
            <h2 className="text-lg font-semibold">{"\u5bfc\u822a"}</h2>
          </div>
          <nav className="flex-1 px-3 py-4">
            {navItems.map((item) => (
              <Button
                key={item.href}
                variant="ghost"
                className="w-full justify-start gap-3 mb-1"
                asChild
              >
                <Link href={item.href}>
                  <item.icon className="h-5 w-5" />
                  {item.label}
                </Link>
              </Button>
            ))}
          </nav>
        </div>
      </aside>

      <Sheet>
        <SheetTrigger asChild className="md:hidden">
          <Button variant="outline" size="icon" className="fixed left-4 top-4 z-50">
            <Menu className="h-5 w-5" />
          </Button>
        </SheetTrigger>
        <SheetContent side="left" className="w-64 p-0">
          <div className="flex h-full flex-col">
            <div className="p-6 border-b">
              <h2 className="text-lg font-semibold">{"\u5bfc\u822a"}</h2>
            </div>
            <nav className="flex-1 p-3">
              {navItems.map((item) => (
                <Button
                  key={item.href}
                  variant="ghost"
                  className="w-full justify-start gap-3 mb-1"
                  asChild
                >
                  <Link href={item.href}>
                    <item.icon className="h-5 w-5" />
                    {item.label}
                  </Link>
                </Button>
              ))}
            </nav>
          </div>
        </SheetContent>
      </Sheet>
    </>
  );
}
