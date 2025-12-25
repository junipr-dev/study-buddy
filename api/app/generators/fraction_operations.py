"""Fraction operations question generator with word problems."""

import random
from fractions import Fraction
from math import gcd
from typing import Dict, Any

# Word problem templates for fractions
FRACTION_WORD_PROBLEMS = {
    "addition": [
        {"context": "pizza", "template": "You ate {frac1} of a pizza. Your friend ate {frac2} of the same pizza. How much pizza was eaten in total?"},
        {"context": "recipe", "template": "A recipe calls for {frac1} cup of flour. You want to add {frac2} cup more. How much flour will you use?"},
        {"context": "distance", "template": "You walked {frac1} of a mile to school. After school, you walked {frac2} of a mile to the store. How far did you walk in total?"},
        {"context": "time", "template": "You spent {frac1} of an hour on homework. Then you spent {frac2} of an hour reading. How much time did you spend?"},
        {"context": "garden", "template": "Your garden is {frac1} full of tomatoes and {frac2} full of peppers. What fraction of your garden has vegetables?"},
    ],
}


def generate_fraction_addition(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate fraction addition problem: a/b + c/d

    Args:
        difficulty: 1 (easy - same denominator), 2-3 (different denominators), 4-5 (mixed numbers)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    # Use word problems 50% of the time
    use_word_problem = random.random() < 0.5

    if difficulty == 1:
        # Easy: Same denominator
        denominator = random.choice([2, 3, 4, 5, 6, 8, 10])
        num1 = random.randint(1, denominator - 1)
        num2 = random.randint(1, denominator - 1)

        frac1 = Fraction(num1, denominator)
        frac2 = Fraction(num2, denominator)

        # Format fractions for display
        frac1_str = f"{num1}/{denominator}"
        frac2_str = f"{num2}/{denominator}"
        frac1_latex = f"$\\frac{{{num1}}}{{{denominator}}}$"
        frac2_latex = f"$\\frac{{{num2}}}{{{denominator}}}$"

        if use_word_problem:
            wp = random.choice(FRACTION_WORD_PROBLEMS["addition"])
            question = wp["template"].format(frac1=frac1_str, frac2=frac2_str)
            steps.append(f"**Problem:** {question}")
            steps.append(f"**Identify:** Add {frac1_latex} + {frac2_latex}")
        else:
            question = f"$\\frac{{{num1}}}{{{denominator}}} + \\frac{{{num2}}}{{{denominator}}}$"
            steps.append(f"Start with the expression: {question}")

        steps.append(f"Both fractions have the same denominator (${denominator}$), so we can add the numerators directly")
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

        # Format fractions for display
        frac1_str = f"{num1}/{denom1}"
        frac2_str = f"{num2}/{denom2}"
        frac1_latex = f"$\\frac{{{num1}}}{{{denom1}}}$"
        frac2_latex = f"$\\frac{{{num2}}}{{{denom2}}}$"

        if use_word_problem:
            wp = random.choice(FRACTION_WORD_PROBLEMS["addition"])
            question = wp["template"].format(frac1=frac1_str, frac2=frac2_str)
            steps.append(f"**Problem:** {question}")
            steps.append(f"**Identify:** Add {frac1_latex} + {frac2_latex}")
        else:
            question = f"$\\frac{{{num1}}}{{{denom1}}} + \\frac{{{num2}}}{{{denom2}}}$"
            steps.append(f"Start with the expression: {question}")

        # Find LCD
        lcm = (denom1 * denom2) // gcd(denom1, denom2)
        steps.append(f"The denominators are different (${denom1}$ and ${denom2}$), so find the least common denominator (LCD)")
        steps.append(f"LCD of ${denom1}$ and ${denom2}$ is ${lcm}$")

        # Convert fractions
        mult1 = lcm // denom1
        mult2 = lcm // denom2
        new_num1 = num1 * mult1
        new_num2 = num2 * mult2

        steps.append(f"Convert each fraction to have denominator ${lcm}$:")
        steps.append(f"$\\frac{{{num1}}}{{{denom1}}} \\times \\frac{{{mult1}}}{{{mult1}}} = \\frac{{{new_num1}}}{{{lcm}}}$")
        steps.append(f"$\\frac{{{num2}}}{{{denom2}}} \\times \\frac{{{mult2}}}{{{mult2}}} = \\frac{{{new_num2}}}{{{lcm}}}$")
        steps.append(f"Now add the fractions with the same denominator:")
        steps.append(f"$\\frac{{{new_num1}}}{{{lcm}}} + \\frac{{{new_num2}}}{{{lcm}}} = \\frac{{{new_num1 + new_num2}}}{{{lcm}}}$")

    # Calculate result
    result = frac1 + frac2

    # Simplify if needed
    if difficulty == 1:
        sum_numerator = num1 + num2
    else:
        sum_numerator = new_num1 + new_num2

    if result.numerator != sum_numerator or result.denominator != (denominator if difficulty == 1 else lcm):
        steps.append(f"Simplify the fraction by dividing both numerator and denominator by their GCD:")
        steps.append(f"$\\frac{{{result.numerator}}}{{{result.denominator}}}$")

    # Format answer
    if result.denominator == 1:
        answer_str = str(result.numerator)
        steps.append(f"**Final Answer:** ${result.numerator}$")
    else:
        answer_str = f"{result.numerator}/{result.denominator}"
        steps.append(f"**Final Answer:** $\\frac{{{result.numerator}}}{{{result.denominator}}}$")

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
