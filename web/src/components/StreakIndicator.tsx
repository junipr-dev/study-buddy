import { useEffect, useState } from 'react';
import { streakCelebration } from '../utils/confetti';

interface StreakIndicatorProps {
  streak: number;
  showLabel?: boolean;
  onStreakMilestone?: (streak: number) => void;
}

const MILESTONE_STREAKS = [3, 5, 10, 15, 25, 50, 100];

export default function StreakIndicator({
  streak,
  showLabel = true,
  onStreakMilestone,
}: StreakIndicatorProps) {
  const [animating, setAnimating] = useState(false);
  const [prevStreak, setPrevStreak] = useState(streak);

  const isMilestone = MILESTONE_STREAKS.includes(streak);
  const isOnFire = streak >= 3;

  useEffect(() => {
    if (streak > prevStreak) {
      setAnimating(true);
      const timer = setTimeout(() => setAnimating(false), 500);

      // Check for milestone
      if (MILESTONE_STREAKS.includes(streak)) {
        streakCelebration(streak);
        onStreakMilestone?.(streak);
      }

      setPrevStreak(streak);
      return () => clearTimeout(timer);
    }
    setPrevStreak(streak);
  }, [streak, prevStreak, onStreakMilestone]);

  if (streak === 0) {
    return null;
  }

  return (
    <div
      className={`
        inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full
        ${isOnFire ? 'bg-orange-500 bg-opacity-20' : 'bg-gray-800'}
        ${isMilestone ? 'ring-2 ring-orange-400 ring-opacity-50' : ''}
        transition-all duration-300
      `}
    >
      {/* Fire emoji with animation */}
      <span
        className={`
          text-lg
          ${animating ? 'animate-firePulse' : ''}
          ${isOnFire ? '' : 'grayscale opacity-50'}
        `}
      >
        🔥
      </span>

      {/* Streak count */}
      <span
        className={`
          font-bold text-sm
          ${isOnFire ? 'text-orange-400' : 'text-gray-400'}
          ${animating ? 'animate-countUp' : ''}
        `}
      >
        {streak}
      </span>

      {/* Optional label */}
      {showLabel && (
        <span className="text-xs text-gray-500 hidden sm:inline">
          streak
        </span>
      )}

      {/* Milestone indicator */}
      {isMilestone && (
        <span className="absolute -top-1 -right-1 w-2 h-2 bg-orange-400 rounded-full animate-ping" />
      )}
    </div>
  );
}

// Compact version for tight spaces
export function StreakBadge({ streak }: { streak: number }) {
  if (streak === 0) return null;

  return (
    <div className="inline-flex items-center gap-1 text-orange-400">
      <span className="text-sm">🔥</span>
      <span className="text-xs font-bold">{streak}</span>
    </div>
  );
}
