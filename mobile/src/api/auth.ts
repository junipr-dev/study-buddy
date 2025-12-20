/**
 * Authentication API calls (React Native)
 */

import * as SecureStore from 'expo-secure-store';
import { api } from './client';
import type { User, LoginCredentials, RegisterData, TokenResponse } from '../types';

export const authAPI = {
  async login(credentials: LoginCredentials): Promise<TokenResponse> {
    const response = await api.post<TokenResponse>('/auth/login', credentials);

    // Store tokens securely
    await SecureStore.setItemAsync('access_token', response.access_token);
    await SecureStore.setItemAsync('refresh_token', response.refresh_token);

    return response;
  },

  async register(data: RegisterData): Promise<User> {
    return api.post<User>('/auth/register', data);
  },

  async getCurrentUser(): Promise<User> {
    return api.get<User>('/auth/me');
  },

  async refreshToken(): Promise<TokenResponse> {
    const refreshToken = await SecureStore.getItemAsync('refresh_token');
    if (!refreshToken) {
      throw new Error('No refresh token available');
    }

    const response = await api.post<TokenResponse>('/auth/refresh', {
      refresh_token: refreshToken,
    });

    await SecureStore.setItemAsync('access_token', response.access_token);
    await SecureStore.setItemAsync('refresh_token', response.refresh_token);

    return response;
  },

  async logout(): Promise<void> {
    await SecureStore.deleteItemAsync('access_token');
    await SecureStore.deleteItemAsync('refresh_token');
  },

  async isAuthenticated(): Promise<boolean> {
    const token = await SecureStore.getItemAsync('access_token');
    return !!token;
  },
};
