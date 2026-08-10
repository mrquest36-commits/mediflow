"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

import { navigation } from "@/lib/navigation";
import { UserRole } from "@/types/auth";


export default function Sidebar() {

const pathname = usePathname();

const role: UserRole = "doctor";

const menuItems = navigation[role];


  return (
    <aside
      className="
      hidden
      md:flex
      w-64
      min-h-screen
      border-r
      border-white/10
      bg-white/5
      flex-col
      p-6
      "
    >

      <div
        className="
        text-2xl
        font-bold
        mb-10
        "
      >
        Medi
        <span className="text-blue-500">
          Flow
        </span>
      </div>


      <nav className="space-y-6">

{
 menuItems.map((section)=>(

  <div key={section.title}>


    <p
      className="
      text-xs
      text-gray-500
      mb-3
      px-3
      "
    >
      {section.title}
    </p>


    <div className="space-y-2">


    {
      section.items.map((item)=>{

const Icon = item.icon;


return (

<Link

key={item.href}

href={item.href}

className={`
flex
items-center
gap-3
px-4
py-3
rounded-lg
transition

${
pathname === item.href
? "bg-blue-500/20 text-blue-400"
: "text-gray-300 hover:bg-white/10"
}

`}

>

<Icon size={18}/>

<span>
{item.label}
</span>


</Link>

);

})
    }


    </div>


  </div>

 ))
}

</nav>


    </aside>
  );
}