/**
 * Evaluation mode API client
 */

import { api } from './client';
import type { Question, AnswerSubmit } from '../types';

export interface EvaluationStartResponse {
  session_id: string;
  total_skills: number;
  skills: Array<{
    id: number;
    name: string;
    subject: string;
  }>;
}

export interface EvaluationAnswerResponse {
  is_correct: boolean;
  evaluation_complete: boolean;
  failed_at_skill?: string;
  correct_answer?: string;
  steps?: string[];
  all_passed?: boolean;
  skills_remaining?: number;
}

export interface EvaluationReport {
  session_id: string;
  total_skills: number;
  skills_tested: number;
  skills_passed: number;
  all_passed: boolean;
  failed_skill?: {
    skill_id: number;
    skill_name: string;
    user_answer: string;
    correct_answer: string;
  };
  passed_skills: Array<{
    skill_id: number;
    skill_name: string;
  }>;
  completion_percentage: number;
  started_at: string;
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
  async getNext(sessionId: string): Promise<Question> {
    return api.get<Question>(`/evaluation/next/${sessionId}`);
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
};
