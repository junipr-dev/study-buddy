import { useEffect } from 'react';
import { BlockMath, InlineMath } from 'react-katex';
import type { AnswerFeedback } from '../types';

interface FeedbackModalProps {
  feedback: AnswerFeedback;
  onContinue: () => void;
}

export default function FeedbackModal({ feedback, onContinue }: FeedbackModalProps) {
  const hasLatex = feedback.correct_answer.includes('$') || feedback.correct_answer.includes('\\');

  // Render a step that may contain mixed text and LaTeX
  const renderStep = (step: string) => {
    // Check if step starts with ** (bold markdown)
    const isBold = step.startsWith('**') && step.includes('**', 2);
    let content = step;
    let boldClass = '';

    if (isBold) {
      // Extract content between **...**
      const match = step.match(/\*\*(.+?)\*\*/);
      if (match) {
        content = match[1];
        boldClass = 'font-bold text-primary';
      }
    }

    // Split by LaTeX delimiters
    const parts = content.split(/(\$[^$]+\$)/g);

    return (
      <div className={boldClass}>
        {parts.map((part, index) => {
          if (part.startsWith('$') && part.endsWith('$')) {
            const math = part.slice(1, -1);
            // Check if it contains fraction or complex expression - use block math
            if (math.includes('\\frac') || math.includes('=') && math.length > 10) {
              return (
                <div key={index} className="my-2">
                  <BlockMath math={math} />
                </div>
              );
            }
            // Otherwise use inline
            return <InlineMath key={index} math={math} />;
          }
          return <span key={index}>{part}</span>;
        })}
      </div>
    );
  };

  // Auto-advance after 1.3 seconds if correct
  useEffect(() => {
    if (feedback.is_correct) {
      const timer = setTimeout(() => {
        onContinue();
      }, 1300);
      return () => clearTimeout(timer);
    }
  }, [feedback.is_correct, onContinue]);

  // Show quick success flash for correct answers
  if (feedback.is_correct) {
    return (
      <div className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center p-4 z-50 animate-correctFlash">
        <div className="bg-success bg-opacity-20 border-4 border-success rounded-2xl p-12">
          <h2 className="text-6xl font-bold text-success text-center">
            ✓ Correct!
          </h2>
        </div>
      </div>
    );
  }

  // Show full feedback modal for incorrect answers
  return (
    <div className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center p-4 z-50">
      <div className="bg-surface border border-gray-800 rounded-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div className="p-6">
          {/* Result Header */}
          <div className="text-center mb-6 p-4 rounded-lg bg-red-500 bg-opacity-10 border border-red-500">
            <h2 className="text-3xl font-bold text-red-400">
              ✗ Not Quite
            </h2>
          </div>

          {/* User's Answer and Correct Answer */}
          <div className="mb-6 space-y-4">
            <div>
              <h3 className="text-lg font-semibold mb-2">Your Answer:</h3>
              <div className="bg-background p-4 rounded-lg border-2 border-red-500 border-opacity-30">
                <p className="text-2xl font-bold text-red-400">{feedback.user_answer}</p>
              </div>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-2">Correct Answer:</h3>
              <div className="bg-background p-4 rounded-lg border-2 border-success border-opacity-30">
                {hasLatex ? (
                  <BlockMath math={feedback.correct_answer.replace(/\$/g, '')} />
                ) : (
                  <p className="text-2xl font-bold text-success">{feedback.correct_answer}</p>
                )}
              </div>
            </div>
          </div>

          {/* Solution Steps */}
          {feedback.steps && feedback.steps.length > 0 && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-3">Solution Steps:</h3>
              <div className="bg-background p-6 rounded-lg space-y-4">
                {feedback.steps.map((step, index) => (
                  <div key={index} className="flex items-start gap-3">
                    <span className="inline-flex items-center justify-center w-7 h-7 bg-primary bg-opacity-20 text-primary rounded-full text-sm font-semibold flex-shrink-0 mt-1">
                      {index + 1}
                    </span>
                    <div className="text-gray-200 flex-1 leading-relaxed">
                      {renderStep(step)}
                    </div>
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
