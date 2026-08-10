const information = [
  {
    label:"Date of Birth",
    value:"12 March 1998",
  },

  {
    label:"Gender",
    value:"Male",
  },

  {
    label:"Phone",
    value:"0240000000",
  },

  {
    label:"Address",
    value:"Accra, Ghana",
  },
];


export default function PatientInformation(){

  return (

    <div
      className="
      rounded-xl
      border
      border-white/10
      bg-white/5
      p-6
      "
    >

      <h2 className="text-xl font-semibold mb-6">
        Personal Information
      </h2>


      <div
        className="
        grid
        md:grid-cols-2
        gap-6
        "
      >

      {
        information.map((item)=>(

          <div key={item.label}>

            <p className="text-gray-400 text-sm">
              {item.label}
            </p>

            <p className="mt-1">
              {item.value}
            </p>

          </div>

        ))
      }

      </div>


    </div>

  );

}