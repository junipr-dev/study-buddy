"""Inverse trigonometric functions question generator."""

import random
import math
from typing import Dict, Any

# Real-world contexts for inverse trigonometric functions
WORD_PROBLEMS = [
    {
        "context": "Navigation and surveying: Given a known distance and angle measurement, you need to find the original angle of elevation.",
        "application": "Calculating angles from known sine/cosine/tangent values in land surveying"
    },
    {
        "context": "Robotics and mechanical engineering: Joint angles must be calculated from position coordinates.",
        "application": "Inverse kinematics - finding joint angles from end-effector positions"
    },
    {
        "context": "Signal processing: Converting signal magnitudes back to phase angles.",
        "application": "Phase angle recovery in digital signal processing"
    },
    {
        "context": "Astronomy: Finding the angle of celestial objects from their coordinates.",
        "application": "Calculating astronomical position angles"
    },
    {
        "context": "Architecture and construction: Converting measured ratios back to angles for structural designs.",
        "application": "Determining roof pitches and ramp angles from known dimensions"
    },
]


def generate_inverse_trig_functions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate problems about inverse trigonometric functions.

    Args:
        difficulty: 1 (evaluate at standard values), 2 (compositions), 3 (solve equations)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Evaluate inverse trig functions at standard values
        use_word_problem = random.random() < 0.4
        inv_values = [
            ("arcsin", 0, 0, "0"),
            ("arcsin", 0.5, 30, "\\frac{1}{2}"),
            ("arcsin", math.sqrt(2)/2, 45, "\\frac{\\sqrt{2}}{2}"),
            ("arcsin", math.sqrt(3)/2, 60, "\\frac{\\sqrt{3}}{2}"),
            ("arcsin", 1, 90, "1"),
            ("arcsin", -0.5, -30, "-\\frac{1}{2}"),
            ("arccos", 0, 90, "0"),
            ("arccos", 0.5, 60, "\\frac{1}{2}"),
            ("arccos", math.sqrt(2)/2, 45, "\\frac{\\sqrt{2}}{2}"),
            ("arccos", math.sqrt(3)/2, 30, "\\frac{\\sqrt{3}}{2}"),
            ("arccos", 1, 0, "1"),
            ("arctan", 0, 0, "0"),
            ("arctan", 1, 45, "1"),
            ("arctan", math.sqrt(3), 60, "\\sqrt{3}"),
            ("arctan", 1/math.sqrt(3), 30, "\\frac{1}{\\sqrt{3}}"),
        ]

        func, value, degrees, value_str = random.choice(inv_values)

        func_name = func[3:]  # "sin", "cos", or "tan"

        if use_word_problem:
            question = f"**Surveying Problem:** A land surveyor measures that the vertical-to-horizontal ratio is {value_str}. They need to find the angle of elevation. Evaluate $\\{func}({value_str})$ in degrees."
        else:
            question = f"Evaluate $\\{func}({value_str})$ in degrees."

        steps = [
            f"**Understanding the inverse function:**",
            f"$\\{func}(x)$ asks: 'What angle has a {func_name} of $x$?'",
            f"In other words: $\\{func}({value_str})$ means: Find $\\theta$ where $\\{func_name}(\\theta) = {value_str}$",
            "",
        ]

        if func == "arcsin":
            steps.append(f"**Setting up the equation:**")
            steps.append(f"We need: $\\sin(\\theta) = {value_str}$")
            steps.append("")
            steps.append(f"**Looking up the unit circle:**")
            steps.append(f"From memory or the unit circle, $\\sin({degrees}°) = {value_str}$")
            steps.append("")
            steps.append(f"**Checking the range:**")
            steps.append(f"Arcsin has a range of $[-90°, 90°]$ (also written as $[-\\frac{{\\pi}}{{2}}, \\frac{{\\pi}}{{2}}]$)")
            steps.append(f"Since ${degrees}°$ is in this range, it's our answer.")
        elif func == "arccos":
            steps.append(f"**Setting up the equation:**")
            steps.append(f"We need: $\\cos(\\theta) = {value_str}$")
            steps.append("")
            steps.append(f"**Looking up the unit circle:**")
            steps.append(f"From memory or the unit circle, $\\cos({degrees}°) = {value_str}$")
            steps.append("")
            steps.append(f"**Checking the range:**")
            steps.append(f"Arccos has a range of $[0°, 180°]$ (also written as $[0, \\pi]$)")
            steps.append(f"Since ${degrees}°$ is in this range, it's our answer.")
        else:  # arctan
            steps.append(f"**Setting up the equation:**")
            steps.append(f"We need: $\\tan(\\theta) = {value_str}$")
            steps.append("")
            steps.append(f"**Looking up the unit circle:**")
            steps.append(f"From memory or the unit circle, $\\tan({degrees}°) = {value_str}$")
            steps.append("")
            steps.append(f"**Checking the range:**")
            steps.append(f"Arctan has a range of $(-90°, 90°)$ (also written as $(-\\frac{{\\pi}}{{2}}, \\frac{{\\pi}}{{2}})$)")
            steps.append(f"Since ${degrees}°$ is in this range, it's our answer.")

        steps.append("")
        steps.append(f"**Final Answer:** ${degrees}°$")

        answer_numeric = degrees

    elif difficulty == 2:
        # Medium: Compositions of trig and inverse trig functions
        composition_types = [
            "sin_arcsin",
            "arcsin_sin",
            "cos_arccos",
            "nested"
        ]

        comp_type = random.choice(composition_types)

        if comp_type == "sin_arcsin":
            value = random.choice([0.5, math.sqrt(2)/2, math.sqrt(3)/2])

            if value == 0.5:
                value_str = "\\frac{1}{2}"
            elif value == math.sqrt(2)/2:
                value_str = "\\frac{\\sqrt{2}}{2}"
            else:
                value_str = "\\frac{\\sqrt{3}}{2}"

            question = f"Evaluate $\\sin(\\arcsin({value_str}))$."

            steps = [
                "Recall the composition property: $\\sin(\\arcsin(x)) = x$ for $x \\in [-1, 1]$",
                f"Since ${value_str}$ is in the domain of arcsin:",
                f"$\\sin(\\arcsin({value_str})) = {value_str}$",
                f"**Final Answer:** ${value_str}$"
            ]

            answer_numeric = round(value, 4)

        elif comp_type == "arcsin_sin":
            angle = random.choice([30, 45, 60])

            if angle == 30:
                result_str = "30"
                radians_str = "\\frac{\\pi}{6}"
            elif angle == 45:
                result_str = "45"
                radians_str = "\\frac{\\pi}{4}"
            else:
                result_str = "60"
                radians_str = "\\frac{\\pi}{3}"

            question = f"Evaluate $\\arcsin(\\sin({angle}°))$ in degrees."

            steps = [
                f"First, evaluate the inner function: $\\sin({angle}°)$",
                f"Since ${angle}°$ is in the range of arcsin $[-90°, 90°]$:",
                f"$\\arcsin(\\sin({angle}°)) = {angle}°$",
                "This works because arcsin 'undoes' sin when the angle is in range",
                f"**Final Answer:** ${angle}°$"
            ]

            answer_numeric = angle

        elif comp_type == "cos_arccos":
            value = random.choice([0.5, math.sqrt(2)/2, math.sqrt(3)/2])

            if value == 0.5:
                value_str = "\\frac{1}{2}"
            elif value == math.sqrt(2)/2:
                value_str = "\\frac{\\sqrt{2}}{2}"
            else:
                value_str = "\\frac{\\sqrt{3}}{2}"

            question = f"Evaluate $\\cos(\\arccos({value_str}))$."

            steps = [
                "Recall the composition property: $\\cos(\\arccos(x)) = x$ for $x \\in [-1, 1]$",
                f"Since ${value_str}$ is in the domain of arccos:",
                f"$\\cos(\\arccos({value_str})) = {value_str}$",
                f"**Final Answer:** ${value_str}$"
            ]

            answer_numeric = round(value, 4)

        else:  # nested
            # sin(arccos(x)) type problem
            value = 0.6
            value_str = "\\frac{3}{5}"

            question = f"Evaluate $\\sin(\\arccos({value_str}))$."

            steps = [
                f"Let $\\theta = \\arccos({value_str})$",
                f"This means $\\cos(\\theta) = {value_str}$",
                "We need to find $\\sin(\\theta)$",
                "Use the Pythagorean identity: $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$",
                f"$\\sin^2(\\theta) = 1 - \\cos^2(\\theta) = 1 - ({value_str})^2$",
                f"$\\sin^2(\\theta) = 1 - \\frac{{9}}{{25}} = \\frac{{16}}{{25}}$",
                "Since $\\arccos$ returns angles in $[0°, 180°]$, $\\sin(\\theta) \\geq 0$",
                f"$\\sin(\\theta) = \\frac{{4}}{{5}}$",
                f"**Final Answer:** $\\frac{{4}}{{5}}$"
            ]

            answer_numeric = 0.8

    else:
        # Hard: Solve equations involving inverse trig functions
        equation_types = [
            "simple_arcsin",
            "arctan_equation",
            "composition_equation"
        ]

        eq_type = random.choice(equation_types)

        if eq_type == "simple_arcsin":
            angle = random.choice([30, 45, 60])

            if angle == 30:
                answer_str = "\\frac{1}{2}"
                answer_val = 0.5
            elif angle == 45:
                answer_str = "\\frac{\\sqrt{2}}{2}"
                answer_val = math.sqrt(2)/2
            else:
                answer_str = "\\frac{\\sqrt{3}}{2}"
                answer_val = math.sqrt(3)/2

            question = f"Solve for $x$: $\\arcsin(x) = {angle}°$"

            steps = [
                "Take the sine of both sides:",
                f"$\\sin(\\arcsin(x)) = \\sin({angle}°)$",
                f"The left side simplifies to $x$:",
                f"$x = \\sin({angle}°)$",
                f"From the unit circle: $\\sin({angle}°) = {answer_str}$",
                f"**Final Answer:** $x = {answer_str}$"
            ]

            answer_numeric = round(answer_val, 4)

        elif eq_type == "arctan_equation":
            # arctan(x) = 45 degrees
            question = "Solve for $x$: $\\arctan(x) = 45°$"

            steps = [
                "Take the tangent of both sides:",
                "$\\tan(\\arctan(x)) = \\tan(45°)$",
                "The left side simplifies to $x$:",
                "$x = \\tan(45°)$",
                "From the unit circle: $\\tan(45°) = 1$",
                "**Final Answer:** $x = 1$"
            ]

            answer_numeric = 1

        else:  # composition_equation
            # 2*arcsin(x) = 90 degrees
            question = "Solve for $x$: $2\\arcsin(x) = 90°$"

            steps = [
                "Divide both sides by 2:",
                "$\\arcsin(x) = 45°$",
                "Take the sine of both sides:",
                "$\\sin(\\arcsin(x)) = \\sin(45°)$",
                "The left side simplifies to $x$:",
                "$x = \\sin(45°)$",
                "From the unit circle: $\\sin(45°) = \\frac{\\sqrt{2}}{2}$",
                "**Final Answer:** $x = \\frac{\\sqrt{2}}{2}$"
            ]

            answer_numeric = round(math.sqrt(2)/2, 4)

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
