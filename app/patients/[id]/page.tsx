import PatientHeader 
from "@/features/patients/components/PatientHeader";

import PatientInformation 
from "@/features/patients/components/PatientInformation";

import PatientTabs 
from "@/features/patients/components/PatientTabs";


export default function PatientProfilePage(){

  return (

    <div className="space-y-8">


      <PatientHeader />


      <PatientTabs />


      <PatientInformation />


    </div>

  );

}