export default function PatientHeader(){

  return (

    <div
      className="
      rounded-2xl
      border
      border-white/10
      bg-white/5
      p-8
      "
    >

      <div>

        <h1
          className="
          text-3xl
          font-bold
          "
        >
          John Mensah
        </h1>


        <p className="text-gray-400 mt-2">
          Patient ID: MF-2026-000001
        </p>


      </div>


      <span
        className="
        inline-block
        mt-5
        px-4
        py-2
        rounded-full
        bg-green-500/20
        text-green-400
        text-sm
        "
      >
        Active
      </span>


    </div>

  );

}