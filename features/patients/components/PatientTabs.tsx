const tabs = [
  "Overview",
  "Medical History",
  "Appointments",
  "Consultations",
  "Prescriptions",
  "Billing",
];


export default function PatientTabs(){

  return (

    <div
      className="
      flex
      gap-3
      overflow-x-auto
      border-b
      border-white/10
      pb-3
      "
    >

      {
        tabs.map((tab)=>(

          <button
            key={tab}
            className="
            px-4
            py-2
            rounded-lg
            text-gray-300
            hover:bg-white/10
            transition
            "
          >
            {tab}
          </button>

        ))
      }

    </div>

  );

}