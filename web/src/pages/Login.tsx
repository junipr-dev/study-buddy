import { useState } from 'react';
import type { FormEvent } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';

export default function Login() {
  const [username, setUsername] = useState('');
  const [firstName, setFirstName] = useState('');
  const [password, setPassword] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);

  const { login, register, isLoading, error, clearError } = useAuthStore();
  const navigate = useNavigate();

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    clearError();

    try {
      let user;
      if (isRegistering) {
        user = await register({ username, first_name: firstName, password });
      } else {
        user = await login({ username, password });
      }
      // Redirect based on user type: admins → /admin, regular users → /quiz
      navigate(user.is_admin ? '/admin' : '/quiz', { replace: true });
    } catch (err) {
      // Error is handled by the store
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-background px-4 py-8 safe-area-inset">
      <div className="max-w-md w-full">
        <div className="text-center mb-6 sm:mb-10">
          <img
            src="/logo.png"
            alt="Study Buddy"
            className="h-20 sm:h-32 mx-auto mb-3 sm:mb-4"
          />
          <p className="text-base sm:text-lg text-gray-400">Your Adaptive Learning Companion</p>
        </div>

        <div className="card">
          <h2 className="text-2xl font-semibold mb-6 text-center">
            {isRegistering ? 'Create Account' : 'Sign In'}
          </h2>

          {error && (
            <div className="bg-red-500 bg-opacity-10 border border-red-500 text-red-400 px-4 py-3 rounded mb-4">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            {isRegistering && (
              <div>
                <label htmlFor="firstName" className="block text-sm font-medium mb-2">
                  First Name
                </label>
                <input
                  id="firstName"
                  type="text"
                  value={firstName}
                  onChange={(e) => setFirstName(e.target.value)}
                  className="w-full px-4 py-2 bg-background border border-gray-700 rounded-lg focus:outline-none focus:border-primary"
                  placeholder="Enter your first name"
                  required
                  minLength={1}
                />
                <p className="text-xs text-gray-500 mt-1">This cannot be changed later</p>
              </div>
            )}

            <div>
              <label htmlFor="username" className="block text-sm font-medium mb-2">
                Username
              </label>
              <input
                id="username"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="w-full px-4 py-2 bg-background border border-gray-700 rounded-lg focus:outline-none focus:border-primary"
                placeholder="Enter your username"
                required
                minLength={3}
              />
            </div>

            <div>
              <label htmlFor="password" className="block text-sm font-medium mb-2">
                Password
              </label>
              <input
                id="password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full px-4 py-2 bg-background border border-gray-700 rounded-lg focus:outline-none focus:border-primary"
                placeholder="Enter your password"
                required
                minLength={8}
              />
            </div>

            <button
              type="submit"
              disabled={isLoading}
              className="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isLoading ? 'Loading...' : isRegistering ? 'Create Account' : 'Sign In'}
            </button>
          </form>

          <div className="mt-6 text-center">
            <button
              onClick={() => {
                setIsRegistering(!isRegistering);
                clearError();
              }}
              className="text-sm text-secondary hover:text-white hover:font-semibold transition-all duration-200 outline-none focus:outline-none focus-visible:outline-none border-none focus:ring-0"
            >
              {isRegistering
                ? 'Already have an account? Sign in'
                : "Don't have an account? Create one"}
            </button>
          </div>
        </div>

        <p className="text-center text-gray-500 text-sm mt-8">
          Adaptive Learning • Personalized Practice • Track Your Progress
        </p>
      </div>
    </div>
  );
}
