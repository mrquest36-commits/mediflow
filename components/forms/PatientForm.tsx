"use client";

import { useState } from "react";
import { FormInput, FormSelect, FormTextarea, FormSection, } from "@/components/ui/forms";
import { Patient } from "@/types/patient";
import { createPatient } from "@/services/patientService";




export default function PatientForm() {

  const [patient, setPatient] = useState<Patient>({
  firstName: "",
  lastName: "",
  phone: "",
  email: "",
  dateOfBirth: "",
  gender: "",
  identificationType: "",
  identificationNumber: "",
  emergencyContactName: "",
  emergencyContactRelationship: "",
  emergencyContactPhone: "",
  bloodGroup: "",
  allergies: "",
  existingConditions: "",
  medicalNotes: "",
});

const handleChange = (
  field: keyof Patient,
  value: string
) => {

  setPatient((previous) => ({
    ...previous,
    [field]: value,
  }));

};

  return (

    <form
  className="space-y-8"
  onSubmit={async (e)=>{

  e.preventDefault();


  const result = await createPatient(
    patient
  );


  console.log(result);

}}
>


      <FormSection
        title="Personal Information"
        description="Basic patient details and contact information."
      >

        <div className="grid md:grid-cols-2 gap-5">

          <FormInput
            label="First Name"
            placeholder="Enter first name"
            value={patient.firstName}
            onChange={(value)=>handleChange("firstName", value)}
          />

          <FormInput
            label="Last Name"
            placeholder="Enter last name"
            value={patient.lastName}
            onChange={(value)=>handleChange("lastName", value)}
          />

          <FormInput
            label="Phone Number"
            placeholder="Enter phone number"
            value={patient.phone}
            onChange={(value)=>handleChange("phone", value)}
          />

          <FormInput
            label="Email Address"
            placeholder="Enter email address"
            type="email"
            value={patient.email}
            onChange={(value)=>handleChange("email", value)}
          />
        </div>
      </FormSection>



      <FormSection
        title="Additional Information"
        description="More details about the patient."
      >

        <div className="grid md:grid-cols-2 gap-5">

          <FormInput
            label="Date of Birth"
            type="date"
            value={patient.dateOfBirth}
            onChange={(value)=>handleChange("dateOfBirth", value)}
          />


          <FormSelect
            label="Gender"
            options={[
              "Male",
              "Female",
              "Other",
            ]}
            value={patient.gender}
            onChange={(value)=>handleChange("gender", value)}
          />

        </div>

      </FormSection>




      <FormSection
        title="Identification Information"
        description="Government or official identification details."
      >

        <div className="grid md:grid-cols-2 gap-5">


          <FormSelect
            label="Identification Type"
            options={[
              "Ghana Card",
              "Passport",
              "Driver's License",
              "Other",
            ]}
            value={patient.identificationType}
            onChange={(value)=>handleChange("identificationType", value)}
          />


          <FormInput
            label="Identification Number"
            placeholder="Enter identification number"
            value={patient.identificationNumber}
            onChange={(value)=>handleChange("identificationNumber", value)}
          />


        </div>

      </FormSection>




      <FormSection
        title="Emergency Contact"
        description="Person to contact in case of emergency."
      >

        <div className="grid md:grid-cols-2 gap-5">


          <FormInput
            label="Contact Name"
            placeholder="Enter emergency contact name"
            value={patient.emergencyContactName}
            onChange={(value)=>handleChange("emergencyContactName", value)}
          />


          <FormInput
            label="Relationship"
            placeholder="Example: Parent, Spouse, Guardian"
            value={patient.emergencyContactRelationship}
            onChange={(value)=>handleChange("emergencyContactRelationship", value)}
          />


          <FormInput
            label="Phone Number"
            placeholder="Enter emergency contact phone number"
            value={patient.emergencyContactPhone}
            onChange={(value)=>handleChange("emergencyContactPhone", value)}
          />


        </div>

      </FormSection>




      <FormSection
        title="Medical Information"
        description="Health information that helps healthcare providers understand the patient."
      >

        <div className="grid md:grid-cols-2 gap-5">


          <FormSelect
            label="Blood Group"
            options={[
              "A+",
              "A-",
              "B+",
              "B-",
              "AB+",
              "AB-",
              "O+",
              "O-",
            ]}
            value={patient.bloodGroup}
            onChange={(value)=>handleChange("bloodGroup", value)}
          />


          <FormInput
            label="Allergies"
            placeholder="Enter known allergies"
            value={patient.allergies}
            onChange={(value)=>handleChange("allergies", value)}
          />


          <FormInput
            label="Existing Conditions"
            placeholder="Example: Asthma, Diabetes"
            value={patient.existingConditions}
            onChange={(value)=>handleChange("existingConditions", value)}
          />


        </div>



        <div className="mt-5">

          <FormTextarea
            label="Medical Notes"
            placeholder="Enter additional medical information"
            value={patient.medicalNotes}
            onChange={(value)=>handleChange("medicalNotes", value)}
          />

        </div>


      </FormSection>




      <button
        type="submit"
        className="
        bg-blue-600
        px-6
        py-3
        rounded-lg
        hover:bg-blue-700
        transition
        "
      >

        Save Patient

      </button>


    </form>

  );

}