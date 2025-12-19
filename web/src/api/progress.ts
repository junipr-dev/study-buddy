/**
 * Progress tracking API calls
 */

import { api } from './client';
import type { ProgressSummary, MasteryRecord, WeakArea } from '../types';

export const progressAPI = {
  async getSummary(): Promise<ProgressSummary> {
    return api.get<ProgressSummary>('/progress');
  },

  async getSkillProgress(skillId: number): Promise<MasteryRecord> {
    return api.get<MasteryRecord>(`/progress/${skillId}`);
  },

  async getWeakAreas(): Promise<WeakArea[]> {
    return api.get<WeakArea[]>('/progress/weak-areas');
  },

  async getNextReviews(): Promise<MasteryRecord[]> {
    return api.get<MasteryRecord[]>('/progress/next-review');
  },
};
