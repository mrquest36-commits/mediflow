import { ButtonHTMLAttributes } from "react";

type ButtonVariant =
  | "primary"
  | "secondary"
  | "outline";

type ButtonSize =
  | "sm"
  | "md"
  | "lg";

interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
  loading?: boolean;
  fullWidth?: boolean;
}

export default function Button({
  children,
  variant = "primary",
  size = "md",
  loading = false,
  fullWidth = false,
  className = "",
  disabled,
  ...props
}: ButtonProps) {
  const baseStyles = `
    inline-flex
    items-center
    justify-center
    rounded-xl
    font-medium
    transition-all
    duration-200
    focus:outline-none
    disabled:opacity-50
    disabled:cursor-not-allowed
  `;

  const variants = {
    primary: `
      bg-blue-600
      text-white
      hover:bg-blue-700
    `,

    secondary: `
      bg-zinc-800
      text-white
      hover:bg-zinc-700
    `,

    outline: `
      border
      border-white/20
      text-white
      hover:bg-white/10
    `,
  };

  const sizes = {
    sm: "px-4 py-2 text-sm",

    md: "px-6 py-3 text-base",

    lg: "px-8 py-4 text-lg",
  };

  return (
    <button
      disabled={disabled || loading}
      className={`
        ${baseStyles}
        ${variants[variant]}
        ${sizes[size]}
        ${fullWidth ? "w-full" : ""}
        ${className}
      `}
      {...props}
    >
      {loading ? "Loading..." : children}
    </button>
  );
}