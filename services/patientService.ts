import { Patient } from "@/types/patient";


export async function createPatient(
  patient: Patient
) {

  console.log(
    "Creating patient:",
    patient
  );


  // Temporary placeholder.
  // Later this will call our backend API.

  return {
    success: true,
    data: patient,
  };

}