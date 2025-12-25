"""Pythagorean trigonometric identities question generator."""

import random
import math
from typing import Dict, Any

# Real-world contexts for Pythagorean identities
WORD_PROBLEMS = [
    {
        "context": "In physics and engineering, oscillatory motion (waves, vibrations) can be decomposed into sine and cosine components that always sum to maintain constant energy.",
        "application": "The fundamental identity sin²(θ) + cos²(θ) = 1 ensures energy conservation in wave mechanics"
    },
    {
        "context": "In signal processing and telecommunications, signals are often represented as combinations of sine and cosine waves (Fourier analysis). The Pythagorean identity ensures signal power remains constant.",
        "application": "Quality assurance in digital signal transmission depends on this fundamental relationship"
    },
    {
        "context": "In navigation systems (GPS, radar), the position of an object can be represented in both rectangular (x, y) and polar (r, θ) coordinates. The conversion relies on the Pythagorean identity.",
        "application": "Converting between coordinate systems while maintaining accuracy"
    },
    {
        "context": "In structural engineering, forces acting on a beam can be decomposed into horizontal and vertical components. The total force magnitude must satisfy the Pythagorean relationship.",
        "application": "Calculating resultant forces in bridge and building design"
    },
]


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
        use_word_problem = random.random() < 0.4
        angles = [
            (30, "\\frac{\\pi}{6}", 0.5, math.sqrt(3)/2, "\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}"),
            (45, "\\frac{\\pi}{4}", math.sqrt(2)/2, math.sqrt(2)/2, "\\frac{\\sqrt{2}}{2}", "\\frac{\\sqrt{2}}{2}"),
            (60, "\\frac{\\pi}{3}", math.sqrt(3)/2, 0.5, "\\frac{\\sqrt{3}}{2}", "\\frac{1}{2}"),
        ]

        degrees, radian_str, sin_val, cos_val, sin_str, cos_str = random.choice(angles)

        if use_word_problem:
            question = f"**Physics Application:** In oscillatory motion at angle ${degrees}°$, the vertical and horizontal components must conserve energy. Verify that $\\sin^2({degrees}°) + \\cos^2({degrees}°) = 1$ using exact values. This fundamental identity ensures energy is neither created nor destroyed."
        else:
            question = f"Verify that $\\sin^2({degrees}°) + \\cos^2({degrees}°) = 1$ using exact values."

        steps = [
            f"**Step 1 - Recall the exact values:**",
            f"$\\sin({degrees}°) = {sin_str}$ and $\\cos({degrees}°) = {cos_str}$",
            "",
            f"**Step 2 - Square the sine value:**",
            f"$\\sin^2({degrees}°) = ({sin_str})^2 = {round(sin_val**2, 4)}$",
            "",
            f"**Step 3 - Square the cosine value:**",
            f"$\\cos^2({degrees}°) = ({cos_str})^2 = {round(cos_val**2, 4)}$",
            "",
            f"**Step 4 - Add the squared components together:**",
            f"$\\sin^2({degrees}°) + \\cos^2({degrees}°) = {round(sin_val**2, 4)} + {round(cos_val**2, 4)} = 1$",
            "",
            "This demonstrates that the identity holds perfectly at this angle, confirming the fundamental relationship between sine and cosine.",
            "**Final Answer:** Identity verified: $1$"
        ]

        answer_numeric = 1

    elif difficulty == 2:
        # Medium: Given sin, find cos (or vice versa) using Pythagorean identity
        # Use fractions for exact values
        use_word_problem = random.random() < 0.4
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

        if use_word_problem:
            question = f"**GPS Navigation:** A satellite's position requires both sine and cosine components. If $\\{given_func}(\\theta) = {given_str}$ and $\\theta$ is in Quadrant I (first quadrant), find $\\{find_func}(\\theta)$ using the fundamental identity. This is essential for accurate position calculation."
        else:
            question = f"If $\\{given_func}(\\theta) = {given_str}$ and $\\theta$ is in Quadrant I, find $\\{find_func}(\\theta)$."

        steps = [
            f"**Step 1 - Apply the Pythagorean identity:**",
            f"The fundamental identity is: $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$",
            "",
        ]

        if given_func == "sin":
            steps.append(f"**Step 2 - Substitute the known sine value:**")
            steps.append(f"$({given_str})^2 + \\cos^2(\\theta) = 1$")
            steps.append(f"$\\frac{{{num**2}}}{{{den**2}}} + \\cos^2(\\theta) = 1$")
            steps.append("")
            steps.append(f"**Step 3 - Isolate the cosine squared term:**")
            steps.append(f"$\\cos^2(\\theta) = 1 - \\frac{{{num**2}}}{{{den**2}}}$")
            steps.append(f"$\\cos^2(\\theta) = \\frac{{{den**2}}}{{{den**2}}} - \\frac{{{num**2}}}{{{den**2}}}$")
            steps.append(f"$\\cos^2(\\theta) = \\frac{{{den**2 - num**2}}}{{{den**2}}}$")
            steps.append("")
            steps.append(f"**Step 4 - Take the square root of both sides:**")
            steps.append(f"$\\cos(\\theta) = \\pm\\sqrt{{\\frac{{{den**2 - num**2}}}{{{den**2}}}}} = \\pm\\frac{{\\sqrt{{{den**2 - num**2}}}}}{{{den}}}$")
            steps.append("")
            steps.append(f"**Step 5 - Determine the sign based on quadrant:**")
            steps.append(f"Since $\\theta$ is in Quadrant I, both sine and cosine are positive")
            steps.append(f"$\\cos(\\theta) = \\frac{{{other_num}}}{{{other_den}}}$ (taking the positive root)")
        else:
            steps.append(f"**Step 2 - Substitute the known cosine value:**")
            steps.append(f"$\\sin^2(\\theta) + ({given_str})^2 = 1$")
            steps.append(f"$\\sin^2(\\theta) + \\frac{{{other_num**2}}}{{{other_den**2}}} = 1$")
            steps.append("")
            steps.append(f"**Step 3 - Isolate the sine squared term:**")
            steps.append(f"$\\sin^2(\\theta) = 1 - \\frac{{{other_num**2}}}{{{other_den**2}}}$")
            steps.append(f"$\\sin^2(\\theta) = \\frac{{{other_den**2 - other_num**2}}}{{{other_den**2}}}$")
            steps.append("")
            steps.append(f"**Step 4 - Take the square root:**")
            steps.append(f"$\\sin(\\theta) = \\pm\\frac{{\\sqrt{{{other_den**2 - other_num**2}}}}}{{{other_den}}}$")
            steps.append("")
            steps.append(f"**Step 5 - Determine the sign (Quadrant I is positive):**")
            steps.append(f"$\\sin(\\theta) = \\frac{{{num}}}{{{den}}}$")

        steps.append("")
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
