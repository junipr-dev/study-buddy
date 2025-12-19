/**
 * Authentication state management
 */

import { create } from 'zustand';
import { authAPI } from '../api/auth';
import type { User, LoginCredentials, RegisterData } from '../types';

interface AuthState {
  user: User | null;
  isLoading: boolean;
  error: string | null;

  login: (credentials: LoginCredentials) => Promise<void>;
  register: (data: RegisterData) => Promise<void>;
  logout: () => void;
  checkAuth: () => Promise<void>;
  clearError: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isLoading: false,
  error: null,

  login: async (credentials) => {
    set({ isLoading: true, error: null });
    try {
      await authAPI.login(credentials);
      const user = await authAPI.getCurrentUser();
      set({ user, isLoading: false });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Login failed',
        isLoading: false,
      });
      throw error;
    }
  },

  register: async (data) => {
    set({ isLoading: true, error: null });
    try {
      const user = await authAPI.register(data);
      // Auto-login after registration
      await authAPI.login({ username: data.username, password: data.password });
      set({ user, isLoading: false });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Registration failed',
        isLoading: false,
      });
      throw error;
    }
  },

  logout: () => {
    authAPI.logout();
    set({ user: null, error: null });
  },

  checkAuth: async () => {
    if (!authAPI.isAuthenticated()) {
      set({ user: null });
      return;
    }

    set({ isLoading: true });
    try {
      const user = await authAPI.getCurrentUser();
      set({ user, isLoading: false });
    } catch (error) {
      // Token might be expired, try to refresh
      try {
        await authAPI.refreshToken();
        const user = await authAPI.getCurrentUser();
        set({ user, isLoading: false });
      } catch {
        authAPI.logout();
        set({ user: null, isLoading: false });
      }
    }
  },

  clearError: () => set({ error: null }),
}));
