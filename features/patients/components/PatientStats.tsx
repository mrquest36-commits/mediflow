const stats = [
  {
    title: "Total Patients",
    value: "1,240",
  },

  {
    title: "New Patients",
    value: "86",
  },

  {
    title: "Active Patients",
    value: "1,102",
  },
];


export default function PatientStats(){

  return (

    <div className="
      grid
      md:grid-cols-3
      gap-5
    ">

      {
        stats.map((stat)=>(

          <div
            key={stat.title}
            className="
              rounded-xl
              border
              border-white/10
              bg-white/5
              p-6
            "
          >

            <p className="
              text-gray-400
              text-sm
            ">
              {stat.title}
            </p>


            <h2 className="
              text-3xl
              font-bold
              mt-3
            ">
              {stat.value}
            </h2>


          </div>

        ))
      }


    </div>

  );

}