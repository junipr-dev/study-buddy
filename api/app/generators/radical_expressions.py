"""Radical expressions generator."""

import random
from typing import Dict, Any, List
from math import sqrt, gcd

# Real-world applications of radicals
RADICAL_WORD_PROBLEMS = [
    {
        "context": "Free fall distance: d = √(2h) where h is height. Simplify radical solutions.",
        "domain": "physics"
    },
    {
        "context": "Pythagorean theorem in construction: diagonal = √(length² + width²)",
        "domain": "engineering"
    },
    {
        "context": "Standard deviation in statistics: σ = √(variance). Rationalize denominators.",
        "domain": "statistics"
    },
    {
        "context": "Pendulum period: T = 2π√(L/g). Simplify radical expressions.",
        "domain": "physics"
    },
    {
        "context": "Circuit impedance: Z = √(R² + X²). Combine radical terms.",
        "domain": "technology"
    },
]


def generate_radical_expressions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate radical expressions problems.

    Args:
        difficulty: 1 (simplify), 2 (add/subtract), 3 (multiply/rationalize)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Simplify radicals
        # Choose a number with perfect square factors
        perfect_squares = [4, 9, 16, 25, 36, 49]
        perfect_square = random.choice(perfect_squares)
        other_factor = random.randint(2, 6)

        # Avoid making another perfect square
        while other_factor in [4, 9, 16, 25, 36, 49]:
            other_factor = random.randint(2, 6)

        radicand = perfect_square * other_factor

        question = f"\\sqrt{{{radicand}}}"

        # Simplify
        outside = int(sqrt(perfect_square))
        inside = other_factor

        steps = [
            f"Simplify: ${question}$",
            f"Factor the radicand into perfect square factors:",
            f"${radicand} = {perfect_square} \\times {other_factor}$",
            f"$\\sqrt{{{radicand}}} = \\sqrt{{{perfect_square} \\times {other_factor}}}$",
            f"Use the property: $\\sqrt{{ab}} = \\sqrt{{a}} \\cdot \\sqrt{{b}}$",
            f"$= \\sqrt{{{perfect_square}}} \\cdot \\sqrt{{{other_factor}}}$",
            f"$= {outside}\\sqrt{{{inside}}}$",
            f"**Final Answer:** ${outside}\\sqrt{{{inside}}}$"
        ]

        answer = f"{outside}√{inside}"

    elif difficulty == 2:
        # Add or subtract radicals
        operation = random.choice(["+", "-"])

        # Create like radicals: a√n ± b√n
        radicand = random.choice([2, 3, 5, 6, 7])
        coef1 = random.randint(2, 8)
        coef2 = random.randint(2, 8)

        question = f"{coef1}\\sqrt{{{radicand}}} {operation} {coef2}\\sqrt{{{radicand}}}"

        if operation == "+":
            result = coef1 + coef2
            op_word = "add"
        else:
            result = coef1 - coef2
            op_word = "subtract"

        steps = [
            f"${question}$",
            f"These are like radicals (same radicand), so we can {op_word} the coefficients",
            f"${coef1}\\sqrt{{{radicand}}} {operation} {coef2}\\sqrt{{{radicand}}} = ({coef1} {operation} {coef2})\\sqrt{{{radicand}}}$",
            f"$= {result}\\sqrt{{{radicand}}}$",
            f"**Final Answer:** ${result}\\sqrt{{{radicand}}}$"
        ]

        answer = f"{result}√{radicand}"

    else:  # difficulty == 3
        # Multiply radicals or rationalize denominator
        problem_type = random.choice(["multiply", "rationalize"])

        if problem_type == "multiply":
            # √a × √b
            a = random.randint(2, 6)
            b = random.randint(2, 6)

            question = f"\\sqrt{{{a}}} \\times \\sqrt{{{b}}}"

            product = a * b

            steps = [
                f"Multiply: ${question}$",
                f"Use the property: $\\sqrt{{a}} \\cdot \\sqrt{{b}} = \\sqrt{{ab}}$",
                f"$\\sqrt{{{a}}} \\times \\sqrt{{{b}}} = \\sqrt{{{a} \\times {b}}}$",
                f"$= \\sqrt{{{product}}}$",
            ]

            # Simplify if possible
            simplified = False
            for i in range(int(sqrt(product)), 1, -1):
                if product % (i * i) == 0:
                    outside = i
                    inside = product // (i * i)
                    steps.append(f"Simplify $\\sqrt{{{product}}}$:")
                    steps.append(f"${product} = {i*i} \\times {inside}$")
                    steps.append(f"$\\sqrt{{{product}}} = \\sqrt{{{i*i} \\times {inside}}} = {outside}\\sqrt{{{inside}}}$")
                    steps.append(f"**Final Answer:** ${outside}\\sqrt{{{inside}}}$")
                    answer = f"{outside}√{inside}"
                    simplified = True
                    break

            if not simplified:
                steps.append(f"$\\sqrt{{{product}}}$ is already in simplest form")
                steps.append(f"**Final Answer:** $\\sqrt{{{product}}}$")
                answer = f"√{product}"

        else:  # rationalize
            # Rationalize: 1/√n
            numerator = random.randint(1, 5)
            radicand = random.choice([2, 3, 5, 6, 7])

            question = f"\\frac{{{numerator}}}{{\\sqrt{{{radicand}}}}}"

            steps = [
                f"Rationalize the denominator: ${question}$",
                f"Multiply numerator and denominator by $\\sqrt{{{radicand}}}$:",
                f"$\\frac{{{numerator}}}{{\\sqrt{{{radicand}}}}} \\times \\frac{{\\sqrt{{{radicand}}}}}{{\\sqrt{{{radicand}}}}}$",
                f"$= \\frac{{{numerator}\\sqrt{{{radicand}}}}}{{\\sqrt{{{radicand}}} \\times \\sqrt{{{radicand}}}}}$",
                f"$= \\frac{{{numerator}\\sqrt{{{radicand}}}}}{{{radicand}}}$",
            ]

            # Simplify if possible
            g = gcd(numerator, radicand)
            if g > 1:
                steps.append(f"Simplify by dividing by ${g}$:")
                steps.append(f"$\\frac{{{numerator // g}\\sqrt{{{radicand}}}}}{{{radicand // g}}}$")
                answer = f"{numerator // g}√{radicand}/{radicand // g}"
                steps.append(f"**Final Answer:** $\\frac{{{numerator // g}\\sqrt{{{radicand}}}}}{{{radicand // g}}}$")
            else:
                if numerator == 1:
                    answer = f"√{radicand}/{radicand}"
                    steps.append(f"**Final Answer:** $\\frac{{\\sqrt{{{radicand}}}}}{{{radicand}}}$")
                else:
                    answer = f"{numerator}√{radicand}/{radicand}"
                    steps.append(f"**Final Answer:** $\\frac{{{numerator}\\sqrt{{{radicand}}}}}{{{radicand}}}$")

    return {
        "question": f"Simplify: ${question}$",
        "answer": answer,
        "answer_numeric": None,
        "steps": steps,
        "difficulty": difficulty,
    }
