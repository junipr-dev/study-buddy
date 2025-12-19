import { useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useAuthStore } from './store/authStore';
import Login from './pages/Login';
import Quiz from './pages/Quiz';
import Progress from './pages/Progress';
import './styles/globals.css';

function App() {
  const { checkAuth, user } = useAuthStore();

  useEffect(() => {
    checkAuth();
  }, [checkAuth]);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/quiz"
          element={user ? <Quiz /> : <Navigate to="/login" replace />}
        />
        <Route
          path="/progress"
          element={user ? <Progress /> : <Navigate to="/login" replace />}
        />
        <Route
          path="/"
          element={<Navigate to={user ? "/quiz" : "/login"} replace />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
