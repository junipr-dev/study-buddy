"""Fraction division question generator with engaging word problems."""

import random
from fractions import Fraction
from math import gcd
from typing import Dict, Any

# Word problem templates for fraction division
FRACTION_DIV_WORD_PROBLEMS = [
    {"context": "pizza", "template": "You have {frac1} of a pizza. You want to share it equally among {whole} friends. How much does each friend get?"},
    {"context": "rope", "template": "A rope is {frac1} meter long. If you cut it into pieces of {frac2} meter each, how many pieces can you make?"},
    {"context": "recipe", "template": "A recipe uses {frac1} cup of oil. If you only have a {frac2} cup measuring spoon, how many spoonfuls do you need?"},
    {"context": "fabric", "template": "You have {frac1} yard of fabric. Each craft project needs {frac2} yard. How many projects can you complete?"},
    {"context": "running", "template": "You ran {frac1} mile. If that's {frac2} of your usual distance, what's your usual distance?"},
    {"context": "time", "template": "A task takes {frac1} hour. If you have {frac2} hour, what fraction of the task can you complete?"},
]

# Question type variety
QUESTION_TYPES = ["standard", "word_problem", "verify", "compare"]


def generate_fractions_division(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a fraction division problem: (a/b) ÷ (c/d).

    Args:
        difficulty:
            1 (easy - simple fractions)
            2 (medium - requires simplification)
            3 (hard - mixed numbers or multiple operations)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    # Variety: use different question types
    use_word_problem = random.random() < 0.4
    use_verify = random.random() < 0.15  # "Is this correct?" style

    if difficulty == 1:
        # Easy: Simple fractions
        num1 = random.randint(1, 8)
        denom1 = random.randint(2, 8)
        num2 = random.randint(1, 8)
        denom2 = random.randint(2, 8)

        frac1 = Fraction(num1, denom1)
        frac2 = Fraction(num2, denom2)
        result = frac1 / frac2

        # Format fractions for display
        frac1_str = f"{num1}/{denom1}"
        frac2_str = f"{num2}/{denom2}"

        expression = f"\\frac{{{num1}}}{{{denom1}}} \\div \\frac{{{num2}}}{{{denom2}}}"

        if use_word_problem:
            wp = random.choice(FRACTION_DIV_WORD_PROBLEMS)
            question = wp["template"].format(frac1=frac1_str, frac2=frac2_str, whole=num2)
            steps.append(f"**Problem:** {question}")
            steps.append(f"**Identify:** Divide $\\frac{{{num1}}}{{{denom1}}} \\div \\frac{{{num2}}}{{{denom2}}}$")
        else:
            steps.append(f"Divide the fractions: ${expression}$")

        steps.append("**Rule:** To divide fractions, multiply by the reciprocal (\"Keep, Change, Flip\")")
        steps.append(f"$\\frac{{a}}{{b}} \\div \\frac{{c}}{{d}} = \\frac{{a}}{{b}} \\times \\frac{{d}}{{c}}$")

        steps.append(f"**Step 1:** Keep the first fraction: $\\frac{{{num1}}}{{{denom1}}}$")
        steps.append(f"**Step 2:** Change ÷ to ×")
        steps.append(f"**Step 3:** Flip the second fraction: $\\frac{{{denom2}}}{{{num2}}}$")
        steps.append(f"Now multiply: $\\frac{{{num1}}}{{{denom1}}} \\times \\frac{{{denom2}}}{{{num2}}}$")

        new_num = num1 * denom2
        new_denom = denom1 * num2

        steps.append(f"Multiply numerators: ${num1} \\times {denom2} = {new_num}$")
        steps.append(f"Multiply denominators: ${denom1} \\times {num2} = {new_denom}$")
        steps.append(f"Result: $\\frac{{{new_num}}}{{{new_denom}}}$")

        # Simplify
        if result.numerator != new_num or result.denominator != new_denom:
            common = gcd(new_num, new_denom)
            steps.append(f"**Simplify:** Divide both by their GCD (${common}$):")
            steps.append(f"$\\frac{{{result.numerator}}}{{{result.denominator}}}$")

    elif difficulty == 2:
        # Medium: Larger numbers, needs simplification
        num1 = random.randint(2, 12)
        denom1 = random.randint(3, 12)
        num2 = random.randint(2, 12)
        denom2 = random.randint(3, 12)

        frac1 = Fraction(num1, denom1)
        frac2 = Fraction(num2, denom2)

        expression = f"\\frac{{{num1}}}{{{denom1}}} \\div \\frac{{{num2}}}{{{denom2}}}"
        steps.append(f"Divide the fractions: ${expression}$")
        steps.append("**Rule:** Multiply by the reciprocal of the divisor")

        steps.append(f"**Step 1:** Flip the second fraction (find its reciprocal):")
        steps.append(f"Reciprocal of $\\frac{{{num2}}}{{{denom2}}}$ is $\\frac{{{denom2}}}{{{num2}}}$")

        steps.append(f"**Step 2:** Multiply:")
        steps.append(f"$\\frac{{{num1}}}{{{denom1}}} \\times \\frac{{{denom2}}}{{{num2}}}$")

        # Show cross-canceling if possible
        if gcd(num1, num2) > 1 or gcd(denom1, denom2) > 1:
            steps.append("**Step 3:** Simplify before multiplying (cross-cancel if possible)")

            gcd1 = gcd(num1, num2)
            gcd2 = gcd(denom1, denom2)

            if gcd1 > 1:
                steps.append(f"Cancel common factor ${gcd1}$ from ${num1}$ and ${num2}$")
            if gcd2 > 1:
                steps.append(f"Cancel common factor ${gcd2}$ from ${denom1}$ and ${denom2}$")

        new_num = num1 * denom2
        new_denom = denom1 * num2

        steps.append(f"**Step 4:** Multiply: $\\frac{{{new_num}}}{{{new_denom}}}$")

        # Simplify
        result = frac1 / frac2
        if result.numerator != new_num or result.denominator != new_denom:
            common = gcd(new_num, new_denom)
            steps.append(f"**Step 5:** Simplify by GCD (${common}$):")
            steps.append(f"$\\frac{{{result.numerator}}}{{{result.denominator}}}$")

    else:  # difficulty == 3
        # Hard: Mixed numbers
        whole = random.randint(1, 4)
        num1 = random.randint(1, 5)
        denom1 = random.randint(2, 6)
        while num1 >= denom1:
            num1 = random.randint(1, 5)

        num2 = random.randint(1, 8)
        denom2 = random.randint(2, 8)

        expression = f"{whole}\\frac{{{num1}}}{{{denom1}}} \\div \\frac{{{num2}}}{{{denom2}}}"
        steps.append(f"Divide the mixed number by a fraction: ${expression}$")

        steps.append("**Step 1:** Convert mixed number to improper fraction")
        improper_num = whole * denom1 + num1
        steps.append(f"${whole}\\frac{{{num1}}}{{{denom1}}} = \\frac{{{whole} \\times {denom1} + {num1}}}{{{denom1}}} = \\frac{{{improper_num}}}{{{denom1}}}$")

        steps.append("**Step 2:** Rewrite the division:")
        steps.append(f"$\\frac{{{improper_num}}}{{{denom1}}} \\div \\frac{{{num2}}}{{{denom2}}}$")

        steps.append("**Step 3:** Multiply by the reciprocal:")
        steps.append(f"$\\frac{{{improper_num}}}{{{denom1}}} \\times \\frac{{{denom2}}}{{{num2}}}$")

        new_num = improper_num * denom2
        new_denom = denom1 * num2

        steps.append(f"**Step 4:** Multiply:")
        steps.append(f"$\\frac{{{improper_num} \\times {denom2}}}{{{denom1} \\times {num2}}} = \\frac{{{new_num}}}{{{new_denom}}}$")

        frac1 = Fraction(improper_num, denom1)
        frac2 = Fraction(num2, denom2)
        result = frac1 / frac2

        if result.numerator != new_num or result.denominator != new_denom:
            steps.append(f"**Step 5:** Simplify:")
            steps.append(f"$\\frac{{{result.numerator}}}{{{result.denominator}}}$")

        # Check if it can be converted back to mixed number
        if result.numerator > result.denominator:
            whole_part = result.numerator // result.denominator
            remainder = result.numerator % result.denominator
            if remainder > 0:
                steps.append(f"Convert to mixed number: ${whole_part}\\frac{{{remainder}}}{{{result.denominator}}}$")

    # Format answer
    if result.denominator == 1:
        answer_str = str(result.numerator)
        steps.append(f"**Final Answer:** ${result.numerator}$")
    else:
        answer_str = f"{result.numerator}/{result.denominator}"
        steps.append(f"**Final Answer:** $\\frac{{{result.numerator}}}{{{result.denominator}}}$")

    return {
        "question": f"Divide: ${expression}$",
        "answer": answer_str,
        "answer_numeric": float(result),
        "steps": steps,
        "difficulty": difficulty,
    }
