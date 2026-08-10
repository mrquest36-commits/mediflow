interface FormInputProps {

  label: string;

  placeholder?: string;

  type?: string;

  value?: string;

  onChange?: (value: string) => void;

}


export default function FormInput({

  label,

  placeholder,

  type = "text",

  value = "",

  onChange,

}: FormInputProps) {


  return (

    <div className="space-y-2">


      <label
        className="
        text-sm
        text-gray-300
        "
      >
        {label}
      </label>


      <input

        type={type}

        value={value}

        onChange={(event)=>{

          onChange?.(event.target.value);

        }}

        placeholder={placeholder}

        className="
        w-full
        rounded-lg
        bg-white/5
        text-white
        placeholder:text-gray-500
        border
        border-white/10
        px-4
        py-3
        outline-none
        focus:border-blue-500
        "

      />


    </div>

  );

}