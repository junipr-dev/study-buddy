/**
 * Authentication store (React Native)
 */

import { create } from 'zustand';
import { authAPI } from '../api/auth';
import type { User, LoginCredentials, RegisterData } from '../types';

interface AuthState {
  user: User | null;
  isLoading: boolean;
  error: string | null;
  isInitialized: boolean;

  initialize: () => Promise<void>;
  login: (credentials: LoginCredentials) => Promise<void>;
  register: (data: RegisterData) => Promise<void>;
  logout: () => Promise<void>;
  clearError: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isLoading: false,
  error: null,
  isInitialized: false,

  initialize: async () => {
    try {
      const isAuth = await authAPI.isAuthenticated();
      if (isAuth) {
        const user = await authAPI.getCurrentUser();
        set({ user, isInitialized: true });
      } else {
        set({ isInitialized: true });
      }
    } catch {
      set({ isInitialized: true });
    }
  },

  login: async (credentials: LoginCredentials) => {
    set({ isLoading: true, error: null });
    try {
      await authAPI.login(credentials);
      const user = await authAPI.getCurrentUser();
      set({ user, isLoading: false });
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Login failed';
      set({ error: message, isLoading: false });
      throw err;
    }
  },

  register: async (data: RegisterData) => {
    set({ isLoading: true, error: null });
    try {
      await authAPI.register(data);
      // Auto-login after registration
      await authAPI.login({ username: data.username, password: data.password });
      const user = await authAPI.getCurrentUser();
      set({ user, isLoading: false });
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Registration failed';
      set({ error: message, isLoading: false });
      throw err;
    }
  },

  logout: async () => {
    await authAPI.logout();
    set({ user: null });
  },

  clearError: () => set({ error: null }),
}));
