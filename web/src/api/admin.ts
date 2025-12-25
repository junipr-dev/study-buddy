/**
 * Admin API client
 */

import { api } from './client';

export interface AdminStats {
  total_users: number;
  total_evaluations: number;
  active_users_7d: number;
  average_score: number;
  total_questions_answered: number;
  evaluations_today: number;
}

export interface UserSummary {
  id: number;
  username: string;
  first_name: string;
  is_admin: boolean;
  created_at: string;
  evaluation_count: number;
  questions_answered: number;
  latest_score: number | null;
  latest_eval_date: string | null;
}

export interface SkillStat {
  skill_name: string;
  subject: string;
  attempts: number;
  correct: number;
  accuracy: number;
}

export interface EvaluationDetail {
  id: number;
  completed_at: string;
  overall_score: number;
  total_questions: number;
  total_correct: number;
  skills_mastered: number;
  skills_review: number;
  skills_study: number;
  skill_results: {
    skill_name: string;
    subject: string;
    proficiency_score: number;
    proficiency_level: string;
  }[];
}

export interface UserDetail {
  id: number;
  username: string;
  first_name: string;
  is_admin: boolean;
  created_at: string;
  evaluations: EvaluationDetail[];
  skill_stats: SkillStat[];
}

export interface EvaluationSummary {
  id: number;
  user_id: number;
  username: string;
  first_name: string;
  completed_at: string;
  overall_score: number;
  total_questions: number;
  total_correct: number;
  skills_mastered: number;
  skills_review: number;
  skills_study: number;
}

export interface SkillPerformance {
  skill_name: string;
  subject: string;
  times_tested: number;
  avg_score: number;
  mastery_count: number;
  study_count: number;
  mastery_rate: number;
}

export interface AdminStatus {
  is_admin: boolean;
  admin_level: 'full' | 'readonly' | null;
  is_readonly: boolean;
}

export const adminAPI = {
  checkStatus: async (): Promise<AdminStatus> => {
    return api.get('/admin/check');
  },

  getStats: async (): Promise<AdminStats> => {
    return api.get('/admin/stats');
  },

  getUsers: async (limit = 50, offset = 0): Promise<{ users: UserSummary[]; total: number }> => {
    return api.get(`/admin/users?limit=${limit}&offset=${offset}`);
  },

  getUserDetail: async (userId: number): Promise<UserDetail> => {
    return api.get(`/admin/users/${userId}`);
  },

  toggleUserAdmin: async (userId: number): Promise<{ id: number; is_admin: boolean; admin_level: string }> => {
    return api.post(`/admin/users/${userId}/toggle-admin`);
  },

  getEvaluations: async (limit = 50, offset = 0): Promise<{ evaluations: EvaluationSummary[]; total: number }> => {
    return api.get(`/admin/evaluations?limit=${limit}&offset=${offset}`);
  },

  getSkillPerformance: async (): Promise<{ skills: SkillPerformance[] }> => {
    return api.get('/admin/skills/performance');
  },
};
