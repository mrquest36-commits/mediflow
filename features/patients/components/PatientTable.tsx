import Link from "next/link";



const patients = [

{
 id:"1",
 patientNumber:"MF-2026-000001",
 name:"John Mensah",
 gender:"Male",
 phone:"0240000000",
},

{
 id:"2",
 patientNumber:"MF-2026-000002",
 name:"Ama Owusu",
 gender:"Female",
 phone:"0200000000",
},

];


export default function PatientTable(){

  return (

    <div
      className="
      overflow-hidden
      rounded-xl
      border
      border-white/10
      "
    >

      <table className="w-full">


        <thead
          className="
          bg-white/5
          text-gray-400
          "
        >

          <tr
            className="
            border-t
            border-white/10
            hover:bg-white/5
            transition
            cursor-pointer
            "
          >

            <th className="text-left p-4">
              Patient ID
            </th>

            <th className="text-left p-4">
              Name
            </th>

            <th className="text-left p-4">
              Gender
            </th>

            <th className="text-left p-4">
              Phone
            </th>


          </tr>

        </thead>


        <tbody>


        {
          patients.map((patient)=>(

            <Link
              key={patient.patientNumber}
              href={`/patients/${patient.id}`}
              className="
              contents"
            >

              <td className="p-4">
                {patient.id}
              </td>


              <td className="p-4">
                {patient.name}
              </td>


              <td className="p-4">
                {patient.gender}
              </td>


              <td className="p-4">
                {patient.phone}
              </td>


            </Link>

          ))
        }


        </tbody>


      </table>


    </div>

  );

}