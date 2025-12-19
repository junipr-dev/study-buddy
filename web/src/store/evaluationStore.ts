/**
 * Evaluation mode state management - Adaptive Testing
 */

import { create } from 'zustand';
import { evaluationAPI } from '../api/evaluation';
import type { EvaluationReport, EvaluationProgress, EvaluationQuestion } from '../api/evaluation';

interface EvaluationState {
  // Session data
  sessionId: string | null;
  subjects: string[];
  skillsPerSubject: Record<string, number>;
  totalSkills: number;
  isActive: boolean;

  // Progress tracking
  progress: EvaluationProgress | null;

  // Section transition
  sectionChanged: boolean;
  completedSection: string | null;

  // Current question
  currentQuestion: EvaluationQuestion | null;
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
  submitAnswer: (answer: string) => Promise<boolean>;
  getReport: () => Promise<void>;
  clearSectionChange: () => void;
  reset: () => void;
}

const initialProgress: EvaluationProgress = {
  overall_completed: 0,
  overall_total: 0,
  overall_percent: 0,
  section_name: '',
  section_completed: 0,
  section_total: 0,
  section_percent: 0,
};

export const useEvaluationStore = create<EvaluationState>((set, get) => ({
  sessionId: null,
  subjects: [],
  skillsPerSubject: {},
  totalSkills: 0,
  isActive: false,
  progress: null,
  sectionChanged: false,
  completedSection: null,
  currentQuestion: null,
  questionStartTime: null,
  report: null,
  showReport: false,
  isLoading: false,
  error: null,

  startEvaluation: async () => {
    set({
      isLoading: true,
      error: null,
      isActive: true,
      showReport: false,
      report: null,
      sectionChanged: false,
      completedSection: null,
      progress: initialProgress,
    });
    try {
      const response = await evaluationAPI.start();
      set({
        sessionId: response.session_id,
        totalSkills: response.total_skills,
        subjects: response.subjects,
        skillsPerSubject: response.skills_per_subject,
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
        progress: question.progress,
        sectionChanged: question.section_changed,
        completedSection: question.completed_section,
        isLoading: false,
      });
    } catch (error) {
      // If no more questions, evaluation might be complete
      const errorMsg = error instanceof Error ? error.message : 'Failed to fetch question';
      if (errorMsg.includes('complete') || errorMsg.includes('No more')) {
        // Evaluation complete, fetch report
        await get().getReport();
        set({
          isLoading: false,
          showReport: true,
          isActive: false,
        });
      } else {
        set({
          error: errorMsg,
          isLoading: false,
        });
      }
    }
  },

  submitAnswer: async (answer: string) => {
    const { sessionId, currentQuestion, questionStartTime } = get();

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

      // Update progress
      set({
        progress: result.progress,
      });

      if (result.evaluation_complete) {
        // Evaluation ended - fetch report
        await get().getReport();
        set({
          isLoading: false,
          showReport: true,
          isActive: false,
        });
        return false;
      }

      // Continue - fetch next question
      set({ isLoading: false });
      await get().fetchNextQuestion();
      return true;
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

  clearSectionChange: () => set({
    sectionChanged: false,
    completedSection: null,
  }),

  reset: () => set({
    sessionId: null,
    subjects: [],
    skillsPerSubject: {},
    totalSkills: 0,
    isActive: false,
    progress: null,
    sectionChanged: false,
    completedSection: null,
    currentQuestion: null,
    questionStartTime: null,
    report: null,
    showReport: false,
    error: null,
  }),
}));
