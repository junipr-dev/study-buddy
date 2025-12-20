// API Response Types

export interface User {
  id: number;
  username: string;
  first_name: string;
  created_at: string;
}

export interface LoginCredentials {
  username: string;
  password: string;
}

export interface RegisterData {
  username: string;
  first_name: string;
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
  user_answer: string;
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

// Evaluation Types

export interface EvaluationProgress {
  overall_completed: number;
  overall_total: number;
  overall_percent: number;
  section_name: string;
  section_completed: number;
  section_total: number;
  section_percent: number;
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
