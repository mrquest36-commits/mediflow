import { ReactNode } from "react";

type Variant =
  | "primary"
  | "success"
  | "warning"
  | "danger"
  | "neutral";

interface BadgeProps {
  children: ReactNode;
  variant?: Variant;
  className?: string;
}

export default function Badge({
  children,
  variant = "neutral",
  className = "",
}: BadgeProps) {
  const variants = {
    primary:
      "bg-blue-100 text-blue-700",

    success:
      "bg-green-100 text-green-700",

    warning:
      "bg-amber-100 text-amber-700",

    danger:
      "bg-red-100 text-red-700",

    neutral:
      "bg-slate-100 text-slate-700",
  };

  return (
    <span
      className={`
        inline-flex
        items-center
        rounded-full
        px-3
        py-1
        text-xs
        font-medium
        ${variants[variant]}
        ${className}
      `}
    >
      {children}
    </span>
  );
}