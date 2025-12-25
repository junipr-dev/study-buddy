import { useEffect, useState } from 'react';

interface EvaluationProgressProps {
  currentSection: string;
  sectionIndex: number;
  totalSections: number;
  questionsInSection: number;
  questionsCompletedInSection: number;
  overallProgress: number; // 0-100
  estimatedMinutesRemaining?: number;
  onSectionComplete?: (sectionName: string) => void;
}

// Encouraging messages for section transitions
const SECTION_MESSAGES = [
  "Great start! Keep it up! 💪",
  "You're doing amazing! 🌟",
  "Fantastic progress! 🎯",
  "Almost there! You've got this! 🚀",
  "Incredible work! 🔥",
  "Final stretch! Finish strong! ⭐",
];

export default function EvaluationProgress({
  currentSection,
  sectionIndex,
  totalSections,
  questionsInSection,
  questionsCompletedInSection,
  overallProgress,
  estimatedMinutesRemaining,
}: EvaluationProgressProps) {
  const [showSectionTransition, setShowSectionTransition] = useState(false);
  const [prevSection, setPrevSection] = useState(currentSection);

  // Detect section change
  useEffect(() => {
    if (currentSection !== prevSection && prevSection) {
      setShowSectionTransition(true);
      const timer = setTimeout(() => {
        setShowSectionTransition(false);
      }, 2000);
      setPrevSection(currentSection);
      return () => clearTimeout(timer);
    }
    setPrevSection(currentSection);
  }, [currentSection, prevSection]);

  return (
    <div className="w-full space-y-3">
      {/* Section transition message */}
      {showSectionTransition && (
        <div className="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-40 animate-bounceIn">
          <div className="bg-primary bg-opacity-95 px-8 py-4 rounded-xl shadow-2xl border border-primary-light">
            <p className="text-xl font-bold text-white text-center">
              {SECTION_MESSAGES[Math.min(sectionIndex, SECTION_MESSAGES.length - 1)]}
            </p>
            <p className="text-sm text-gray-200 text-center mt-1">
              Moving to {currentSection}
            </p>
          </div>
        </div>
      )}

      {/* Main progress display */}
      <div className="bg-surface rounded-lg p-3 sm:p-4 border border-gray-800">
        {/* Section info */}
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <span className="text-xs sm:text-sm font-medium text-primary">
              Section {sectionIndex + 1} of {totalSections}
            </span>
            <span className="text-gray-600">•</span>
            <span className="text-xs sm:text-sm font-semibold text-white truncate max-w-[120px] sm:max-w-none">
              {currentSection}
            </span>
          </div>

          {/* Estimated time */}
          {estimatedMinutesRemaining !== undefined && (
            <span className="text-xs text-gray-500 hidden sm:inline">
              ~{estimatedMinutesRemaining} min left
            </span>
          )}
        </div>

        {/* Section dots */}
        <div className="flex gap-1.5 mb-3">
          {Array.from({ length: totalSections }).map((_, i) => (
            <div
              key={i}
              className={`
                h-1.5 flex-1 rounded-full transition-all duration-500
                ${i < sectionIndex ? 'bg-success' : ''}
                ${i === sectionIndex ? 'bg-gradient-to-r from-primary to-secondary' : ''}
                ${i > sectionIndex ? 'bg-gray-700' : ''}
              `}
            />
          ))}
        </div>

        {/* Overall progress bar */}
        <div className="relative h-2 bg-gray-800 rounded-full overflow-hidden">
          <div
            className="absolute inset-y-0 left-0 bg-gradient-to-r from-primary via-secondary to-accent rounded-full transition-all duration-500 ease-out"
            style={{ width: `${overallProgress}%` }}
          />
          {/* Shimmer effect */}
          <div
            className="absolute inset-y-0 left-0 bg-gradient-to-r from-transparent via-white/20 to-transparent rounded-full animate-shimmer"
            style={{ width: `${overallProgress}%` }}
          />
        </div>

        {/* Progress stats */}
        <div className="flex items-center justify-between mt-2 text-xs text-gray-500">
          <span>
            {questionsCompletedInSection}/{questionsInSection} in section
          </span>
          <span className="font-medium text-primary">
            {Math.round(overallProgress)}% complete
          </span>
        </div>
      </div>
    </div>
  );
}

// Compact version for mobile header
export function EvaluationProgressCompact({
  overallProgress,
  currentSection,
  sectionIndex,
  totalSections,
}: {
  overallProgress: number;
  currentSection: string;
  sectionIndex: number;
  totalSections: number;
}) {
  return (
    <div className="flex items-center gap-3">
      {/* Mini progress ring */}
      <div className="relative w-10 h-10">
        <svg className="w-10 h-10 transform -rotate-90">
          <circle
            cx="20"
            cy="20"
            r="16"
            fill="none"
            stroke="currentColor"
            strokeWidth="4"
            className="text-gray-800"
          />
          <circle
            cx="20"
            cy="20"
            r="16"
            fill="none"
            stroke="url(#mini-gradient)"
            strokeWidth="4"
            strokeDasharray={100.53}
            strokeDashoffset={100.53 - (overallProgress / 100) * 100.53}
            strokeLinecap="round"
            className="transition-all duration-500"
          />
          <defs>
            <linearGradient id="mini-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#6B4FFF" />
              <stop offset="100%" stopColor="#FF6EC7" />
            </linearGradient>
          </defs>
        </svg>
        <span className="absolute inset-0 flex items-center justify-center text-xs font-bold text-white">
          {Math.round(overallProgress)}%
        </span>
      </div>

      {/* Section info */}
      <div className="hidden sm:block">
        <p className="text-xs text-gray-500">
          {sectionIndex + 1}/{totalSections}
        </p>
        <p className="text-sm font-medium text-white truncate max-w-[100px]">
          {currentSection}
        </p>
      </div>
    </div>
  );
}
