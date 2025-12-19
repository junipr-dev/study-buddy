"""Fraction operations question generator."""

import random
from fractions import Fraction
from math import gcd
from typing import Dict, Any


def generate_fraction_addition(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate fraction addition problem: a/b + c/d

    Args:
        difficulty: 1 (easy - same denominator), 2-3 (different denominators), 4-5 (mixed numbers)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    if difficulty == 1:
        # Easy: Same denominator
        denominator = random.choice([2, 3, 4, 5, 6, 8, 10])
        num1 = random.randint(1, denominator - 1)
        num2 = random.randint(1, denominator - 1)

        frac1 = Fraction(num1, denominator)
        frac2 = Fraction(num2, denominator)

        question = f"$\\frac{{{num1}}}{{{denominator}}} + \\frac{{{num2}}}{{{denominator}}}$"
        steps.append(f"Same denominator, add numerators:")
        steps.append(f"$\\frac{{{num1} + {num2}}}{{{denominator}}} = \\frac{{{num1 + num2}}}{{{denominator}}}$")

    else:
        # Medium/Hard: Different denominators
        if difficulty <= 3:
            # Medium: smaller numbers
            denom1 = random.choice([2, 3, 4, 5, 6])
            denom2 = random.choice([2, 3, 4, 5, 6])
        else:
            # Hard: larger numbers
            denom1 = random.randint(3, 12)
            denom2 = random.randint(3, 12)

        # Avoid same denominator for these difficulties
        while denom1 == denom2:
            denom2 = random.randint(3, 12)

        num1 = random.randint(1, denom1 - 1)
        num2 = random.randint(1, denom2 - 1)

        frac1 = Fraction(num1, denom1)
        frac2 = Fraction(num2, denom2)

        question = f"$\\frac{{{num1}}}{{{denom1}}} + \\frac{{{num2}}}{{{denom2}}}$"

        # Find LCD
        lcm = (denom1 * denom2) // gcd(denom1, denom2)
        steps.append(f"Find common denominator: LCD = ${lcm}$")

        # Convert fractions
        mult1 = lcm // denom1
        mult2 = lcm // denom2
        new_num1 = num1 * mult1
        new_num2 = num2 * mult2

        steps.append(f"$\\frac{{{num1}}}{{{denom1}}} = \\frac{{{new_num1}}}{{{lcm}}}$")
        steps.append(f"$\\frac{{{num2}}}{{{denom2}}} = \\frac{{{new_num2}}}{{{lcm}}}$")
        steps.append(f"Add: $\\frac{{{new_num1}}}{{{lcm}}} + \\frac{{{new_num2}}}{{{lcm}}} = \\frac{{{new_num1 + new_num2}}}{{{lcm}}}$")

    # Calculate result
    result = frac1 + frac2

    # Simplify if needed
    if result.denominator != (num1 + num2 if difficulty == 1 else new_num1 + new_num2):
        steps.append(f"Simplify: $\\frac{{{result.numerator}}}{{{result.denominator}}}$")

    # Format answer
    if result.denominator == 1:
        answer_str = str(result.numerator)
    else:
        answer_str = f"{result.numerator}/{result.denominator}"

    return {
        "question": f"Calculate: {question}",
        "answer": answer_str,
        "answer_numeric": float(result),
        "steps": steps,
        "difficulty": difficulty,
    }


def validate_fraction_answer(user_answer: str, correct_answer: Fraction, tolerance: float = 0.01) -> bool:
    """Validate user's fraction answer."""
    try:
        # Try parsing as fraction first
        if "/" in user_answer:
            parts = user_answer.split("/")
            user_fraction = Fraction(int(parts[0]), int(parts[1]))
            return user_fraction == correct_answer
        else:
            # Try as decimal
            user_value = float(user_answer)
            return abs(user_value - float(correct_answer)) < tolerance
    except (ValueError, ZeroDivisionError):
        return False
