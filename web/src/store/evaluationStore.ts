/**
 * Evaluation mode state management
 */

import { create } from 'zustand';
import { evaluationAPI, type EvaluationReport } from '../api/evaluation';
import type { Question } from '../types';

interface EvaluationState {
  // Session data
  sessionId: string | null;
  totalSkills: number;
  currentSkillIndex: number;
  isActive: boolean;

  // Current question
  currentQuestion: Question | null;
  questionStartTime: number | null;

  // Results
  report: EvaluationReport | null;
  showReport: boolean;

  // UI state
  isLoading: boolean;
  error: string | null;

  // Actions
  startEvaluation: () => Promise<void>;
  fetchNextQuestion: () => Promise<void>;
  submitAnswer: (answer: string) => Promise<boolean>; // Returns true if continue, false if failed
  getReport: () => Promise<void>;
  reset: () => void;
}

export const useEvaluationStore = create<EvaluationState>((set, get) => ({
  sessionId: null,
  totalSkills: 0,
  currentSkillIndex: 0,
  isActive: false,
  currentQuestion: null,
  questionStartTime: null,
  report: null,
  showReport: false,
  isLoading: false,
  error: null,

  startEvaluation: async () => {
    set({ isLoading: true, error: null, isActive: true });
    try {
      const response = await evaluationAPI.start();
      set({
        sessionId: response.session_id,
        totalSkills: response.total_skills,
        currentSkillIndex: 0,
        isLoading: false,
      });

      // Fetch first question
      await get().fetchNextQuestion();
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to start evaluation',
        isLoading: false,
        isActive: false,
      });
    }
  },

  fetchNextQuestion: async () => {
    const { sessionId } = get();
    if (!sessionId) {
      set({ error: 'No active evaluation session' });
      return;
    }

    set({ isLoading: true, error: null });
    try {
      const question = await evaluationAPI.getNext(sessionId);
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

  submitAnswer: async (answer: string) => {
    const { sessionId, currentQuestion, questionStartTime, currentSkillIndex } = get();

    if (!sessionId || !currentQuestion) {
      set({ error: 'No active question' });
      return false;
    }

    set({ isLoading: true, error: null });
    try {
      const timeTaken = questionStartTime
        ? Math.floor((Date.now() - questionStartTime) / 1000)
        : undefined;

      const result = await evaluationAPI.submitAnswer(sessionId, {
        question_id: currentQuestion.question_id,
        answer,
        time_taken_seconds: timeTaken,
      });

      if (result.evaluation_complete) {
        // Evaluation ended - fetch report
        await get().getReport();
        set({
          isLoading: false,
          showReport: true,
          isActive: false,
        });
        return false; // Stop evaluation
      }

      if (result.is_correct) {
        // Correct - move to next skill
        set({
          currentSkillIndex: currentSkillIndex + 1,
          isLoading: false,
        });

        // Fetch next question
        await get().fetchNextQuestion();
        return true; // Continue evaluation
      }

      // This shouldn't happen but handle it
      return false;
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to submit answer',
        isLoading: false,
      });
      return false;
    }
  },

  getReport: async () => {
    const { sessionId } = get();
    if (!sessionId) return;

    set({ isLoading: true, error: null });
    try {
      const report = await evaluationAPI.getReport(sessionId);
      set({
        report,
        isLoading: false,
      });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to fetch report',
        isLoading: false,
      });
    }
  },

  reset: () => set({
    sessionId: null,
    totalSkills: 0,
    currentSkillIndex: 0,
    isActive: false,
    currentQuestion: null,
    questionStartTime: null,
    report: null,
    showReport: false,
    error: null,
  }),
}));
