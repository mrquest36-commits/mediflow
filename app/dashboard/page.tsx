import AppShell from "@/components/shared/AppShell";
import SectionHeading from "@/components/ui/SectionHeading";
import Card from "@/components/ui/Card";


export default function DashboardPage() {
  return (
    <AppShell>

      <SectionHeading
        eyebrow="Overview"
        title="Clinic Dashboard"
        description="Monitor patients, appointments and healthcare operations from one place."
      />


      <div
        className="
          grid
          md:grid-cols-2
          lg:grid-cols-4
          gap-6
        "
      >

        <Card>
          <p className="text-gray-400 text-sm">
            Total Patients
          </p>

          <p className="text-3xl font-bold mt-2">
            1,240
          </p>
        </Card>


        <Card>
          <p className="text-gray-400 text-sm">
            Today's Appointments
          </p>

          <p className="text-3xl font-bold mt-2">
            48
          </p>
        </Card>


        <Card>
          <p className="text-gray-400 text-sm">
            Active Doctors
          </p>

          <p className="text-3xl font-bold mt-2">
            12
          </p>
        </Card>


        <Card>
          <p className="text-gray-400 text-sm">
            Pending Records
          </p>

          <p className="text-3xl font-bold mt-2">
            7
          </p>
        </Card>


      </div>


    </AppShell>
  );
}