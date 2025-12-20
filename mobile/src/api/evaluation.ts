/**
 * Evaluation mode API client (React Native)
 */

import { api } from './client';
import type {
  AnswerSubmit,
  EvaluationStartResponse,
  EvaluationQuestion,
  EvaluationAnswerResponse,
  EvaluationReport,
  LatestEvaluationResponse,
} from '../types';

export const evaluationAPI = {
  async start(): Promise<EvaluationStartResponse> {
    return api.post<EvaluationStartResponse>('/evaluation/start', {});
  },

  async getNext(sessionId: string): Promise<EvaluationQuestion> {
    return api.get<EvaluationQuestion>(`/evaluation/next/${sessionId}`);
  },

  async submitAnswer(
    sessionId: string,
    answerData: AnswerSubmit
  ): Promise<EvaluationAnswerResponse> {
    return api.post<EvaluationAnswerResponse>(
      `/evaluation/answer/${sessionId}`,
      answerData
    );
  },

  async getReport(sessionId: string): Promise<EvaluationReport> {
    return api.get<EvaluationReport>(`/evaluation/report/${sessionId}`);
  },

  async getLatest(): Promise<LatestEvaluationResponse> {
    return api.get<LatestEvaluationResponse>('/evaluation/history/latest');
  },
};
