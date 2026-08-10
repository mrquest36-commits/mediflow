interface LoadingProps {
  text?: string;
}

export default function Loading({
  text = "Loading...",
}: LoadingProps) {
  return (
    <div
      className="
        flex
        flex-col
        items-center
        justify-center
        py-10
        text-gray-400
      "
    >

      <div
        className="
          h-8
          w-8
          rounded-full
          border-4
          border-blue-500/30
          border-t-blue-500
          animate-spin
          mb-4
        "
      />

      <p className="text-sm">
        {text}
      </p>

    </div>
  );
}