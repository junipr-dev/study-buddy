"""Trigonometric equations question generator."""

import random
import math
from typing import Dict, Any

# Real-world contexts for trigonometric equations
WORD_PROBLEMS = [
    {
        "context": "Oscillatory motion: Finding when a pendulum reaches maximum height or returns to equilibrium.",
        "application": "Timing analysis in mechanical and physics systems"
    },
    {
        "context": "Electrical engineering: AC circuit analysis where voltage/current follows sinusoidal patterns.",
        "application": "Finding when voltage reaches specific values"
    },
    {
        "context": "Astronomy: Predicting planetary positions and celestial events.",
        "application": "Orbital calculations and eclipse predictions"
    },
    {
        "context": "Climate science: Modeling seasonal temperature and precipitation patterns.",
        "application": "Predicting extreme weather timing"
    },
    {
        "context": "Music and acoustics: Finding frequencies and harmonics that produce specific notes.",
        "application": "Instrument tuning and sound synthesis"
    },
]


def generate_trigonometric_equations(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate problems solving trigonometric equations.

    Args:
        difficulty: 1 (basic equations), 2 (quadratic-type equations), 3 (multiple angle equations)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Basic trigonometric equations like sin(x) = value
        use_word_problem = random.random() < 0.4
        equation_types = [
            ("sin", 0.5, 30, "\\frac{1}{2}"),
            ("sin", math.sqrt(2)/2, 45, "\\frac{\\sqrt{2}}{2}"),
            ("sin", math.sqrt(3)/2, 60, "\\frac{\\sqrt{3}}{2}"),
            ("cos", 0.5, 60, "\\frac{1}{2}"),
            ("cos", math.sqrt(2)/2, 45, "\\frac{\\sqrt{2}}{2}"),
            ("cos", math.sqrt(3)/2, 30, "\\frac{\\sqrt{3}}{2}"),
            ("tan", 1, 45, "1"),
            ("tan", math.sqrt(3), 60, "\\sqrt{3}"),
        ]

        func, value, angle, value_str = random.choice(equation_types)

        # Also find the second solution in [0, 360)
        if func == "sin":
            angle2 = 180 - angle
        elif func == "cos":
            angle2 = 360 - angle
        else:  # tan
            angle2 = 180 + angle

        if use_word_problem:
            question = f"**Oscillating Motion:** A pendulum's position follows $\\{func}(x) = {value_str}$, where $x$ is the angle in degrees. Find all solutions in the interval $[0°, 360°)$ (one complete cycle of motion)."
        else:
            question = f"Solve for $x$ in the interval $[0°, 360°)$: $\\{func}(x) = {value_str}$"

        steps = [
            f"**Step 1 - Understand what we're solving:**",
            f"We need to find all angles $x$ where $\\{func}(x) = {value_str}$ in the range $[0°, 360°)$.",
            "",
            f"**Step 2 - Find the primary solution using the unit circle:**",
            f"From the unit circle, we know that $\\{func}({angle}°) = {value_str}$",
            f"So one solution is: $x = {angle}°$",
            "",
            f"**Step 3 - Find additional solutions based on function properties:**",
        ]

        if func == "sin":
            steps.append(f"Sine is positive in both Quadrant I and Quadrant II.")
            steps.append(f"In Quadrant II, if the reference angle is ${angle}°$, then:")
            steps.append(f"$x = 180° - {angle}° = {angle2}°$")
            steps.append("")
            steps.append(f"We can verify: $\\sin({angle2}°) = {value_str}$ ✓")
        elif func == "cos":
            steps.append(f"Cosine is positive in both Quadrant I and Quadrant IV.")
            steps.append(f"In Quadrant IV, if the reference angle is ${angle}°$, then:")
            steps.append(f"$x = 360° - {angle}° = {angle2}°$")
            steps.append("")
            steps.append(f"We can verify: $\\cos({angle2}°) = {value_str}$ ✓")
        else:  # tan
            steps.append(f"Tangent has a period of $180°$ (it repeats every 180°).")
            steps.append(f"If $\\tan({angle}°) = {value_str}$, then the next solution is:")
            steps.append(f"$x = {angle}° + 180° = {angle2}°$")
            steps.append("")
            steps.append(f"We can verify: $\\tan({angle2}°) = {value_str}$ ✓")

        steps.append("")
        steps.append(f"**Final Answer:** $x = {angle}°$ or $x = {angle2}°$")

        answer_numeric = angle  # Return the first solution

    elif difficulty == 2:
        # Medium: Quadratic-type equations like 2sin²(x) - sin(x) = 0
        equation_type = random.choice(["factor", "quadratic_formula", "double_angle"])

        if equation_type == "factor":
            # 2sin(x)cos(x) = 0 type
            question = "Solve for $x$ in $[0°, 360°)$: $2\\sin(x)\\cos(x) = 0$"

            steps = [
                "This equation equals zero when either factor equals zero:",
                "**Case 1:** $\\sin(x) = 0$",
                "This occurs at $x = 0°, 180°, 360°$",
                "In $[0°, 360°)$: $x = 0°, 180°$",
                "",
                "**Case 2:** $\\cos(x) = 0$",
                "This occurs at $x = 90°, 270°$",
                "",
                "**Final Answer:** $x = 0°, 90°, 180°, 270°$"
            ]

            answer_numeric = 0

        elif equation_type == "quadratic_formula":
            # 2sin²(x) - sin(x) = 0
            question = "Solve for $x$ in $[0°, 360°)$: $2\\sin^2(x) - \\sin(x) = 0$"

            steps = [
                "Factor out $\\sin(x)$:",
                "$\\sin(x)(2\\sin(x) - 1) = 0$",
                "",
                "**Case 1:** $\\sin(x) = 0$",
                "$x = 0°, 180°$",
                "",
                "**Case 2:** $2\\sin(x) - 1 = 0$",
                "$\\sin(x) = \\frac{1}{2}$",
                "$x = 30°, 150°$ (Quadrants I and II)",
                "",
                "**Final Answer:** $x = 0°, 30°, 150°, 180°$"
            ]

            answer_numeric = 0

        else:  # double_angle
            # Using double angle identity
            question = "Solve for $x$ in $[0°, 360°)$: $\\cos(2x) = \\cos(x)$"

            steps = [
                "Use the double angle formula: $\\cos(2x) = 2\\cos^2(x) - 1$",
                "Substitute: $2\\cos^2(x) - 1 = \\cos(x)$",
                "Rearrange: $2\\cos^2(x) - \\cos(x) - 1 = 0$",
                "Factor: $(2\\cos(x) + 1)(\\cos(x) - 1) = 0$",
                "",
                "**Case 1:** $2\\cos(x) + 1 = 0$",
                "$\\cos(x) = -\\frac{1}{2}$",
                "$x = 120°, 240°$",
                "",
                "**Case 2:** $\\cos(x) - 1 = 0$",
                "$\\cos(x) = 1$",
                "$x = 0°$",
                "",
                "**Final Answer:** $x = 0°, 120°, 240°$"
            ]

            answer_numeric = 0

    else:
        # Hard: More complex equations with multiple angles or identities
        complex_types = ["multiple_angle", "identity_substitution", "sum_formula"]

        comp_type = random.choice(complex_types)

        if comp_type == "multiple_angle":
            # sin(2x) = 1/2
            question = "Solve for $x$ in $[0°, 360°)$: $\\sin(2x) = \\frac{1}{2}$"

            steps = [
                "Let $u = 2x$, so we need $\\sin(u) = \\frac{1}{2}$",
                "Since $x \\in [0°, 360°)$, we have $u \\in [0°, 720°)$",
                "$\\sin(u) = \\frac{1}{2}$ when $u = 30°, 150°, 390°, 510°$",
                "",
                "Solve for $x$ by dividing by 2:",
                "$x = 15°$ (from $u = 30°$)",
                "$x = 75°$ (from $u = 150°$)",
                "$x = 195°$ (from $u = 390°$)",
                "$x = 255°$ (from $u = 510°$)",
                "",
                "**Final Answer:** $x = 15°, 75°, 195°, 255°$"
            ]

            answer_numeric = 15

        elif comp_type == "identity_substitution":
            # 1 - cos²(x) = 3/4
            question = "Solve for $x$ in $[0°, 360°)$: $1 - \\cos^2(x) = \\frac{3}{4}$"

            steps = [
                "Use the identity: $\\sin^2(x) + \\cos^2(x) = 1$",
                "Therefore: $1 - \\cos^2(x) = \\sin^2(x)$",
                "Substitute: $\\sin^2(x) = \\frac{3}{4}$",
                "Take the square root: $\\sin(x) = \\pm\\frac{\\sqrt{3}}{2}$",
                "",
                "**Case 1:** $\\sin(x) = \\frac{\\sqrt{3}}{2}$",
                "$x = 60°, 120°$ (Quadrants I and II)",
                "",
                "**Case 2:** $\\sin(x) = -\\frac{\\sqrt{3}}{2}$",
                "$x = 240°, 300°$ (Quadrants III and IV)",
                "",
                "**Final Answer:** $x = 60°, 120°, 240°, 300°$"
            ]

            answer_numeric = 60

        else:  # sum_formula
            # tan(x) + 1 = 0
            question = "Solve for $x$ in $[0°, 360°)$: $\\tan(x) + 1 = 0$"

            steps = [
                "Rearrange: $\\tan(x) = -1$",
                "From the unit circle, $\\tan(45°) = 1$",
                "We need $\\tan(x) = -1$, which occurs when:",
                "- $x$ is in Quadrant II: $x = 180° - 45° = 135°$",
                "- $x$ is in Quadrant IV: $x = 360° - 45° = 315°$",
                "",
                "Since tangent has period $180°$, these are all solutions in $[0°, 360°)$",
                "",
                "**Final Answer:** $x = 135°, 315°$"
            ]

            answer_numeric = 135

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
