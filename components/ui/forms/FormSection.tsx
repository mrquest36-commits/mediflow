interface FormSectionProps {
  title: string;
  description?: string;
  children: React.ReactNode;
}


export default function FormSection({
  title,
  description,
  children,
}: FormSectionProps) {

  return (
    <section
      className="
      rounded-2xl
      border
      border-white/10
      bg-white/5
      p-8
      "
    >

      <div className="mb-6">

        <h2 className="text-xl font-semibold">
          {title}
        </h2>


        {description && (
          <p className="text-gray-400 mt-2">
            {description}
          </p>
        )}

      </div>


      {children}

    </section>
  );
}