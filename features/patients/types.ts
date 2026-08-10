export interface Patient {


  id: string;


  patientNumber: string;



  firstName: string;

  lastName: string;



  dateOfBirth: string;


  gender:
    | "male"
    | "female"
    | "other";



  phone: string;


  email?: string;


  address?: string;



  identification?: {

    type:
      | "ghana_card"
      | "passport"
      | "other";


    number: string;

  };



  emergencyContact?: {


    name: string;


    relationship: string;


    phone: string;


  };



  medicalInformation?: {


    bloodGroup?: string;


    allergies?: string;


    conditions?: string;


    notes?: string;


  };



  createdAt: string;


  updatedAt: string;


}