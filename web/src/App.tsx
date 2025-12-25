import { useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useAuthStore } from './store/authStore';
import Login from './pages/Login';
import Quiz from './pages/Quiz';
import Progress from './pages/Progress';
import Admin from './pages/Admin';
import './styles/globals.css';

// Protected route wrapper
function RequireAuth({ children }: { children: React.ReactElement }) {
  const { user } = useAuthStore();

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  return children;
}

function AppRoutes() {
  const { checkAuth, user, isLoading } = useAuthStore();

  useEffect(() => {
    checkAuth();
  }, [checkAuth]);

  // Show loading while checking auth
  if (isLoading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
      </div>
    );
  }

  return (
    <Routes>
      <Route path="/login" element={user ? <Navigate to="/quiz" replace /> : <Login />} />
      <Route
        path="/quiz"
        element={<RequireAuth><Quiz /></RequireAuth>}
      />
      <Route
        path="/progress"
        element={<RequireAuth><Progress /></RequireAuth>}
      />
      <Route
        path="/admin"
        element={<RequireAuth><Admin /></RequireAuth>}
      />
      <Route
        path="/"
        element={<Navigate to={user ? "/quiz" : "/login"} replace />}
      />
    </Routes>
  );
}

function App() {
  return (
    <BrowserRouter>
      <AppRoutes />
    </BrowserRouter>
  );
}

export default App;
