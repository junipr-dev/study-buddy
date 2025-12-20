import { useState, useEffect, useCallback } from 'react';
import { createPortal } from 'react-dom';

interface TutorialStep {
  target: string; // CSS selector for the element to highlight
  title: string;
  content: string;
  position: 'top' | 'bottom' | 'left' | 'right';
  align?: 'start' | 'center' | 'end';
}

const TUTORIAL_STEPS: TutorialStep[] = [
  {
    target: '[data-tutorial="logo"]',
    title: 'Welcome to Study Buddy!',
    content: 'Your adaptive math learning companion. This tutorial will show you around in about 30 seconds.',
    position: 'bottom',
    align: 'start',
  },
  {
    target: '[data-tutorial="mode-switcher"]',
    title: 'Two Learning Modes',
    content: 'Switch between Evaluation Mode (test your knowledge) and Practice Mode (targeted learning).',
    position: 'bottom',
    align: 'start',
  },
  {
    target: '[data-tutorial="evaluation-mode"]',
    title: 'Evaluation Mode',
    content: 'Take a comprehensive assessment across all math topics. See your strengths and areas to improve.',
    position: 'bottom',
    align: 'start',
  },
  {
    target: '[data-tutorial="practice-mode"]',
    title: 'Practice Mode',
    content: 'Practice with adaptive questions that adjust to your level. Choose specific skills or let the algorithm guide you.',
    position: 'bottom',
    align: 'start',
  },
  {
    target: '[data-tutorial="progress-bar"]',
    title: 'Track Your Progress',
    content: 'Watch your progress in real-time. In Evaluation Mode, you\'ll see both overall and section progress.',
    position: 'bottom',
    align: 'center',
  },
  {
    target: '[data-tutorial="question-card"]',
    title: 'Answer Questions',
    content: 'Type your answer and press Enter or click Submit. For fractions, use format like 3/4 or 1/2.',
    position: 'top',
    align: 'center',
  },
  {
    target: '[data-tutorial="progress-button"]',
    title: 'View Your Progress',
    content: 'Check your evaluation history, see which skills you\'ve mastered, and track improvement over time.',
    position: 'bottom',
    align: 'end',
  },
];

interface TutorialProps {
  onComplete: () => void;
  onSkip: () => void;
}

export default function Tutorial({ onComplete, onSkip }: TutorialProps) {
  const [currentStep, setCurrentStep] = useState(0);
  const [targetRect, setTargetRect] = useState<DOMRect | null>(null);
  const [isVisible, setIsVisible] = useState(false);

  const step = TUTORIAL_STEPS[currentStep];

  const updateTargetRect = useCallback(() => {
    const element = document.querySelector(step.target);
    if (element) {
      const rect = element.getBoundingClientRect();
      setTargetRect(rect);
      setIsVisible(true);
    } else {
      setTargetRect(null);
      setIsVisible(false);
    }
  }, [step.target]);

  useEffect(() => {
    // Initial update
    updateTargetRect();

    // Update on resize/scroll
    window.addEventListener('resize', updateTargetRect);
    window.addEventListener('scroll', updateTargetRect);

    // Small delay to ensure elements are rendered
    const timer = setTimeout(updateTargetRect, 100);

    return () => {
      window.removeEventListener('resize', updateTargetRect);
      window.removeEventListener('scroll', updateTargetRect);
      clearTimeout(timer);
    };
  }, [updateTargetRect]);

  const handleNext = () => {
    if (currentStep < TUTORIAL_STEPS.length - 1) {
      setCurrentStep(currentStep + 1);
    } else {
      onComplete();
    }
  };

  const handlePrev = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  const handleKeyDown = useCallback((e: KeyboardEvent) => {
    if (e.key === 'Escape') {
      onSkip();
    } else if (e.key === 'ArrowRight' || e.key === 'Enter') {
      handleNext();
    } else if (e.key === 'ArrowLeft') {
      handlePrev();
    }
  }, [currentStep, onSkip]);

  useEffect(() => {
    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [handleKeyDown]);

  if (!isVisible || !targetRect) {
    return null;
  }

  // Calculate spotlight position with padding
  const padding = 8;
  const spotlight = {
    top: targetRect.top - padding,
    left: targetRect.left - padding,
    width: targetRect.width + padding * 2,
    height: targetRect.height + padding * 2,
  };

  // Calculate tooltip position
  const getTooltipStyle = (): React.CSSProperties => {
    const tooltipWidth = 320;
    const tooltipOffset = 16;

    let top = 0;
    let left = 0;

    switch (step.position) {
      case 'top':
        top = spotlight.top - tooltipOffset;
        left = spotlight.left + spotlight.width / 2;
        break;
      case 'bottom':
        top = spotlight.top + spotlight.height + tooltipOffset;
        left = spotlight.left + spotlight.width / 2;
        break;
      case 'left':
        top = spotlight.top + spotlight.height / 2;
        left = spotlight.left - tooltipOffset;
        break;
      case 'right':
        top = spotlight.top + spotlight.height / 2;
        left = spotlight.left + spotlight.width + tooltipOffset;
        break;
    }

    // Adjust horizontal alignment
    let translateX = '-50%';
    if (step.align === 'start') {
      translateX = '0%';
      left = spotlight.left;
    } else if (step.align === 'end') {
      translateX = '-100%';
      left = spotlight.left + spotlight.width;
    }

    // Adjust vertical for left/right positions
    let translateY = step.position === 'top' ? '-100%' : '0%';
    if (step.position === 'left' || step.position === 'right') {
      translateY = '-50%';
    }

    return {
      position: 'fixed',
      top,
      left,
      transform: `translate(${translateX}, ${translateY})`,
      width: tooltipWidth,
      zIndex: 10002,
    };
  };

  const overlay = (
    <div className="fixed inset-0 z-[10000]" onClick={onSkip}>
      {/* Dark overlay with spotlight cutout */}
      <svg className="absolute inset-0 w-full h-full">
        <defs>
          <mask id="spotlight-mask">
            <rect x="0" y="0" width="100%" height="100%" fill="white" />
            <rect
              x={spotlight.left}
              y={spotlight.top}
              width={spotlight.width}
              height={spotlight.height}
              rx="8"
              fill="black"
            />
          </mask>
        </defs>
        <rect
          x="0"
          y="0"
          width="100%"
          height="100%"
          fill="rgba(0, 0, 0, 0.85)"
          mask="url(#spotlight-mask)"
        />
      </svg>

      {/* Spotlight border/glow */}
      <div
        className="absolute border-2 border-primary rounded-lg shadow-[0_0_0_4px_rgba(107,79,255,0.3),0_0_20px_rgba(107,79,255,0.4)] transition-all duration-300"
        style={{
          top: spotlight.top,
          left: spotlight.left,
          width: spotlight.width,
          height: spotlight.height,
        }}
      />

      {/* Tooltip */}
      <div
        style={getTooltipStyle()}
        onClick={(e) => e.stopPropagation()}
        className="bg-surface border border-gray-700 rounded-xl shadow-2xl overflow-hidden animate-fadeIn"
      >
        {/* Progress indicator */}
        <div className="h-1 bg-gray-800">
          <div
            className="h-full bg-gradient-to-r from-primary to-secondary transition-all duration-300"
            style={{ width: `${((currentStep + 1) / TUTORIAL_STEPS.length) * 100}%` }}
          />
        </div>

        <div className="p-5">
          {/* Step counter */}
          <div className="text-xs text-gray-500 mb-2">
            Step {currentStep + 1} of {TUTORIAL_STEPS.length}
          </div>

          {/* Title */}
          <h3 className="text-lg font-bold text-white mb-2">{step.title}</h3>

          {/* Content */}
          <p className="text-gray-300 text-sm leading-relaxed mb-4">{step.content}</p>

          {/* Navigation */}
          <div className="flex items-center justify-between">
            <button
              onClick={onSkip}
              className="text-sm text-gray-500 hover:text-gray-300 transition-colors"
            >
              Skip tutorial
            </button>

            <div className="flex items-center gap-2">
              {currentStep > 0 && (
                <button
                  onClick={handlePrev}
                  className="px-3 py-1.5 text-sm text-gray-300 hover:text-white transition-colors"
                >
                  Back
                </button>
              )}
              <button
                onClick={handleNext}
                className="px-4 py-1.5 bg-primary hover:bg-primary-dark text-white text-sm font-medium rounded-lg transition-colors"
              >
                {currentStep === TUTORIAL_STEPS.length - 1 ? 'Get Started' : 'Next'}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  return createPortal(overlay, document.body);
}
