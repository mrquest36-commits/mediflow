interface SectionHeadingProps {
  eyebrow?: string;
  title: string;
  description?: string;
}

export default function SectionHeading({
  eyebrow,
  title,
  description,
}: SectionHeadingProps) {
  return (
    <div className="max-w-3xl mb-10">

      {eyebrow && (
        <p className="
          text-blue-400
          text-sm
          font-medium
          mb-3
        ">
          {eyebrow}
        </p>
      )}


      <h2 className="
        text-3xl
        md:text-4xl
        font-bold
        tracking-tight
      ">
        {title}
      </h2>


      {description && (
        <p className="
          mt-4
          text-gray-400
          leading-relaxed
        ">
          {description}
        </p>
      )}

    </div>
  );
}