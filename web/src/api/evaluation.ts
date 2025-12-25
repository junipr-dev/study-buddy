/**
 * Evaluation mode API client
 */

import { api } from './client';
import type { Question, AnswerSubmit } from '../types';

export interface EvaluationProgress {
  overall_completed: number;
  overall_total: number;
  overall_percent: number;
  section_name: string;
  section_completed: number;
  section_total: number;
  section_percent: number;
  section_index?: number;
  total_sections?: number;
}

export interface EvaluationStartResponse {
  session_id: string;
  total_skills: number;
  subjects: string[];
  skills_per_subject: Record<string, number>;
}

export interface EvaluationQuestion extends Question {
  progress: EvaluationProgress;
  section_changed: boolean;
  completed_section: string | null;
}

export interface EvaluationAnswerResponse {
  is_correct: boolean;
  correct_answer: string;
  steps?: string[];
  skill_completed: boolean;
  evaluation_complete: boolean;
  advanced_level: boolean;
  current_level: number;
  highest_passed: number;
  attempts_at_level: number;
  progress: EvaluationProgress;
}

export interface SkillResult {
  skill_id: number;
  skill_name: string;
  subject: string;
  highest_level_passed?: number;
  proficiency_score: number;
  proficiency_level: 'mastered' | 'proficient' | 'developing' | 'study';
  questions_correct: number;
  questions_total: number;
}

export interface EvaluationReport {
  evaluation_id?: number;
  session_id?: string;
  overall_score: number;
  total_skills_tested: number;
  total_questions: number;
  total_correct: number;
  skills_mastered: number;
  skills_proficient?: number;
  skills_developing?: number;
  skills_need_study: number;
  study: SkillResult[];
  developing?: SkillResult[];
  proficient?: SkillResult[];
  mastered: SkillResult[];
  all_skills: SkillResult[];
  started_at: string;
  completed_at: string;
  study_recommendation: string;
  by_subject?: Record<string, {
    skills: SkillResult[];
    mastered: number;
    proficient: number;
    developing: number;
    study: number;
  }>;
}

export interface EvaluationSummary {
  id: number;
  completed_at: string;
  overall_score: number;
  total_questions: number;
  total_correct: number;
  skills_mastered: number;
  skills_review: number;
  skills_study: number;
}

export interface EvaluationHistoryResponse {
  evaluations: EvaluationSummary[];
  total_evaluations: number;
}

export interface SkillSummary {
  skill_id: number;
  skill_name: string;
  proficiency_score: number;
}

export interface LatestEvaluationResponse {
  latest: {
    id: number;
    completed_at: string;
    overall_score: number;
    total_questions: number;
    total_correct: number;
    skills_mastered: number;
    skills_review: number;
    skills_study: number;
    study: SkillSummary[];
    developing: SkillSummary[];
    proficient: SkillSummary[];
    mastered: SkillSummary[];
  } | null;
  previous: {
    id: number;
    completed_at: string;
    overall_score: number;
  } | null;
  improvement: {
    score_change: number;
    mastered_change: number;
    days_between: number;
  } | null;
}

export const evaluationAPI = {
  /**
   * Start a new evaluation session
   */
  async start(): Promise<EvaluationStartResponse> {
    return api.post<EvaluationStartResponse>('/evaluation/start', {});
  },

  /**
   * Get next evaluation question
   */
  async getNext(sessionId: string): Promise<EvaluationQuestion> {
    return api.get<EvaluationQuestion>(`/evaluation/next/${sessionId}`);
  },

  /**
   * Submit answer for evaluation question
   */
  async submitAnswer(
    sessionId: string,
    answerData: AnswerSubmit
  ): Promise<EvaluationAnswerResponse> {
    return api.post<EvaluationAnswerResponse>(
      `/evaluation/answer/${sessionId}`,
      answerData
    );
  },

  /**
   * Get evaluation report card
   */
  async getReport(sessionId: string): Promise<EvaluationReport> {
    return api.get<EvaluationReport>(`/evaluation/report/${sessionId}`);
  },

  /**
   * Get evaluation history
   */
  async getHistory(limit: number = 10): Promise<EvaluationHistoryResponse> {
    return api.get<EvaluationHistoryResponse>(`/evaluation/history?limit=${limit}`);
  },

  /**
   * Get latest evaluation with comparison
   */
  async getLatest(): Promise<LatestEvaluationResponse> {
    return api.get<LatestEvaluationResponse>('/evaluation/history/latest');
  },

  /**
   * Get a saved evaluation by ID
   */
  async getSavedEvaluation(evaluationId: number): Promise<EvaluationReport> {
    return api.get<EvaluationReport>(`/evaluation/history/${evaluationId}`);
  },
};
