/**
 * Quiz state management
 */

import { create } from 'zustand';
import { questionsAPI } from '../api/questions';
import type { Question, AnswerFeedback } from '../types';

interface QuizState {
  currentQuestion: Question | null;
  feedback: AnswerFeedback | null;
  isLoading: boolean;
  error: string | null;
  questionStartTime: number | null;
  selectedSkillId: number | null;

  fetchNextQuestion: (skillId?: number | null) => Promise<void>;
  submitAnswer: (answer: string) => Promise<void>;
  clearFeedback: () => void;
  setSelectedSkill: (skillId: number | null) => void;
  reset: () => void;
}

export const useQuizStore = create<QuizState>((set, get) => ({
  currentQuestion: null,
  feedback: null,
  isLoading: false,
  error: null,
  questionStartTime: null,
  selectedSkillId: null,

  fetchNextQuestion: async (skillId?: number | null) => {
    set({ isLoading: true, error: null, feedback: null });
    try {
      const useSkillId = skillId !== undefined ? skillId : get().selectedSkillId;
      const question = useSkillId
        ? await questionsAPI.practiceSkill(useSkillId)
        : await questionsAPI.getNext();

      set({
        currentQuestion: question,
        questionStartTime: Date.now(),
        isLoading: false,
      });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to fetch question',
        isLoading: false,
      });
    }
  },

  setSelectedSkill: (skillId: number | null) => {
    set({ selectedSkillId: skillId });
  },

  submitAnswer: async (answer: string) => {
    const { currentQuestion, questionStartTime } = get();
    if (!currentQuestion) return;

    set({ isLoading: true, error: null });
    try {
      const timeTaken = questionStartTime
        ? Math.floor((Date.now() - questionStartTime) / 1000)
        : undefined;

      const feedback = await questionsAPI.submitAnswer({
        question_id: currentQuestion.question_id,
        answer,
        time_taken_seconds: timeTaken,
      });

      set({
        feedback,
        currentQuestion: feedback.next_question || null,
        questionStartTime: feedback.next_question ? Date.now() : null,
        isLoading: false,
      });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to submit answer',
        isLoading: false,
      });
    }
  },

  clearFeedback: () => set({ feedback: null }),

  reset: () => set({
    currentQuestion: null,
    feedback: null,
    error: null,
    questionStartTime: null,
  }),
}));
