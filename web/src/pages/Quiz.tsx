import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { useQuizStore } from '../store/quizStore';
import QuestionCard from '../components/QuestionCard';
import FeedbackModal from '../components/FeedbackModal';

export default function Quiz() {
  const { user } = useAuthStore();
  const {
    currentQuestion,
    feedback,
    isLoading,
    error,
    fetchNextQuestion,
    submitAnswer,
    clearFeedback,
  } = useQuizStore();

  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }

    // Fetch first question on mount
    if (!currentQuestion && !feedback) {
      fetchNextQuestion();
    }
  }, [user, navigate, currentQuestion, feedback, fetchNextQuestion]);

  const handleSubmitAnswer = async (answer: string) => {
    await submitAnswer(answer);
  };

  const handleContinue = () => {
    clearFeedback();
    if (!currentQuestion) {
      fetchNextQuestion();
    }
  };

  if (!user) {
    return null; // Redirecting
  }

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="bg-surface border-b border-gray-800">
        <div className="max-w-4xl mx-auto px-4 py-4 flex items-center justify-between">
          <h1 className="text-2xl font-bold text-primary">Study Buddy</h1>
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
      </header>

      {/* Main Content */}
      <main className="max-w-3xl mx-auto px-4 py-8">
        {error && (
          <div className="bg-red-500 bg-opacity-10 border border-red-500 text-red-400 px-4 py-3 rounded-lg mb-6">
            {error}
          </div>
        )}

        {isLoading && !currentQuestion ? (
          <div className="card text-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto mb-4"></div>
            <p className="text-gray-400">Loading next question...</p>
          </div>
        ) : currentQuestion ? (
          <QuestionCard
            question={currentQuestion}
            onSubmit={handleSubmitAnswer}
            isLoading={isLoading}
          />
        ) : (
          <div className="card text-center py-12">
            <p className="text-gray-400 mb-4">No questions available</p>
            <button onClick={fetchNextQuestion} className="btn-primary">
              Start Practicing
            </button>
          </div>
        )}

        {/* Help Text */}
        <div className="mt-8 text-center text-sm text-gray-500">
          <p>💡 Tip: The more you practice, the better the adaptive algorithm gets at finding your weak spots!</p>
        </div>
      </main>

      {/* Feedback Modal */}
      {feedback && (
        <FeedbackModal feedback={feedback} onContinue={handleContinue} />
      )}
    </div>
  );
}
