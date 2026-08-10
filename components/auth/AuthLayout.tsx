import { ReactNode } from "react";

interface AuthLayoutProps {
  title: string;
  description: string;
  children: ReactNode;
}

export default function AuthLayout({
  title,
  description,
  children,
}: AuthLayoutProps) {
  return (
    <main className="min-h-screen bg-slate-50 flex items-center justify-center px-6 py-12">
      <div className="w-full max-w-md">

        {/* Logo */}

        <div className="mb-10 text-center">

          <h1 className="text-3xl font-bold text-blue-600">
            MediFlow
          </h1>

          <p className="mt-2 text-sm text-slate-500">
            Clinic & Hospital Management Platform
          </p>

        </div>

        {/* Card */}

        <div className="rounded-2xl border border-slate-200 bg-white shadow-sm p-8">

          <div className="mb-8">

            <h2 className="text-3xl font-bold text-slate-900">
              {title}
            </h2>

            <p className="mt-2 text-slate-500">
              {description}
            </p>

          </div>

          {children}

        </div>

      </div>
    </main>
  );
}