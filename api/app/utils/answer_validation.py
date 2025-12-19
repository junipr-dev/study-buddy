"""Answer validation utilities."""

from fractions import Fraction
import re


def parse_fraction(answer: str) -> float | None:
    """
    Parse various fraction formats to a decimal value.

    Supports:
    - Improper fractions: "7/5" -> 1.4
    - Mixed fractions: "1 2/5" -> 1.4
    - Decimals: "1.4" -> 1.4
    - Integers: "1" -> 1.0

    Returns None if parsing fails.
    """
    answer = answer.strip()

    try:
        # Try mixed fraction format: "1 2/5"
        mixed_match = re.match(r'^(-?\d+)\s+(\d+)/(\d+)$', answer)
        if mixed_match:
            whole = int(mixed_match.group(1))
            numerator = int(mixed_match.group(2))
            denominator = int(mixed_match.group(3))

            # Handle negative mixed fractions
            if whole < 0:
                return whole - (numerator / denominator)
            else:
                return whole + (numerator / denominator)

        # Try simple fraction: "7/5"
        if '/' in answer:
            frac = Fraction(answer)
            return float(frac)

        # Try decimal or integer
        return float(answer)

    except (ValueError, ZeroDivisionError):
        return None


def answers_are_equivalent(user_answer: str, correct_answer: str, tolerance: float = 0.01) -> bool:
    """
    Check if two answers are mathematically equivalent.

    Args:
        user_answer: The user's submitted answer
        correct_answer: The correct answer
        tolerance: Acceptable difference for floating point comparison

    Returns:
        True if answers are equivalent, False otherwise
    """
    # Try string match first (fastest)
    if user_answer.strip() == correct_answer.strip():
        return True

    # Parse both answers
    user_value = parse_fraction(user_answer)
    correct_value = parse_fraction(correct_answer)

    # If either failed to parse, not equivalent
    if user_value is None or correct_value is None:
        return False

    # Compare numerically
    return abs(user_value - correct_value) < tolerance
