import Link from "next/link";

import {
  PatientStats,
  PatientSearch,
  PatientTable,
} from "@/features/patients";


export default function PatientsPage(){

  return (

    <div className="space-y-8">


      <div>

        <h1 className="
          text-4xl
          font-bold
        ">
          Patients
        </h1>


        <p className="
          text-gray-400
          mt-2
        ">
          Manage patient records and healthcare information.
        </p>


        <Link

          href="/patients/new"

          className="
          inline-flex
          mt-6
          bg-blue-600
          px-5
          py-3
          rounded-lg
          hover:bg-blue-700
          transition
          "
        >
          + Register Patient

        </Link>


      </div>



      <PatientStats />


      <PatientSearch />


      <PatientTable />


    </div>

  );

}