import AuthLayout from "@/components/auth/AuthLayout";
import LoginForm from "@/features/auth/components/LoginForm";

export default function LoginPage() {
  return (
    <AuthLayout
      title="Welcome Back"
      description="Sign in to access the MediFlow dashboard."
    >
      <LoginForm />
    </AuthLayout>
  );
}