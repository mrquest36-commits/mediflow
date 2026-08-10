export default function Logo() {
  return (
    <div
      className="
        flex
        items-center
        gap-2
        font-bold
        text-xl
      "
    >

      <div
        className="
          h-9
          w-9
          rounded-xl
          bg-blue-600
          flex
          items-center
          justify-center
          text-white
        "
      >
        M
      </div>


      <span>
        Medi
        <span className="text-blue-500">
          Flow
        </span>
      </span>

    </div>
  );
}