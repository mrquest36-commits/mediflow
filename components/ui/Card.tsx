import { HTMLAttributes } from "react";

interface CardProps extends HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode;
}

export default function Card({
  children,
  className = "",
  ...props
}: CardProps) {
  return (
    <div
      className={`
        rounded-2xl
        border
        border-white/10
        bg-white/[0.03]
        backdrop-blur-sm
        p-6
        transition-all
        duration-300
        hover:border-blue-500/30
        hover:bg-white/[0.05]
        ${className}
      `}
      {...props}
    >
      {children}
    </div>
  );
}