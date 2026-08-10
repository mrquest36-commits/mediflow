"use client";

import Sidebar from "@/components/dashboard/Sidebar";
import DashboardHeader from "@/components/dashboard/DashboardHeader";

interface AppShellProps {
  children: React.ReactNode;
}

export default function AppShell({
  children,
}: AppShellProps) {
  return (
    <div className="min-h-screen bg-black text-white flex">

      <Sidebar />

      <div className="flex-1 flex flex-col">

        <DashboardHeader />

        <main className="
          flex-1
          p-6
          md:p-8
        ">
          {children}
        </main>

      </div>

    </div>
  );
}