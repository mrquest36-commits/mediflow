export default function PatientRegistrationForm() {
  return (
    <div
      className="
        rounded-2xl
        border
        border-white/10
        bg-white/5
        p-8
      "
    >
      <h2 className="text-2xl font-semibold">
        Patient Registration
      </h2>

      <p className="mt-2 text-gray-400">
        Complete the patient's information below to create a new medical record.
      </p>
    </div>
  );
}