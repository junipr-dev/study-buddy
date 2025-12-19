/**
 * Questions API calls
 */

import { api } from './client';
import type { Question, AnswerSubmit, AnswerFeedback } from '../types';

export const questionsAPI = {
  async getNext(): Promise<Question> {
    return api.get<Question>('/questions/next');
  },

  async submitAnswer(data: AnswerSubmit): Promise<AnswerFeedback> {
    return api.post<AnswerFeedback>('/questions/answer', data);
  },

  async practiceSkill(skillId: number): Promise<Question> {
    return api.get<Question>(`/questions/practice/${skillId}`);
  },
};
