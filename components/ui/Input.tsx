import { InputHTMLAttributes, forwardRef } from "react";

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {}

const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className = "", ...props }, ref) => {
    return (
      <input
        ref={ref}
        className={`
          w-full
          rounded-xl
          border
          border-white/10
          bg-white/[0.03]
          px-4
          py-3
          text-white
          placeholder:text-gray-500
          outline-none
          transition-all
          duration-300
          focus:border-blue-500
          focus:ring-2
          focus:ring-blue-500/20
          ${className}
        `}
        {...props}
      />
    );
  }
);

Input.displayName = "Input";

export default Input;