import { HTMLAttributes } from "react";

interface ContainerProps extends HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode;
}

export default function Container({
  children,
  className = "",
  ...props
}: ContainerProps) {
  return (
    <div
      className={`
        w-full
        max-w-7xl
        mx-auto
        px-6
        md:px-8
        ${className}
      `}
      {...props}
    >
      {children}
    </div>
  );
}