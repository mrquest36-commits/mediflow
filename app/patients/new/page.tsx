import PatientForm from "@/components/forms/PatientForm";


export default function NewPatientPage() {

  return (

    <div className="space-y-8">


      <div>

        <h1
          className="
          text-4xl
          font-bold
          "
        >
          Register Patient
        </h1>


        <p
          className="
          mt-2
          text-gray-400
          "
        >
          Create a new patient record.
        </p>


      </div>


      <PatientForm />


    </div>

  );

}