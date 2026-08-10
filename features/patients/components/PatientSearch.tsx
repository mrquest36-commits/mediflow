"use client";


export default function PatientSearch(){

  return (

    <input

      type="text"

      placeholder="Search patients..."

      className="
        w-full
        rounded-xl
        bg-white/5
        border
        border-white/10
        px-5
        py-3
        text-white
        outline-none
        focus:border-blue-500
      "

    />

  );

}