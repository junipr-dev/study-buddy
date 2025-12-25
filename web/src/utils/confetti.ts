import confetti from 'canvas-confetti';

// Synthwave color palette for confetti
const synthwaveColors = ['#6B4FFF', '#FF6EC7', '#00E6F6', '#B3FF00', '#FFD700'];

/**
 * Fire confetti from both sides of the screen
 */
export function celebrationBurst() {
  const duration = 3000;
  const end = Date.now() + duration;

  const frame = () => {
    // Left side
    confetti({
      particleCount: 3,
      angle: 60,
      spread: 55,
      origin: { x: 0, y: 0.6 },
      colors: synthwaveColors,
    });

    // Right side
    confetti({
      particleCount: 3,
      angle: 120,
      spread: 55,
      origin: { x: 1, y: 0.6 },
      colors: synthwaveColors,
    });

    if (Date.now() < end) {
      requestAnimationFrame(frame);
    }
  };

  frame();
}

/**
 * Single burst of confetti from center
 */
export function centerBurst() {
  confetti({
    particleCount: 100,
    spread: 70,
    origin: { x: 0.5, y: 0.5 },
    colors: synthwaveColors,
  });
}

/**
 * Subtle sparkle effect for correct answers
 */
export function correctAnswerSparkle() {
  confetti({
    particleCount: 30,
    spread: 60,
    origin: { x: 0.5, y: 0.5 },
    colors: ['#B3FF00', '#7ACC00', '#FFFFFF'],
    ticks: 100,
    gravity: 0.8,
    scalar: 0.8,
    shapes: ['circle'],
  });
}

/**
 * Badge unlock celebration
 */
export function badgeUnlockEffect() {
  // First burst
  confetti({
    particleCount: 50,
    spread: 100,
    origin: { x: 0.5, y: 0.5 },
    colors: synthwaveColors,
    shapes: ['star', 'circle'],
  });

  // Delayed second burst
  setTimeout(() => {
    confetti({
      particleCount: 30,
      spread: 120,
      origin: { x: 0.5, y: 0.5 },
      colors: ['#FFD700', '#FFA500', '#FFFFFF'],
      shapes: ['star'],
    });
  }, 150);
}

/**
 * Streak milestone celebration
 */
export function streakCelebration(streakCount: number) {
  const intensity = Math.min(streakCount / 10, 1);

  confetti({
    particleCount: Math.floor(50 * intensity) + 20,
    spread: 60 + (intensity * 40),
    origin: { x: 0.5, y: 0.6 },
    colors: ['#FF6B35', '#FF9F1C', '#FFCA3A', '#FFD700'],
    shapes: ['circle'],
  });
}

/**
 * Report card reveal celebration
 */
export function reportCardReveal(score: number) {
  const isGreat = score >= 80;
  const isGood = score >= 60;

  if (isGreat) {
    // Epic celebration
    celebrationBurst();
  } else if (isGood) {
    // Nice celebration
    centerBurst();
  } else {
    // Encouraging sparkle
    confetti({
      particleCount: 20,
      spread: 40,
      origin: { x: 0.5, y: 0.5 },
      colors: ['#6B4FFF', '#00E6F6'],
      ticks: 80,
    });
  }
}
