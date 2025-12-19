"""Point-slope form generator."""

import random
from typing import Dict, Any, List


def generate_point_slope_form(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate point-slope form problems.

    Args:
        difficulty: 1 (convert to slope-intercept), 2 (write from point and slope), 3 (from two points)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Convert from point-slope to slope-intercept form
        m = random.randint(-6, 6)
        if m == 0:
            m = 2
        x1 = random.randint(-5, 5)
        y1 = random.randint(-8, 8)

        # Point-slope form: y - y1 = m(x - x1)
        point_slope = f"y - ({y1})" if y1 < 0 else f"y - {y1}"
        point_slope += f" = {m}(x - ({x1}))" if x1 < 0 else f" = {m}(x - {x1})"

        # Calculate slope-intercept form
        b = y1 - m * x1
        slope_intercept = f"y = {m}x {'+' if b >= 0 else '-'} {abs(b)}" if b != 0 else f"y = {m}x"
        if m == 1:
            slope_intercept = f"y = x {'+' if b >= 0 else '-'} {abs(b)}" if b != 0 else "y = x"
        elif m == -1:
            slope_intercept = f"y = -x {'+' if b >= 0 else '-'} {abs(b)}" if b != 0 else "y = -x"

        steps = [
            f"Start with point-slope form: ${point_slope}$",
            f"Distribute ${m}$ on the right side:",
            f"$y - {y1} = {m} \\cdot x - {m} \\cdot {x1}$",
            f"$y - {y1} = {m}x {'-' if m*x1 >= 0 else '+'} {abs(m*x1)}$",
            f"Add ${y1}$ to both sides to isolate $y$:",
            f"$y = {m}x {'-' if m*x1 >= 0 else '+'} {abs(m*x1)} {'+' if y1 >= 0 else '-'} {abs(y1)}$",
            f"Simplify:",
            f"${slope_intercept}$",
            f"**Final Answer:** ${slope_intercept}$"
        ]

        answer = slope_intercept

    elif difficulty == 2:
        # Write point-slope equation from point and slope
        m = random.randint(-5, 5)
        if m == 0:
            m = 3
        x1 = random.randint(-6, 6)
        y1 = random.randint(-8, 8)

        # Point-slope form
        point_slope = f"y - ({y1})" if y1 < 0 else f"y - {y1}"
        point_slope += f" = {m}(x - ({x1}))" if x1 < 0 else f" = {m}(x - {x1})"

        # Simplify if possible
        if y1 == 0:
            point_slope = f"y = {m}(x - {x1})" if x1 >= 0 else f"y = {m}(x - ({x1}))"
        if x1 == 0:
            point_slope = f"y - {y1} = {m}x" if y1 >= 0 else f"y - ({y1}) = {m}x"
        if m == 1:
            point_slope = point_slope.replace(f"{m}(", "(")
        elif m == -1:
            point_slope = point_slope.replace(f"{m}(", "-(")

        steps = [
            f"Given:",
            f"- Point: $({x1}, {y1})$",
            f"- Slope: $m = {m}$",
            f"Use point-slope form: $y - y_1 = m(x - x_1)$",
            f"Substitute the given values:",
            f"${point_slope}$",
            f"**Final Answer:** ${point_slope}$"
        ]

        answer = point_slope

    else:  # difficulty == 3
        # Find equation from two points
        x1 = random.randint(-6, 3)
        y1 = random.randint(-8, 8)
        x2 = random.randint(x1 + 1, x1 + 6)
        y2 = random.randint(-8, 8)

        # Ensure different y-values for non-horizontal line
        while y1 == y2:
            y2 = random.randint(-8, 8)

        # Calculate slope
        m = (y2 - y1) // (x2 - x1) if (y2 - y1) % (x2 - x1) == 0 else (y2 - y1) / (x2 - x1)

        # Use first point for point-slope form
        if isinstance(m, float):
            # Fraction slope
            from math import gcd
            g = gcd(abs(y2 - y1), abs(x2 - x1))
            m_num = (y2 - y1) // g
            m_den = (x2 - x1) // g
            m_str = f"\\frac{{{m_num}}}{{{m_den}}}"

            point_slope = f"y - ({y1})" if y1 < 0 else f"y - {y1}"
            point_slope += f" = {m_str}(x - ({x1}))" if x1 < 0 else f" = {m_str}(x - {x1})"

            steps = [
                f"Given two points: $({x1}, {y1})$ and $({x2}, {y2})$",
                f"First, find the slope using: $m = \\frac{{y_2 - y_1}}{{x_2 - x_1}}$",
                f"$m = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}}$" if y1 < 0 else f"$m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}}$",
                f"$m = \\frac{{{y2 - y1}}}{{{x2 - x1}}}$",
                f"Simplify: $m = {m_str}$",
                f"Now use point-slope form with point $({x1}, {y1})$:",
                f"$y - y_1 = m(x - x_1)$",
                f"${point_slope}$",
                f"**Final Answer:** ${point_slope}$"
            ]
        else:
            # Integer slope
            point_slope = f"y - ({y1})" if y1 < 0 else f"y - {y1}"
            point_slope += f" = {m}(x - ({x1}))" if x1 < 0 else f" = {m}(x - {x1})"

            if m == 1:
                point_slope = point_slope.replace(f"{m}(", "(")
            elif m == -1:
                point_slope = point_slope.replace(f"{m}(", "-(")

            steps = [
                f"Given two points: $({x1}, {y1})$ and $({x2}, {y2})$",
                f"First, find the slope using: $m = \\frac{{y_2 - y_1}}{{x_2 - x_1}}$",
                f"$m = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}}$" if y1 < 0 else f"$m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}}$",
                f"$m = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {m}$",
                f"Now use point-slope form with point $({x1}, {y1})$:",
                f"$y - y_1 = m(x - x_1)$",
                f"${point_slope}$",
                f"**Final Answer:** ${point_slope}$"
            ]

        answer = point_slope

    return {
        "question": (f"Convert to slope-intercept form: ${point_slope}$" if difficulty == 1 else
                    (f"Write the point-slope equation for a line with slope ${m}$ passing through $({x1}, {y1})$" if difficulty == 2 else
                     f"Find the equation in point-slope form for the line passing through $({x1}, {y1})$ and $({x2}, {y2})$")),
        "answer": answer,
        "answer_numeric": None,
        "steps": steps,
        "difficulty": difficulty,
    }
