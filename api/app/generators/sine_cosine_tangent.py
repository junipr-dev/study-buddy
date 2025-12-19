"""Basic trigonometric ratios question generator."""

import random
import math
from typing import Dict, Any


def generate_sine_cosine_tangent(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate basic trigonometric ratio problems.

    Args:
        difficulty: 1 (evaluate at standard angles), 2 (solve for angle), 3 (word problems)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Evaluate trig functions at standard angles
        # (degrees, radians_str, sin, cos, tan)
        standard_angles = [
            (0, "0", 0, 1, 0),
            (30, "\\frac{\\pi}{6}", 0.5, math.sqrt(3)/2, 1/math.sqrt(3)),
            (45, "\\frac{\\pi}{4}", math.sqrt(2)/2, math.sqrt(2)/2, 1),
            (60, "\\frac{\\pi}{3}", math.sqrt(3)/2, 0.5, math.sqrt(3)),
            (90, "\\frac{\\pi}{2}", 1, 0, None),  # tan undefined
        ]

        degrees, radian_str, sin_val, cos_val, tan_val = random.choice(standard_angles)
        trig_func = random.choice(['sin', 'cos'] if tan_val is None else ['sin', 'cos', 'tan'])

        if trig_func == 'sin':
            value = sin_val
            if value == 0:
                value_str = "0"
            elif value == 1:
                value_str = "1"
            elif value == 0.5:
                value_str = "\\frac{1}{2}"
            elif value == math.sqrt(2)/2:
                value_str = "\\frac{\\sqrt{2}}{2}"
            elif value == math.sqrt(3)/2:
                value_str = "\\frac{\\sqrt{3}}{2}"
        elif trig_func == 'cos':
            value = cos_val
            if value == 0:
                value_str = "0"
            elif value == 1:
                value_str = "1"
            elif value == 0.5:
                value_str = "\\frac{1}{2}"
            elif value == math.sqrt(2)/2:
                value_str = "\\frac{\\sqrt{2}}{2}"
            elif value == math.sqrt(3)/2:
                value_str = "\\frac{\\sqrt{3}}{2}"
        else:  # tan
            value = tan_val
            if value == 0:
                value_str = "0"
            elif value == 1:
                value_str = "1"
            elif value == 1/math.sqrt(3):
                value_str = "\\frac{1}{\\sqrt{3}} = \\frac{\\sqrt{3}}{3}"
            elif value == math.sqrt(3):
                value_str = "\\sqrt{3}"

        question = f"Evaluate $\\{trig_func}({degrees}°)$."

        steps = [
            f"${degrees}°$ is equivalent to ${radian_str}$ radians",
            f"This is a standard angle on the unit circle",
        ]

        if trig_func == 'sin':
            steps.append(f"$\\sin({degrees}°)$ is the $y$-coordinate on the unit circle")
            steps.append(f"At ${degrees}°$, the $y$-coordinate is ${value_str}$")
        elif trig_func == 'cos':
            steps.append(f"$\\cos({degrees}°)$ is the $x$-coordinate on the unit circle")
            steps.append(f"At ${degrees}°$, the $x$-coordinate is ${value_str}$")
        else:
            steps.append(f"$\\tan({degrees}°) = \\frac{{\\sin({degrees}°)}}{{\\cos({degrees}°)}}$")
            steps.append(f"$\\tan({degrees}°) = {value_str}$")

        steps.append(f"**Final Answer:** ${value_str}$")
        answer_numeric = round(value, 4)

    elif difficulty == 2:
        # Medium: Find the angle given a trig value
        # Use inverse relationships
        angle_values = [
            (30, "\\frac{\\pi}{6}", "sin", 0.5, "\\frac{1}{2}"),
            (30, "\\frac{\\pi}{6}", "cos", math.sqrt(3)/2, "\\frac{\\sqrt{3}}{2}"),
            (45, "\\frac{\\pi}{4}", "sin", math.sqrt(2)/2, "\\frac{\\sqrt{2}}{2}"),
            (45, "\\frac{\\pi}{4}", "cos", math.sqrt(2)/2, "\\frac{\\sqrt{2}}{2}"),
            (60, "\\frac{\\pi}{3}", "sin", math.sqrt(3)/2, "\\frac{\\sqrt{3}}{2}"),
            (60, "\\frac{\\pi}{3}", "cos", 0.5, "\\frac{1}{2}"),
            (0, "0", "sin", 0, "0"),
            (90, "\\frac{\\pi}{2}", "sin", 1, "1"),
            (0, "0", "cos", 1, "1"),
        ]

        degrees, radian_str, func, value, value_str = random.choice(angle_values)

        question = f"Find the angle $\\theta$ (in degrees, where $0° \\leq \\theta \\leq 90°$) such that $\\{func}(\\theta) = {value_str}$."

        steps = [
            f"We need to find $\\theta$ where $\\{func}(\\theta) = {value_str}$",
            "Recall the standard angle values:",
        ]

        if func == "sin":
            steps.append("$\\sin(0°) = 0$, $\\sin(30°) = \\frac{1}{2}$, $\\sin(45°) = \\frac{\\sqrt{2}}{2}$, $\\sin(60°) = \\frac{\\sqrt{3}}{2}$, $\\sin(90°) = 1$")
        else:
            steps.append("$\\cos(0°) = 1$, $\\cos(30°) = \\frac{\\sqrt{3}}{2}$, $\\cos(45°) = \\frac{\\sqrt{2}}{2}$, $\\cos(60°) = \\frac{1}{2}$, $\\cos(90°) = 0$")

        steps.append(f"Comparing with ${value_str}$, we find:")
        steps.append(f"**Final Answer:** $\\theta = {degrees}°$")

        answer_numeric = degrees

    else:
        # Hard: Right triangle word problems
        problem_types = ["ladder", "ramp", "height"]
        problem_type = random.choice(problem_types)

        if problem_type == "ladder":
            # Ladder against wall - find height or angle
            length = random.choice([10, 12, 15, 20])
            angle = random.choice([30, 45, 60])

            if angle == 30:
                height = length * 0.5
                height_str = f"{length}/2 = {height}"
            elif angle == 45:
                height = length * math.sqrt(2)/2
                height_str = f"{length} \\cdot \\frac{{\\sqrt{{2}}}}{{2}} \\approx {round(height, 2)}"
            else:  # 60
                height = length * math.sqrt(3)/2
                height_str = f"{length} \\cdot \\frac{{\\sqrt{{3}}}}{{2}} \\approx {round(height, 2)}"

            question = f"A {length}-foot ladder leans against a wall at an angle of ${angle}°$ from the ground. How high up the wall does the ladder reach?"

            steps = [
                "Draw a right triangle where:",
                f"- Hypotenuse = ladder length = ${length}$ feet",
                "- Height = opposite side to the angle",
                f"Use the sine ratio: $\\sin(\\theta) = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}}$",
                f"Substitute: $\\sin({angle}°) = \\frac{{h}}{{{length}}}$",
                f"Solve for height: $h = {length} \\cdot \\sin({angle}°)$",
                f"Calculate: $h = {height_str}$ feet",
                f"**Final Answer:** ${round(height, 2)}$ feet"
            ]

            answer_numeric = round(height, 2)

        elif problem_type == "ramp":
            # Wheelchair ramp - find length or angle
            height = random.choice([2, 3, 4])
            angle = random.choice([5, 10, 15])  # ADA compliant angles

            # Using sin(angle) = height/length
            length = height / math.sin(math.radians(angle))

            question = f"A wheelchair ramp must rise ${height}$ feet at an angle of ${angle}°$. How long must the ramp be?"

            steps = [
                "Draw a right triangle where:",
                f"- Height (rise) = ${height}$ feet",
                f"- Angle = ${angle}°$",
                "- Length of ramp = hypotenuse",
                f"Use the sine ratio: $\\sin(\\theta) = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}}$",
                f"Substitute: $\\sin({angle}°) = \\frac{{{height}}}{{L}}$",
                f"Solve for length: $L = \\frac{{{height}}}{{\\sin({angle}°)}}$",
                f"Calculate: $L \\approx {round(length, 2)}$ feet",
                f"**Final Answer:** ${round(length, 2)}$ feet"
            ]

            answer_numeric = round(length, 2)

        else:  # height
            # Tree height from distance and angle
            distance = random.choice([30, 40, 50, 60])
            angle = random.choice([30, 45, 60])

            if angle == 30:
                height = distance / math.sqrt(3)
                height_str = f"{distance}/\\sqrt{{3}} \\approx {round(height, 2)}"
            elif angle == 45:
                height = distance
                height_str = f"{distance}"
            else:  # 60
                height = distance * math.sqrt(3)
                height_str = f"{distance}\\sqrt{{3}} \\approx {round(height, 2)}"

            question = f"From a point ${distance}$ feet from the base of a tree, the angle of elevation to the top is ${angle}°$. How tall is the tree?"

            steps = [
                "Draw a right triangle where:",
                f"- Base = distance from tree = ${distance}$ feet",
                "- Height = tree height",
                f"- Angle of elevation = ${angle}°$",
                f"Use the tangent ratio: $\\tan(\\theta) = \\frac{{\\text{{opposite}}}}{{\\text{{adjacent}}}}$",
                f"Substitute: $\\tan({angle}°) = \\frac{{h}}{{{distance}}}$",
                f"Solve for height: $h = {distance} \\cdot \\tan({angle}°)$",
                f"Calculate: $h = {height_str}$ feet",
                f"**Final Answer:** ${round(height, 2)}$ feet"
            ]

            answer_numeric = round(height, 2)

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
