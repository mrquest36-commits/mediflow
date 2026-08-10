interface FormSelectProps {

  label:string;

  options:string[];

  value?: string;

  onChange?: (value:string)=>void;

}


export default function FormSelect({

  label,

  options,

  value = "",

  onChange,

}:FormSelectProps){


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


<select

value={value}

onChange={(event)=>{

  onChange?.(event.target.value);

}}

className="
w-full
rounded-lg
bg-white/5
text-white
border
border-white/10
px-4
py-3
outline-none
focus:border-blue-500
"

>


<option
value=""
className="text-black"
>
Select
</option>


{
options.map((option)=>(

<option

key={option}

value={option}

className="text-black"

>

{option}

</option>

))
}


</select>


</div>

);

}