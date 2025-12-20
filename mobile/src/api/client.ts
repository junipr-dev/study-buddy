/**
 * API Client for Study Buddy backend (React Native)
 */

import * as SecureStore from 'expo-secure-store';

const API_BASE_URL = 'https://study.junipr.io/api/study';

class APIClient {
  private async getAuthHeader(): Promise<Record<string, string>> {
    const token = await SecureStore.getItemAsync('access_token');
    return token ? { Authorization: `Bearer ${token}` } : {};
  }

  async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${API_BASE_URL}${endpoint}`;
    const authHeader = await this.getAuthHeader();

    const config: RequestInit = {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...authHeader,
        ...options.headers,
      },
    };

    const response = await fetch(url, config);

    if (!response.ok) {
      try {
        const error = await response.json();
        let message: string;
        if (typeof error === 'string') {
          message = error;
        } else if (typeof error.detail === 'string') {
          message = error.detail;
        } else if (Array.isArray(error.detail)) {
          message = error.detail.map((e: { msg?: string }) => e.msg || 'Validation error').join(', ');
        } else if (typeof error.message === 'string') {
          message = error.message;
        } else {
          message = `HTTP ${response.status}`;
        }
        throw new Error(message);
      } catch (e) {
        if (e instanceof Error && e.message && !e.message.startsWith('Unexpected')) {
          throw e;
        }
        throw new Error(`HTTP ${response.status}`);
      }
    }

    return response.json();
  }

  async get<T>(endpoint: string): Promise<T> {
    return this.request<T>(endpoint, { method: 'GET' });
  }

  async post<T>(endpoint: string, data?: unknown): Promise<T> {
    return this.request<T>(endpoint, {
      method: 'POST',
      body: data ? JSON.stringify(data) : undefined,
    });
  }

  async put<T>(endpoint: string, data?: unknown): Promise<T> {
    return this.request<T>(endpoint, {
      method: 'PUT',
      body: data ? JSON.stringify(data) : undefined,
    });
  }

  async delete<T>(endpoint: string): Promise<T> {
    return this.request<T>(endpoint, { method: 'DELETE' });
  }
}

export const api = new APIClient();
