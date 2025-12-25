"""Polar coordinates question generator."""

import random
import math
from typing import Dict, Any

# Word problem templates for engaging, real-world contexts
POLAR_WORD_PROBLEMS = [
    {
        "context": "A radar system tracks an aircraft at angle {angle_deg}° from the reference direction and distance {r} km.",
        "difficulty": 1,
        "type": "convert_polar_to_rect"
    },
    {
        "context": "A flower's petal pattern follows a spiral in polar coordinates. At angle {angle_deg}°, the distance is {r} units from the center.",
        "difficulty": 1,
        "type": "convert_polar_to_rect"
    },
    {
        "context": "A GPS system receives coordinates from a satellite. The satellite is at position ({x}, {y}) in rectangular coordinates.",
        "difficulty": 2,
        "type": "convert_rect_to_polar_r"
    },
    {
        "context": "A robot navigates by converting between coordinate systems. It detects an object at rectangular position ({x}, {y}).",
        "difficulty": 2,
        "type": "convert_rect_to_polar_r"
    },
    {
        "context": "A ship uses polar navigation with a compass bearing. It receives a location at rectangular coordinates ({x}, {y}).",
        "difficulty": 3,
        "type": "convert_rect_to_polar_theta"
    },
    {
        "context": "An antenna rotates and measures distances. A target is located at rectangular position ({x}, {y}).",
        "difficulty": 3,
        "type": "convert_rect_to_polar_theta"
    }
]


def generate_polar_coordinates(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a polar coordinates conversion problem.

    Args:
        difficulty: 1 (polar to rectangular), 2 (rectangular to polar - r), 3 (rectangular to polar - θ)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Convert polar to rectangular (find x or y)
        # Use special angles for clean answers
        angles_deg = [0, 30, 45, 60, 90, 120, 135, 150, 180]
        angle_deg = random.choice(angles_deg)
        angle_rad = math.radians(angle_deg)
        r = random.randint(2, 6)
        use_word_problem = random.random() < 0.4

        x = r * math.cos(angle_rad)
        y = r * math.sin(angle_rad)

        # Round to 2 decimal places
        x = round(x, 2)
        y = round(y, 2)

        # Choose whether to ask for x or y
        if random.choice([True, False]):
            if use_word_problem:
                context = random.choice([p for p in POLAR_WORD_PROBLEMS if p["difficulty"] == 1])
                context_text = context["context"].format(angle_deg=angle_deg, r=r, x=x, y=y)
                question = f"{context_text}\n\nConvert to rectangular coordinates and find the $x$-coordinate."
            else:
                question = f"Convert the polar coordinates $(r, \\theta) = ({r}, {angle_deg}°)$ to rectangular coordinates and find the $x$-coordinate."

            cos_val_str = {
                0: "1", 30: "\\frac{\\sqrt{3}}{2}", 45: "\\frac{\\sqrt{2}}{2}",
                60: "\\frac{1}{2}", 90: "0", 120: "-\\frac{1}{2}",
                135: "-\\frac{\\sqrt{2}}{2}", 150: "-\\frac{\\sqrt{3}}{2}", 180: "-1"
            }.get(angle_deg, f"\\cos({angle_deg}°)")

            steps = [
                "Use the conversion formula: $x = r\\cos(\\theta)$",
                "",
                f"Calculate the $x$-coordinate:",
                f"$x = r\\cos(\\theta) = {r} \\cdot \\cos({angle_deg}°)$",
                f"$x = {r} \\cdot {cos_val_str}$",
                f"$x \\approx {x}$",
                "",
                f"**Final Answer:** ${x}$"
            ]

            answer_numeric = x
        else:
            if use_word_problem:
                context = random.choice([p for p in POLAR_WORD_PROBLEMS if p["difficulty"] == 1])
                context_text = context["context"].format(angle_deg=angle_deg, r=r, x=x, y=y)
                question = f"{context_text}\n\nConvert to rectangular coordinates and find the $y$-coordinate."
            else:
                question = f"Convert the polar coordinates $(r, \\theta) = ({r}, {angle_deg}°)$ to rectangular coordinates and find the $y$-coordinate."

            sin_val_str = {
                0: "0", 30: "\\frac{1}{2}", 45: "\\frac{\\sqrt{2}}{2}",
                60: "\\frac{\\sqrt{3}}{2}", 90: "1", 120: "\\frac{\\sqrt{3}}{2}",
                135: "\\frac{\\sqrt{2}}{2}", 150: "\\frac{1}{2}", 180: "0"
            }.get(angle_deg, f"\\sin({angle_deg}°)")

            steps = [
                "Use the conversion formula: $y = r\\sin(\\theta)$",
                "",
                f"Calculate the $y$-coordinate:",
                f"$y = r\\sin(\\theta) = {r} \\cdot \\sin({angle_deg}°)$",
                f"$y = {r} \\cdot {sin_val_str}$",
                f"$y \\approx {y}$",
                "",
                f"**Final Answer:** ${y}$"
            ]

            answer_numeric = y

    elif difficulty == 2:
        # Medium: Convert rectangular to polar (find r)
        # Use Pythagorean triples scaled
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10)]
        x, y, r = random.choice(triples)
        use_word_problem = random.random() < 0.4

        # Randomly negate coordinates
        if random.choice([True, False]):
            x = -x
        if random.choice([True, False]):
            y = -y

        if use_word_problem:
            context = random.choice([p for p in POLAR_WORD_PROBLEMS if p["difficulty"] == 2])
            context_text = context["context"].format(x=x, y=y, r=r)
            question = f"{context_text}\n\nConvert to polar coordinates and find $r$ (the distance from the origin)."
        else:
            question = f"Convert the rectangular coordinates $({x}, {y})$ to polar coordinates and find $r$ (the distance from the origin)."

        steps = [
            "To convert from rectangular to polar coordinates, use the distance formula:",
            "$r = \\sqrt{x^2 + y^2}$",
            "",
            f"Substitute the values:",
            f"$r = \\sqrt{{({x})^2 + ({y})^2}}$",
            f"$r = \\sqrt{{{x**2} + {y**2}}}$",
            f"$r = \\sqrt{{{x**2 + y**2}}}$",
            f"$r = {r}$ units",
            "",
            f"**Final Answer:** ${r}$ units"
        ]

        answer_numeric = r

    else:
        # Hard: Convert rectangular to polar (find θ in degrees)
        # Use points where arctangent gives nice angles
        angle_points = {
            0: (1, 0),
            30: (round(math.sqrt(3), 2), 1),
            45: (1, 1),
            60: (1, round(math.sqrt(3), 2)),
            90: (0, 1),
        }

        angle_deg = random.choice([30, 45, 60])
        base_x, base_y = angle_points[angle_deg]
        use_word_problem = random.random() < 0.4

        # Scale the point
        scale = random.randint(2, 4)
        x = round(base_x * scale, 2)
        y = round(base_y * scale, 2)

        if use_word_problem:
            context = random.choice([p for p in POLAR_WORD_PROBLEMS if p["difficulty"] == 3])
            context_text = context["context"].format(x=x, y=y, angle_deg=angle_deg)
            question = f"{context_text}\n\nConvert to polar coordinates and find $\\theta$ in degrees (in the range $[0°, 360°)$). Round to the nearest whole degree."
        else:
            question = f"Convert the rectangular coordinates $({x}, {y})$ to polar coordinates (in the range $[0°, 360°)$) and find $\\theta$ in degrees. Round to the nearest whole degree."

        steps = [
            "To find the angle from rectangular coordinates, use:",
            "$\\theta = \\arctan\\left(\\frac{y}{x}\\right)$",
            "",
            f"Substitute the values:",
            f"$\\theta = \\arctan\\left(\\frac{{{y}}}{{{x}}}\\right)$",
        ]

        # Simplify the fraction if possible
        if y == x:
            steps.append(f"$\\theta = \\arctan(1) = 45°$")
        else:
            ratio = round(y / x, 2)
            steps.append(f"$\\theta = \\arctan({ratio})$")

        steps.extend([
            "",
            f"Since both $x > 0$ and $y > 0$, the point is in Quadrant I (northeast direction).",
            f"$\\theta \\approx {angle_deg}°$",
            "",
            f"**Final Answer:** ${angle_deg}°$"
        ])

        answer_numeric = angle_deg

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
