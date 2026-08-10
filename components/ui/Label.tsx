import { LabelHTMLAttributes } from "react";

interface LabelProps extends LabelHTMLAttributes<HTMLLabelElement> {}

export default function Label({
  className = "",
  ...props
}: LabelProps) {
  return (
    <label
      className={`
        mb-2
        block
        text-sm
        font-medium
        text-slate-700
        ${className}
      `}
      {...props}
    />
  );
}