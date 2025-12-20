/**
 * Quiz store for practice mode (React Native)
 */

import { create } from 'zustand';
import { questionsAPI } from '../api/questions';
import type { Question, AnswerFeedback, Skill } from '../types';

interface QuizState {
  currentQuestion: Question | null;
  feedback: AnswerFeedback | null;
  skills: Skill[];
  selectedSkillId: number | null;
  isLoading: boolean;
  error: string | null;

  fetchSkills: () => Promise<void>;
  fetchNextQuestion: (skillId?: number | null) => Promise<void>;
  submitAnswer: (answer: string) => Promise<void>;
  setSelectedSkill: (skillId: number | null) => void;
  clearFeedback: () => void;
  reset: () => void;
}

export const useQuizStore = create<QuizState>((set, get) => ({
  currentQuestion: null,
  feedback: null,
  skills: [],
  selectedSkillId: null,
  isLoading: false,
  error: null,

  fetchSkills: async () => {
    try {
      const skills = await questionsAPI.getSkills();
      set({ skills });
    } catch (err) {
      console.error('Failed to fetch skills:', err);
    }
  },

  fetchNextQuestion: async (skillId?: number | null) => {
    set({ isLoading: true, error: null });
    try {
      const question = await questionsAPI.getNext(skillId ?? undefined);
      set({ currentQuestion: question, isLoading: false, feedback: null });
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to load question';
      set({ error: message, isLoading: false });
    }
  },

  submitAnswer: async (answer: string) => {
    const { currentQuestion } = get();
    if (!currentQuestion) return;

    set({ isLoading: true, error: null });
    try {
      const feedback = await questionsAPI.submitAnswer({
        question_id: currentQuestion.question_id,
        answer: answer.trim(),
      });
      set({
        feedback,
        isLoading: false,
        currentQuestion: feedback.next_question ?? null,
      });
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to submit answer';
      set({ error: message, isLoading: false });
    }
  },

  setSelectedSkill: (skillId: number | null) => {
    set({ selectedSkillId: skillId });
  },

  clearFeedback: () => set({ feedback: null }),

  reset: () => set({
    currentQuestion: null,
    feedback: null,
    selectedSkillId: null,
    isLoading: false,
    error: null,
  }),
}));
