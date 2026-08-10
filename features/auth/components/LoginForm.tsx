"use client";

import Button from "@/components/ui/Button";
import Input from "@/components/ui/Input";
import Label from "@/components/ui/Label";

export default function LoginForm() {
  return (
    <form className="space-y-6">

      <div>

        <Label htmlFor="email">
          Email Address
        </Label>

        <Input
          id="email"
          type="email"
          placeholder="doctor@hospital.com"
        />

      </div>

      <div>

        <Label htmlFor="password">
          Password
        </Label>

        <Input
          id="password"
          type="password"
          placeholder="Enter your password"
        />

      </div>

      <div className="flex items-center justify-between">

        <label className="flex items-center gap-2 text-sm text-slate-600">

          <input
            type="checkbox"
            className="rounded"
          />

          Remember me

        </label>

        <button
          type="button"
          className="text-sm text-blue-600 hover:text-blue-700"
        >
          Forgot Password?
        </button>

      </div>

      <Button
        type="submit"
        className="w-full"
      >
        Sign In
      </Button>

    </form>
  );
}