export default function DashboardHeader() {

  return (
    <header
      className="
      h-20
      border-b
      border-white/10
      flex
      items-center
      justify-between
      px-6
      md:px-8
      "
    >

      <div>
        <p className="text-sm text-gray-400">
          Good morning
        </p>

        <h2 className="font-semibold">
          Dr. Mensah
        </h2>
      </div>


      <div
        className="
        w-10
        h-10
        rounded-full
        bg-blue-600
        flex
        items-center
        justify-center
        "
      >
        DM
      </div>


    </header>
  );
}