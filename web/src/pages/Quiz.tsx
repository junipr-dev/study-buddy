import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { useQuizStore } from '../store/quizStore';
import { useEvaluationStore } from '../store/evaluationStore';
import QuestionCard from '../components/QuestionCard';
import FeedbackModal from '../components/FeedbackModal';
import SkillSelector from '../components/SkillSelector';
import ReportCard from '../components/ReportCard';

type Mode = 'practice' | 'evaluation';

export default function Quiz() {
  const { user } = useAuthStore();
  const [mode, setMode] = useState<Mode>('practice');

  // Practice mode store
  const quizStore = useQuizStore();

  // Evaluation mode store
  const evaluationStore = useEvaluationStore();

  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }

    // Fetch first question on mount in practice mode
    if (mode === 'practice' && !quizStore.currentQuestion && !quizStore.feedback) {
      quizStore.fetchNextQuestion();
    }
  }, [user, navigate, mode, quizStore]);

  // Mode switching handlers
  const handleStartEvaluation = async () => {
    setMode('evaluation');
    await evaluationStore.startEvaluation();
  };

  const handleExitEvaluation = () => {
    setMode('practice');
    evaluationStore.reset();
    // Fetch a new practice question
    quizStore.fetchNextQuestion();
  };

  // Practice mode handlers
  const handlePracticeSubmit = async (answer: string) => {
    await quizStore.submitAnswer(answer);
  };

  const handlePracticeContinue = () => {
    quizStore.clearFeedback();
    if (!quizStore.currentQuestion) {
      quizStore.fetchNextQuestion();
    }
  };

  const handleSelectSkill = (skillId: number | null) => {
    quizStore.setSelectedSkill(skillId);
    quizStore.fetchNextQuestion(skillId);
  };

  // Evaluation mode handlers
  const handleEvaluationSubmit = async (answer: string) => {
    const shouldContinue = await evaluationStore.submitAnswer(answer);
    // If shouldContinue is false, the evaluation ended and report will show
  };

  const handleCloseReport = () => {
    handleExitEvaluation();
  };

  if (!user) {
    return null; // Redirecting
  }

  // Determine which store to use based on mode
  const currentQuestion = mode === 'practice' ? quizStore.currentQuestion : evaluationStore.currentQuestion;
  const isLoading = mode === 'practice' ? quizStore.isLoading : evaluationStore.isLoading;
  const error = mode === 'practice' ? quizStore.error : evaluationStore.error;

  return (
    <div className="min-h-screen bg-background">
      <div className="max-w-3xl mx-auto py-8 px-4">
        {/* Header */}
        <header className="bg-surface border border-gray-800 rounded-t-lg px-6 py-4">
          <div className="flex items-center justify-between mb-4">
            <h1 className="text-2xl font-bold bg-gradient-to-r from-[#6B4FFF] to-[#FF6EC7] bg-clip-text text-transparent">
              Study Buddy
            </h1>
            <div className="flex items-center gap-4">
              <button
                onClick={() => navigate('/progress')}
                className="btn-secondary text-sm"
              >
                View Progress
              </button>
              <span className="text-gray-400">Hi, {user.username}</span>
            </div>
          </div>

          {/* Mode Switcher */}
          <div className="flex items-center gap-3">
            <div className="flex bg-background rounded-lg p-1 border border-gray-700">
              <button
                onClick={() => mode === 'evaluation' && handleExitEvaluation()}
                disabled={mode === 'practice'}
                className={`px-4 py-2 rounded text-sm font-medium transition-colors ${
                  mode === 'practice'
                    ? 'bg-primary text-white'
                    : 'text-gray-400 hover:text-gray-200'
                }`}
              >
                Practice Mode
              </button>
              <button
                onClick={handleStartEvaluation}
                disabled={mode === 'evaluation' || evaluationStore.isActive}
                className={`px-4 py-2 rounded text-sm font-medium transition-colors ${
                  mode === 'evaluation'
                    ? 'bg-secondary text-white'
                    : 'text-gray-400 hover:text-gray-200'
                }`}
              >
                Evaluation Mode
              </button>
            </div>

            {mode === 'practice' && (
              <p className="text-sm text-gray-500">
                Adaptive practice with personalized questions
              </p>
            )}
            {mode === 'evaluation' && (
              <p className="text-sm text-gray-500">
                Quick assessment to find your knowledge level
              </p>
            )}
          </div>

          {/* Evaluation Progress Bar */}
          {mode === 'evaluation' && evaluationStore.isActive && (
            <div className="mt-4">
              <div className="flex items-center justify-between text-sm text-gray-400 mb-2">
                <span>Evaluation Progress</span>
                <span>
                  {evaluationStore.currentSkillIndex + 1} / {evaluationStore.totalSkills}
                </span>
              </div>
              <div className="w-full bg-gray-700 rounded-full h-2">
                <div
                  className="bg-gradient-to-r from-[#6B4FFF] to-[#FF6EC7] h-2 rounded-full transition-all duration-500"
                  style={{
                    width: `${((evaluationStore.currentSkillIndex + 1) / evaluationStore.totalSkills) * 100}%`,
                  }}
                />
              </div>
            </div>
          )}
        </header>

        {/* Main Content */}
        <main className="bg-background px-6 py-8 border-x border-b border-gray-800 rounded-b-lg">
          {/* Skill Selector - Only in Practice Mode */}
          {mode === 'practice' && (
            <SkillSelector
              onSelectSkill={handleSelectSkill}
              selectedSkillId={quizStore.selectedSkillId}
            />
          )}

          {error && (
            <div className="bg-red-500 bg-opacity-10 border border-red-500 text-red-400 px-4 py-3 rounded-lg mb-6">
              {error}
            </div>
          )}

          {isLoading && !currentQuestion ? (
            <div className="card text-center py-12">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto mb-4"></div>
              <p className="text-gray-400">
                {mode === 'evaluation' ? 'Starting evaluation...' : 'Loading next question...'}
              </p>
            </div>
          ) : currentQuestion ? (
            <QuestionCard
              question={currentQuestion}
              onSubmit={mode === 'practice' ? handlePracticeSubmit : handleEvaluationSubmit}
              isLoading={isLoading}
            />
          ) : (
            <div className="card text-center py-12">
              <p className="text-gray-400 mb-4">No questions available</p>
              <button
                onClick={() => mode === 'practice' ? quizStore.fetchNextQuestion() : handleStartEvaluation()}
                className="btn-primary"
              >
                {mode === 'practice' ? 'Start Practicing' : 'Start Evaluation'}
              </button>
            </div>
          )}

          {/* Help Text */}
          <div className="mt-8 text-center text-sm text-gray-500">
            {mode === 'practice' ? (
              <p>💡 Tip: The more you practice, the better the adaptive algorithm gets at finding your weak spots!</p>
            ) : (
              <p>🎯 Evaluation Mode: Answer questions until you miss one to find your knowledge level</p>
            )}
          </div>
        </main>

        {/* Feedback Modal - Only in Practice Mode */}
        {mode === 'practice' && quizStore.feedback && (
          <FeedbackModal feedback={quizStore.feedback} onContinue={handlePracticeContinue} />
        )}

        {/* Report Card - Only in Evaluation Mode */}
        {mode === 'evaluation' && evaluationStore.showReport && evaluationStore.report && (
          <ReportCard report={evaluationStore.report} onClose={handleCloseReport} />
        )}
      </div>
    </div>
  );
}
