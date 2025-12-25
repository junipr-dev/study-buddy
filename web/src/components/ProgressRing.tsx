import { useEffect, useState } from 'react';

interface ProgressRingProps {
  progress: number; // 0-100
  size?: number;
  strokeWidth?: number;
  label?: string;
  showPercentage?: boolean;
  color?: 'primary' | 'success' | 'warning' | 'error';
  animated?: boolean;
}

const gradientIds = {
  primary: 'gradient-primary',
  success: 'gradient-success',
  warning: 'gradient-warning',
  error: 'gradient-error',
};

export default function ProgressRing({
  progress,
  size = 80,
  strokeWidth = 8,
  label,
  showPercentage = true,
  color = 'primary',
  animated = true,
}: ProgressRingProps) {
  const [displayProgress, setDisplayProgress] = useState(animated ? 0 : progress);

  const radius = (size - strokeWidth) / 2;
  const circumference = radius * 2 * Math.PI;
  const offset = circumference - (displayProgress / 100) * circumference;

  useEffect(() => {
    if (animated) {
      const timer = setTimeout(() => {
        setDisplayProgress(progress);
      }, 100);
      return () => clearTimeout(timer);
    } else {
      setDisplayProgress(progress);
    }
  }, [progress, animated]);

  return (
    <div className="relative inline-flex items-center justify-center">
      <svg width={size} height={size} className="transform -rotate-90">
        <defs>
          <linearGradient id="gradient-primary" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#6B4FFF" />
            <stop offset="100%" stopColor="#FF6EC7" />
          </linearGradient>
          <linearGradient id="gradient-success" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#B3FF00" />
            <stop offset="100%" stopColor="#7ACC00" />
          </linearGradient>
          <linearGradient id="gradient-warning" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#FFA500" />
            <stop offset="100%" stopColor="#FF6B35" />
          </linearGradient>
          <linearGradient id="gradient-error" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#FF4444" />
            <stop offset="100%" stopColor="#CC0000" />
          </linearGradient>
        </defs>

        {/* Background circle */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke="currentColor"
          strokeWidth={strokeWidth}
          className="text-gray-800"
        />

        {/* Progress circle */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke={`url(#${gradientIds[color]})`}
          strokeWidth={strokeWidth}
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          strokeLinecap="round"
          className={`transition-all duration-1000 ease-out ${animated ? '' : ''}`}
          style={{
            '--ring-circumference': circumference,
            '--ring-offset': offset,
          } as React.CSSProperties}
        />
      </svg>

      {/* Center content */}
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        {showPercentage && (
          <span className="text-lg font-bold text-white">
            {Math.round(displayProgress)}%
          </span>
        )}
        {label && (
          <span className="text-xs text-gray-400 text-center px-1 leading-tight">
            {label}
          </span>
        )}
      </div>
    </div>
  );
}

// Compact version for inline use
export function ProgressRingSmall({
  progress,
  color = 'primary',
}: {
  progress: number;
  color?: 'primary' | 'success' | 'warning' | 'error';
}) {
  return (
    <ProgressRing
      progress={progress}
      size={32}
      strokeWidth={4}
      showPercentage={false}
      color={color}
      animated={true}
    />
  );
}
