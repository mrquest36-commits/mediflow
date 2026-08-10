import {
  LayoutDashboard,
  Users,
  CalendarDays,
  Stethoscope,
  FileText,
  Settings,
  UserCog,
  ClipboardList,
} from "lucide-react";

import { UserRole } from "@/types/auth";


export const navigation = {

  admin: [

    {
      title: "MAIN",
      items: [
        {
          label: "Dashboard",
          href: "/dashboard",
          icon: LayoutDashboard,
          permission: "view_dashboard",
        },
      ],
    },


    {
      title: "PATIENT CARE",
      items: [
        {
          label: "Patients",
          href: "/patients",
          icon: Users,
          permission: "view_patients",
        },

        {
          label: "Appointments",
          href: "/appointments",
          icon: CalendarDays,
          permission: "view_appointments",
        },
      ],
    },


    {
      title: "CLINICAL",
      items: [

        {
          label: "Consultations",
          href: "/consultations",
          icon: Stethoscope,
          permission: "create_consultation",
        },

        {
          label: "Prescriptions",
          href: "/prescriptions",
          icon: FileText,
          permission: "create_prescription",
        },

      ],
    },


    {
      title: "ADMINISTRATION",

      items: [

        {
          label: "Staff Management",
          href: "/staff",
          icon: UserCog,
          permission: "manage_staff",
        },

        {
          label: "Reports",
          href: "/reports",
          icon: ClipboardList,
          permission: "view_reports",
        },

        {
          label: "Settings",
          href: "/settings",
          icon: Settings,
          permission: "manage_settings",
        },

      ],
    },

  ],



  doctor: [

    {
      title: "MAIN",

      items: [
        {
          label:"Dashboard",
          href:"/dashboard",
          icon:LayoutDashboard,
          permission:"view_dashboard",
        },
      ],
    },


    {
      title:"PATIENT CARE",

      items:[
        {
          label:"Patients",
          href:"/patients",
          icon:Users,
          permission:"view_patients",
        },

        {
          label:"Appointments",
          href:"/appointments",
          icon:CalendarDays,
          permission:"view_appointments",
        },
      ],
    },


    {
      title:"CLINICAL",

      items:[
        {
          label:"Consultations",
          href:"/consultations",
          icon:Stethoscope,
          permission:"create_consultation",
        },

        {
          label:"Prescriptions",
          href:"/prescriptions",
          icon:FileText,
          permission:"create_prescription",
        },
      ],
    },

  ],

  nurse: [

    {
      title: "MAIN",

      items: [
        {
          label: "Dashboard",
          href: "/dashboard",
          icon: LayoutDashboard,
          permission: "view_dashboard",
        },
      ],
    },


    {
      title: "PATIENT CARE",

      items: [
        {
          label: "Patients",
          href: "/patients",
          icon: Users,
          permission: "view_patients",
        },

        {
          label: "Queue",
          href: "/queue",
          icon: CalendarDays,
          permission: "manage_queue",
        },
      ],
    },


    {
      title: "CLINICAL",

      items: [
        {
          label: "Vitals",
          href: "/vitals",
          icon: Stethoscope,
          permission: "manage_vitals",
        },
      ],
    },

  ],



  receptionist: [

    {
      title: "MAIN",

      items: [
        {
          label: "Dashboard",
          href: "/dashboard",
          icon: LayoutDashboard,
          permission: "view_dashboard",
        },
      ],
    },


    {
      title: "FRONT DESK",

      items: [
        {
          label: "Patients",
          href: "/patients",
          icon: Users,
          permission: "view_patients",
        },

        {
          label: "Appointments",
          href: "/appointments",
          icon: CalendarDays,
          permission: "manage_appointments",
        },
      ],
    },

  ],



  pharmacist: [

    {
      title: "MAIN",

      items: [
        {
          label: "Dashboard",
          href: "/dashboard",
          icon: LayoutDashboard,
          permission: "view_dashboard",
        },
      ],
    },


    {
      title: "PHARMACY",

      items: [

        {
          label: "Prescriptions",
          href: "/prescriptions",
          icon: FileText,
          permission: "view_prescriptions",
        },

        {
          label: "Inventory",
          href: "/inventory",
          icon: ClipboardList,
          permission: "manage_inventory",
        },

      ],
    },

  ],

} satisfies Record<UserRole, any[]>;