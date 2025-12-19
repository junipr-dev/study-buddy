// API Response Types

export interface User {
  id: number;
  username: string;
  created_at: string;
}

export interface LoginCredentials {
  username: string;
  password: string;
}

export interface RegisterData {
  username: string;
  password: string;
}

export interface TokenResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

export interface Skill {
  id: number;
  slug: string;
  name: string;
  subject: string;
  description: string;
  khan_url?: string;
  explanation?: string;
  difficulty_base: number;
}

export interface Question {
  question_id: string;
  skill_id: number;
  skill_name: string;
  question: string;
  difficulty: number;
  template_id: number;
}

export interface AnswerSubmit {
  question_id: string;
  answer: string;
  time_taken_seconds?: number;
}

export interface AnswerFeedback {
  is_correct: boolean;
  correct_answer: string;
  explanation?: string;
  steps?: string[];
  next_question?: Question;
}

export interface MasteryRecord {
  skill_id: number;
  skill_name: string;
  subject: string;
  mastery_score: number;
  total_attempts: number;
  correct_attempts: number;
  accuracy: number;
  last_practiced?: string;
  next_review?: string;
}

export interface ProgressSummary {
  total_questions_answered: number;
  overall_accuracy: number;
  skills_practiced: number;
  skills_mastered: number;
  skills_in_progress: number;
  skills_weak: number;
  mastery_by_skill: MasteryRecord[];
}

export interface WeakArea {
  skill_id: number;
  skill_name: string;
  subject: string;
  mastery_score: number;
  is_prerequisite_gap: boolean;
  dependent_skills: string[];
}
