import { useState, FormEvent } from 'react';
import { InlineMath } from 'react-katex';
import type { Question } from '../types';

interface QuestionCardProps {
  question: Question;
  onSubmit: (answer: string) => void;
  isLoading: boolean;
}

export default function QuestionCard({ question, onSubmit, isLoading }: QuestionCardProps) {
  const [answer, setAnswer] = useState('');

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (answer.trim()) {
      onSubmit(answer.trim());
      setAnswer('');
    }
  };

  // Parse and render text with LaTeX
  const renderQuestion = () => {
    const parts = question.question.split(/(\$[^$]+\$)/g);

    return (
      <p className="text-xl font-medium">
        {parts.map((part, index) => {
          if (part.startsWith('$') && part.endsWith('$')) {
            const math = part.slice(1, -1);
            return <InlineMath key={index} math={math} />;
          }
          return <span key={index}>{part}</span>;
        })}
      </p>
    );
  };

  return (
    <div className="card">
      <div className="mb-4">
        <span className="inline-block px-3 py-1 bg-primary bg-opacity-20 text-primary text-sm rounded-full">
          {question.skill_name}
        </span>
        <span className="ml-2 text-sm text-gray-400">
          Difficulty: {question.difficulty}/5
        </span>
      </div>

      <div className="mb-6">
        {renderQuestion()}
      </div>

      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="answer" className="block text-sm font-medium mb-2">
            Your Answer
          </label>
          <input
            id="answer"
            type="text"
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            className="w-full px-4 py-3 bg-background border border-gray-700 rounded-lg focus:outline-none focus:border-primary text-lg"
            placeholder="Enter your answer (e.g., 3, 1/2, or 1.5)"
            disabled={isLoading}
            autoFocus
          />
          <p className="text-sm text-gray-500 mt-2">
            For fractions, use format: 3/4 or 1/2
          </p>
        </div>

        <button
          type="submit"
          disabled={isLoading || !answer.trim()}
          className="w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {isLoading ? 'Checking...' : 'Submit Answer'}
        </button>
      </form>
    </div>
  );
}
