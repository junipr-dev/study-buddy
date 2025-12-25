import { useEffect, useState } from 'react';
import { badgeUnlockEffect } from '../utils/confetti';

interface Badge {
  id: number;
  slug: string;
  name: string;
  description: string;
  icon_emoji: string;
  category: string;
  tier: string;
}

interface BadgeUnlockModalProps {
  badge: Badge | null;
  onClose: () => void;
}

const tierColors = {
  bronze: 'from-amber-600 to-amber-800',
  silver: 'from-gray-300 to-gray-500',
  gold: 'from-yellow-400 to-yellow-600',
  platinum: 'from-purple-400 to-pink-500',
};

const tierGlow = {
  bronze: 'shadow-amber-500/50',
  silver: 'shadow-gray-400/50',
  gold: 'shadow-yellow-500/50',
  platinum: 'shadow-purple-500/50',
};

export default function BadgeUnlockModal({ badge, onClose }: BadgeUnlockModalProps) {
  const [show, setShow] = useState(false);

  useEffect(() => {
    if (badge) {
      // Trigger entrance animation
      setTimeout(() => setShow(true), 50);
      // Trigger confetti
      badgeUnlockEffect();
      // Auto-dismiss after 4 seconds
      const timer = setTimeout(() => {
        setShow(false);
        setTimeout(onClose, 300);
      }, 4000);
      return () => clearTimeout(timer);
    }
  }, [badge, onClose]);

  if (!badge) return null;

  const tier = badge.tier as keyof typeof tierColors;

  return (
    <div
      className={`fixed inset-0 bg-black/80 flex items-center justify-center z-50 transition-opacity duration-300 ${
        show ? 'opacity-100' : 'opacity-0'
      }`}
      onClick={() => {
        setShow(false);
        setTimeout(onClose, 300);
      }}
    >
      <div
        className={`transform transition-all duration-500 ${
          show ? 'scale-100 translate-y-0' : 'scale-50 translate-y-8'
        }`}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Badge container */}
        <div className="text-center">
          {/* "Badge Unlocked" text */}
          <p className="text-primary text-sm uppercase tracking-widest mb-4 animate-pulse">
            Badge Unlocked!
          </p>

          {/* Badge icon with glow */}
          <div
            className={`w-32 h-32 mx-auto rounded-full bg-gradient-to-br ${tierColors[tier]}
                       flex items-center justify-center shadow-2xl ${tierGlow[tier]}
                       animate-bounce-slow`}
          >
            <span className="text-6xl">{badge.icon_emoji}</span>
          </div>

          {/* Badge name */}
          <h2 className="text-2xl font-bold text-white mt-6 mb-2">
            {badge.name}
          </h2>

          {/* Badge description */}
          <p className="text-gray-400 max-w-xs mx-auto">
            {badge.description}
          </p>

          {/* Tier indicator */}
          <div className={`inline-block mt-4 px-4 py-1 rounded-full bg-gradient-to-r ${tierColors[tier]} text-white text-sm font-medium capitalize`}>
            {badge.tier}
          </div>

          {/* Tap to dismiss hint */}
          <p className="text-gray-500 text-xs mt-6">
            Tap anywhere to dismiss
          </p>
        </div>
      </div>
    </div>
  );
}
