"use client";

import { ReactNode, useEffect, useState } from "react";
import { usePathname, useRouter } from "next/navigation";

import { getStoredSession } from "@/lib/auth";

export function AuthGuard({ children }: { children: ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();
  const [checked, setChecked] = useState(false);

  useEffect(() => {
    const session = getStoredSession();

    if (!session?.tokens.accessToken) {
      router.replace("/login");
      return;
    }

    setChecked(true);
  }, [pathname, router]);

  if (!checked) {
    return null;
  }

  return <>{children}</>;
}
