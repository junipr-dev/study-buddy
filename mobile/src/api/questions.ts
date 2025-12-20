/**
 * Questions API client (React Native)
 */

import { api } from './client';
import type { Question, AnswerSubmit, AnswerFeedback, Skill } from '../types';

export const questionsAPI = {
  async getNext(skillId?: number): Promise<Question> {
    const url = skillId ? `/questions/next?skill_id=${skillId}` : '/questions/next';
    return api.get<Question>(url);
  },

  async submitAnswer(answerData: AnswerSubmit): Promise<AnswerFeedback> {
    return api.post<AnswerFeedback>('/questions/answer', answerData);
  },

  async getSkills(): Promise<Skill[]> {
    return api.get<Skill[]>('/skills');
  },
};
