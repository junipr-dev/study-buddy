"""Pythagorean trigonometric identities question generator."""

import random
import math
from typing import Dict, Any


def generate_pythagorean_identities(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate problems using Pythagorean trigonometric identities.

    Args:
        difficulty: 1 (verify identity), 2 (find unknown trig value), 3 (simplify expressions)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Verify basic Pythagorean identity at standard angle
        angles = [
            (30, "\\frac{\\pi}{6}", 0.5, math.sqrt(3)/2, "\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}"),
            (45, "\\frac{\\pi}{4}", math.sqrt(2)/2, math.sqrt(2)/2, "\\frac{\\sqrt{2}}{2}", "\\frac{\\sqrt{2}}{2}"),
            (60, "\\frac{\\pi}{3}", math.sqrt(3)/2, 0.5, "\\frac{\\sqrt{3}}{2}", "\\frac{1}{2}"),
        ]

        degrees, radian_str, sin_val, cos_val, sin_str, cos_str = random.choice(angles)

        question = f"Verify that $\\sin^2({degrees}°) + \\cos^2({degrees}°) = 1$ using exact values."

        steps = [
            f"Recall: $\\sin({degrees}°) = {sin_str}$ and $\\cos({degrees}°) = {cos_str}$",
            f"Calculate $\\sin^2({degrees}°)$:",
            f"$\\sin^2({degrees}°) = ({sin_str})^2 = {round(sin_val**2, 4)}$",
            f"Calculate $\\cos^2({degrees}°)$:",
            f"$\\cos^2({degrees}°) = ({cos_str})^2 = {round(cos_val**2, 4)}$",
            f"Add them together:",
            f"$\\sin^2({degrees}°) + \\cos^2({degrees}°) = {round(sin_val**2, 4)} + {round(cos_val**2, 4)} = 1$",
            "**Final Answer:** Identity verified: $1$"
        ]

        answer_numeric = 1

    elif difficulty == 2:
        # Medium: Given sin, find cos (or vice versa) using Pythagorean identity
        # Use fractions for exact values
        trig_values = [
            ("sin", 3, 5, 4, 5, "\\frac{3}{5}", "\\frac{4}{5}"),  # sin=3/5, cos=4/5
            ("sin", 5, 13, 12, 13, "\\frac{5}{13}", "\\frac{12}{13}"),  # sin=5/13, cos=12/13
            ("sin", 8, 17, 15, 17, "\\frac{8}{17}", "\\frac{15}{17}"),  # sin=8/17, cos=15/17
            ("cos", 4, 5, 3, 5, "\\frac{3}{5}", "\\frac{4}{5}"),  # cos=4/5, sin=3/5
            ("cos", 12, 13, 5, 13, "\\frac{5}{13}", "\\frac{12}{13}"),  # cos=12/13, sin=5/13
        ]

        given_func, num, den, other_num, other_den, sin_str, cos_str = random.choice(trig_values)

        if given_func == "sin":
            given_str = sin_str
            find_func = "cos"
            find_str = cos_str
            given_val = num / den
            find_val = other_num / other_den
        else:
            given_str = cos_str
            find_func = "sin"
            find_str = sin_str
            given_val = other_num / other_den
            find_val = num / den

        question = f"If $\\{given_func}(\\theta) = {given_str}$ and $\\theta$ is in Quadrant I, find $\\{find_func}(\\theta)$."

        steps = [
            f"Use the Pythagorean identity: $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$",
        ]

        if given_func == "sin":
            steps.append(f"Substitute: $({given_str})^2 + \\cos^2(\\theta) = 1$")
            steps.append(f"Calculate: $\\frac{{{num**2}}}{{{den**2}}} + \\cos^2(\\theta) = 1$")
            steps.append(f"Simplify: $\\cos^2(\\theta) = 1 - \\frac{{{num**2}}}{{{den**2}}}$")
            steps.append(f"$\\cos^2(\\theta) = \\frac{{{den**2}}}{{{den**2}}} - \\frac{{{num**2}}}{{{den**2}}} = \\frac{{{den**2 - num**2}}}{{{den**2}}}$")
            steps.append(f"Take the square root: $\\cos(\\theta) = \\pm\\sqrt{{\\frac{{{den**2 - num**2}}}{{{den**2}}}}}$")
            steps.append(f"Since $\\theta$ is in Quadrant I, $\\cos(\\theta) > 0$")
            steps.append(f"$\\cos(\\theta) = \\frac{{\\sqrt{{{den**2 - num**2}}}}}{{{den}}} = \\frac{{{other_num}}}{{{other_den}}}$")
        else:
            steps.append(f"Substitute: $\\sin^2(\\theta) + ({given_str})^2 = 1$")
            steps.append(f"Calculate: $\\sin^2(\\theta) + \\frac{{{other_num**2}}}{{{other_den**2}}} = 1$")
            steps.append(f"Simplify: $\\sin^2(\\theta) = 1 - \\frac{{{other_num**2}}}{{{other_den**2}}}$")
            steps.append(f"$\\sin^2(\\theta) = \\frac{{{other_den**2}}}{{{other_den**2}}} - \\frac{{{other_num**2}}}{{{other_den**2}}} = \\frac{{{other_den**2 - other_num**2}}}{{{other_den**2}}}$")
            steps.append(f"Take the square root: $\\sin(\\theta) = \\pm\\sqrt{{\\frac{{{other_den**2 - other_num**2}}}{{{other_den**2}}}}}$")
            steps.append(f"Since $\\theta$ is in Quadrant I, $\\sin(\\theta) > 0$")
            steps.append(f"$\\sin(\\theta) = \\frac{{\\sqrt{{{other_den**2 - other_num**2}}}}}{{{other_den}}} = \\frac{{{num}}}{{{den}}}$")

        steps.append(f"**Final Answer:** $\\{find_func}(\\theta) = {find_str}$")

        answer_numeric = round(find_val, 4)

    else:
        # Hard: Simplify expressions using multiple identities
        expression_types = [
            "substitute",
            "tangent_identity",
            "reciprocal"
        ]

        expr_type = random.choice(expression_types)

        if expr_type == "substitute":
            # Simplify using sin^2 + cos^2 = 1
            question = "Simplify the expression: $\\frac{1 - \\sin^2(\\theta)}{\\cos(\\theta)}$"

            steps = [
                "Use the Pythagorean identity: $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$",
                "Rearrange: $1 - \\sin^2(\\theta) = \\cos^2(\\theta)$",
                "Substitute into the expression:",
                "$\\frac{1 - \\sin^2(\\theta)}{\\cos(\\theta)} = \\frac{\\cos^2(\\theta)}{\\cos(\\theta)}$",
                "Simplify: $\\frac{\\cos^2(\\theta)}{\\cos(\\theta)} = \\cos(\\theta)$",
                "**Final Answer:** $\\cos(\\theta)$"
            ]

            # For answer, use a test value (45 degrees)
            answer_numeric = round(math.cos(math.radians(45)), 4)

        elif expr_type == "tangent_identity":
            # Use 1 + tan^2 = sec^2
            question = "Simplify the expression: $\\frac{\\sin^2(\\theta)}{\\cos^2(\\theta)} + 1$"

            steps = [
                "Recognize that $\\frac{\\sin(\\theta)}{\\cos(\\theta)} = \\tan(\\theta)$",
                "Therefore: $\\frac{\\sin^2(\\theta)}{\\cos^2(\\theta)} = \\tan^2(\\theta)$",
                "The expression becomes: $\\tan^2(\\theta) + 1$",
                "Use the identity: $1 + \\tan^2(\\theta) = \\sec^2(\\theta)$",
                "Also: $\\sec(\\theta) = \\frac{1}{\\cos(\\theta)}$, so $\\sec^2(\\theta) = \\frac{1}{\\cos^2(\\theta)}$",
                "**Final Answer:** $\\sec^2(\\theta)$ or $\\frac{1}{\\cos^2(\\theta)}$"
            ]

            # For answer, use a test value (45 degrees)
            answer_numeric = round(1 / (math.cos(math.radians(45))**2), 4)

        else:  # reciprocal
            # Simplify using reciprocal identities
            question = "Simplify: $(1 - \\cos^2(\\theta))(1 + \\cot^2(\\theta))$"

            steps = [
                "Simplify the first term using $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$:",
                "$1 - \\cos^2(\\theta) = \\sin^2(\\theta)$",
                "Simplify the second term using $1 + \\cot^2(\\theta) = \\csc^2(\\theta)$:",
                "The expression becomes: $\\sin^2(\\theta) \\cdot \\csc^2(\\theta)$",
                "Since $\\csc(\\theta) = \\frac{1}{\\sin(\\theta)}$, we have $\\csc^2(\\theta) = \\frac{1}{\\sin^2(\\theta)}$",
                "Substitute: $\\sin^2(\\theta) \\cdot \\frac{1}{\\sin^2(\\theta)} = 1$",
                "**Final Answer:** $1$"
            ]

            answer_numeric = 1

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
