"""Fraction multiplication question generator."""

import random
from fractions import Fraction
from math import gcd
from typing import Dict, Any


def generate_fractions_multiplication(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a fraction multiplication problem: (a/b) * (c/d).

    Args:
        difficulty:
            1 (easy - simple fractions)
            2 (medium - larger denominators, requires simplification)
            3 (hard - mixed numbers or three fractions)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    if difficulty == 1:
        # Easy: Simple fractions
        num1 = random.randint(1, 8)
        denom1 = random.randint(2, 8)
        num2 = random.randint(1, 8)
        denom2 = random.randint(2, 8)

        frac1 = Fraction(num1, denom1)
        frac2 = Fraction(num2, denom2)

        expression = f"\\frac{{{num1}}}{{{denom1}}} \\times \\frac{{{num2}}}{{{denom2}}}"
        steps.append(f"Multiply the fractions: ${expression}$")
        steps.append("**Rule:** Multiply numerators together and denominators together")
        steps.append(f"$\\frac{{a}}{{b}} \\times \\frac{{c}}{{d}} = \\frac{{a \\times c}}{{b \\times d}}$")

        new_num = num1 * num2
        new_denom = denom1 * denom2

        steps.append(f"Multiply numerators: ${num1} \\times {num2} = {new_num}$")
        steps.append(f"Multiply denominators: ${denom1} \\times {denom2} = {new_denom}$")
        steps.append(f"Result: $\\frac{{{new_num}}}{{{new_denom}}}$")

        # Simplify
        result = frac1 * frac2
        if result.numerator != new_num or result.denominator != new_denom:
            common = gcd(new_num, new_denom)
            steps.append(f"Simplify by dividing both by their GCD (${common}$):")
            steps.append(f"$\\frac{{{new_num} \\div {common}}}{{{new_denom} \\div {common}}} = \\frac{{{result.numerator}}}{{{result.denominator}}}$")

    elif difficulty == 2:
        # Medium: Larger numbers, definitely needs simplification
        num1 = random.randint(2, 12)
        denom1 = random.randint(3, 12)
        num2 = random.randint(2, 12)
        denom2 = random.randint(3, 12)

        frac1 = Fraction(num1, denom1)
        frac2 = Fraction(num2, denom2)

        expression = f"\\frac{{{num1}}}{{{denom1}}} \\times \\frac{{{num2}}}{{{denom2}}}"
        steps.append(f"Multiply the fractions: ${expression}$")
        steps.append("**Rule:** Multiply numerators together and denominators together")

        # Option to show cross-canceling
        if gcd(num1, denom2) > 1 or gcd(num2, denom1) > 1:
            steps.append("**Tip:** We can simplify before multiplying by cross-canceling")

            gcd1 = gcd(num1, denom2)
            gcd2 = gcd(num2, denom1)

            if gcd1 > 1:
                steps.append(f"Cancel common factor ${gcd1}$ from ${num1}$ and ${denom2}$:")
                steps.append(f"$\\frac{{{num1 // gcd1}}}{{{denom1}}} \\times \\frac{{{num2}}}{{{denom2 // gcd1}}}$")

            if gcd2 > 1:
                new_num2 = num2
                new_denom1 = denom1
                steps.append(f"Cancel common factor ${gcd2}$ from ${new_num2}$ and ${new_denom1}$:")

        new_num = num1 * num2
        new_denom = denom1 * denom2

        steps.append(f"Multiply: $\\frac{{{num1} \\times {num2}}}{{{denom1} \\times {denom2}}} = \\frac{{{new_num}}}{{{new_denom}}}$")

        # Simplify
        result = frac1 * frac2
        if result.numerator != new_num or result.denominator != new_denom:
            common = gcd(new_num, new_denom)
            steps.append(f"Simplify by dividing both by GCD (${common}$):")
            steps.append(f"$\\frac{{{result.numerator}}}{{{result.denominator}}}$")

    else:  # difficulty == 3
        # Hard: Three fractions or mixed numbers
        if random.choice([True, False]):
            # Three fractions
            num1 = random.randint(1, 6)
            denom1 = random.randint(2, 6)
            num2 = random.randint(1, 6)
            denom2 = random.randint(2, 6)
            num3 = random.randint(1, 6)
            denom3 = random.randint(2, 6)

            frac1 = Fraction(num1, denom1)
            frac2 = Fraction(num2, denom2)
            frac3 = Fraction(num3, denom3)

            expression = f"\\frac{{{num1}}}{{{denom1}}} \\times \\frac{{{num2}}}{{{denom2}}} \\times \\frac{{{num3}}}{{{denom3}}}"
            steps.append(f"Multiply the fractions: ${expression}$")
            steps.append("**Rule:** Multiply all numerators together and all denominators together")

            new_num = num1 * num2 * num3
            new_denom = denom1 * denom2 * denom3

            steps.append(f"Multiply numerators: ${num1} \\times {num2} \\times {num3} = {new_num}$")
            steps.append(f"Multiply denominators: ${denom1} \\times {denom2} \\times {denom3} = {new_denom}$")
            steps.append(f"Result: $\\frac{{{new_num}}}{{{new_denom}}}$")

            result = frac1 * frac2 * frac3
            if result.numerator != new_num or result.denominator != new_denom:
                common = gcd(new_num, new_denom)
                steps.append(f"Simplify by GCD (${common}$):")
                steps.append(f"$\\frac{{{result.numerator}}}{{{result.denominator}}}$")
        else:
            # Mixed number
            whole = random.randint(1, 4)
            num1 = random.randint(1, 5)
            denom1 = random.randint(2, 6)
            while num1 >= denom1:
                num1 = random.randint(1, 5)

            num2 = random.randint(1, 8)
            denom2 = random.randint(2, 8)

            expression = f"{whole}\\frac{{{num1}}}{{{denom1}}} \\times \\frac{{{num2}}}{{{denom2}}}"
            steps.append(f"Multiply the mixed number and fraction: ${expression}$")
            steps.append("**Step 1:** Convert mixed number to improper fraction")

            improper_num = whole * denom1 + num1
            steps.append(f"${whole}\\frac{{{num1}}}{{{denom1}}} = \\frac{{{whole} \\times {denom1} + {num1}}}{{{denom1}}} = \\frac{{{improper_num}}}{{{denom1}}}$")

            steps.append("**Step 2:** Multiply the fractions")
            steps.append(f"$\\frac{{{improper_num}}}{{{denom1}}} \\times \\frac{{{num2}}}{{{denom2}}}$")

            new_num = improper_num * num2
            new_denom = denom1 * denom2

            steps.append(f"$= \\frac{{{new_num}}}{{{new_denom}}}$")

            frac1 = Fraction(improper_num, denom1)
            frac2 = Fraction(num2, denom2)
            result = frac1 * frac2

            if result.numerator != new_num or result.denominator != new_denom:
                steps.append(f"Simplify: $\\frac{{{result.numerator}}}{{{result.denominator}}}$")

    # Format answer
    if result.denominator == 1:
        answer_str = str(result.numerator)
        steps.append(f"**Final Answer:** ${result.numerator}$")
    else:
        answer_str = f"{result.numerator}/{result.denominator}"
        steps.append(f"**Final Answer:** $\\frac{{{result.numerator}}}{{{result.denominator}}}$")

    return {
        "question": f"Multiply: ${expression}$",
        "answer": answer_str,
        "answer_numeric": float(result),
        "steps": steps,
        "difficulty": difficulty,
    }
