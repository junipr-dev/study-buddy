import { BlockMath } from 'react-katex';
import type { AnswerFeedback } from '../types';

interface FeedbackModalProps {
  feedback: AnswerFeedback;
  onContinue: () => void;
}

export default function FeedbackModal({ feedback, onContinue }: FeedbackModalProps) {
  const hasLatex = feedback.correct_answer.includes('$') || feedback.correct_answer.includes('\\');

  return (
    <div className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center p-4 z-50">
      <div className="bg-surface border border-gray-800 rounded-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div className="p-6">
          {/* Result Header */}
          <div className={`text-center mb-6 p-4 rounded-lg ${
            feedback.is_correct
              ? 'bg-success bg-opacity-10 border border-success'
              : 'bg-red-500 bg-opacity-10 border border-red-500'
          }`}>
            <h2 className={`text-3xl font-bold ${
              feedback.is_correct ? 'text-success' : 'text-red-400'
            }`}>
              {feedback.is_correct ? '✓ Correct!' : '✗ Not Quite'}
            </h2>
          </div>

          {/* Correct Answer */}
          {!feedback.is_correct && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-2">Correct Answer:</h3>
              <div className="bg-background p-4 rounded-lg">
                {hasLatex ? (
                  <BlockMath math={feedback.correct_answer.replace(/\$/g, '')} />
                ) : (
                  <p className="text-2xl font-bold text-primary">{feedback.correct_answer}</p>
                )}
              </div>
            </div>
          )}

          {/* Solution Steps */}
          {feedback.steps && feedback.steps.length > 0 && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-3">Solution Steps:</h3>
              <div className="bg-background p-4 rounded-lg space-y-2">
                {feedback.steps.map((step, index) => (
                  <div key={index} className="flex items-start">
                    <span className="inline-block w-6 h-6 bg-primary bg-opacity-20 text-primary rounded-full text-center text-sm mr-3 flex-shrink-0">
                      {index + 1}
                    </span>
                    <p className="text-gray-300">{step}</p>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Explanation */}
          {feedback.explanation && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-2">Learn More:</h3>
              <div className="bg-background p-4 rounded-lg">
                <p className="text-gray-300 leading-relaxed">
                  {feedback.explanation.substring(0, 300)}
                  {feedback.explanation.length > 300 && '...'}
                </p>
              </div>
            </div>
          )}

          {/* Continue Button */}
          <button
            onClick={onContinue}
            className="w-full btn-primary text-lg py-3"
          >
            {feedback.next_question ? 'Next Question →' : 'Continue'}
          </button>
        </div>
      </div>
    </div>
  );
}
