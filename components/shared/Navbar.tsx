import Logo from "./Logo";

export default function Navbar() {
  return (
    <nav
      className="
        border-b
        border-white/10
        bg-black/40
        backdrop-blur-lg
      "
    >

      <div
        className="
          max-w-7xl
          mx-auto
          px-6
          md:px-8
          h-20
          flex
          items-center
          justify-between
        "
      >

        <Logo />


        <div
          className="
            flex
            items-center
            gap-4
          "
        >

          <button
            className="
              text-sm
              text-gray-400
              hover:text-white
              transition
            "
          >
            Sign In
          </button>


          <button
            className="
              rounded-xl
              bg-blue-600
              px-5
              py-2.5
              text-sm
              font-medium
              hover:bg-blue-700
              transition
            "
          >
            Get Started
          </button>

        </div>

      </div>

    </nav>
  );
}