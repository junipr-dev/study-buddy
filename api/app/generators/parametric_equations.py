"""Parametric equations question generator."""

import random
from typing import Dict, Any


def generate_parametric_equations(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a parametric equations problem.

    Args:
        difficulty: 1 (evaluate at t), 2 (eliminate parameter), 3 (find t for given point)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Evaluate x or y at a specific t value
        a = random.randint(2, 5)
        b = random.randint(-5, 5)
        c = random.randint(2, 5)
        d = random.randint(-5, 5)
        t_val = random.randint(1, 4)

        # Choose whether to ask for x or y
        if random.choice([True, False]):
            # Ask for x
            x_result = a * t_val + b

            question = f"Given the parametric equations $x = {a}t {b:+d}$ and $y = {c}t {d:+d}$, find the value of $x$ when $t = {t_val}$."

            steps = [
                f"We have $x = {a}t {b:+d}$",
                "",
                f"Substitute $t = {t_val}$:",
                f"$x = {a}({t_val}) {b:+d}$",
                f"$x = {a * t_val} {b:+d}$",
                f"$x = {x_result}$",
                "",
                f"**Final Answer:** ${x_result}$"
            ]

            answer_numeric = x_result
        else:
            # Ask for y
            y_result = c * t_val + d

            question = f"Given the parametric equations $x = {a}t {b:+d}$ and $y = {c}t {d:+d}$, find the value of $y$ when $t = {t_val}$."

            steps = [
                f"We have $y = {c}t {d:+d}$",
                "",
                f"Substitute $t = {t_val}$:",
                f"$y = {c}({t_val}) {d:+d}$",
                f"$y = {c * t_val} {d:+d}$",
                f"$y = {y_result}$",
                "",
                f"**Final Answer:** ${y_result}$"
            ]

            answer_numeric = y_result

    elif difficulty == 2:
        # Medium: Eliminate parameter to find slope
        # x = at + b, y = ct + d
        # Solving for t from x: t = (x - b)/a
        # Substituting: y = c((x-b)/a) + d = (c/a)x - (bc/a) + d
        # Slope is c/a
        a = random.randint(2, 4)
        b = random.randint(-3, 3)
        c = random.randint(2, 6)
        d = random.randint(-3, 3)

        slope = c / a
        if slope == int(slope):
            slope = int(slope)
            answer_numeric = slope
        else:
            answer_numeric = round(slope, 2)

        question = f"Eliminate the parameter $t$ from the parametric equations $x = {a}t {b:+d}$ and $y = {c}t {d:+d}$ to find the slope of the resulting line."

        steps = [
            "**Step 1:** Solve for $t$ from the $x$ equation:",
            f"$x = {a}t {b:+d}$",
            f"$x {-b:+d} = {a}t$",
            f"$t = \\frac{{x {-b:+d}}}{{{a}}}$",
            "",
            "**Step 2:** Substitute into the $y$ equation:",
            f"$y = {c}t {d:+d}$",
            f"$y = {c} \\cdot \\frac{{x {-b:+d}}}{{{a}}} {d:+d}$",
            f"$y = \\frac{{{c}}}{{{a}}}x - \\frac{{{c * b}}}{{{a}}} {d:+d}$",
            "",
            "**Step 3:** Identify the slope:",
            f"The equation is in the form $y = mx + b$ where $m = \\frac{{{c}}}{{{a}}}$",
        ]

        if slope == int(slope):
            steps.append(f"$m = {int(slope)}$")
            steps.append("")
            steps.append(f"**Final Answer:** ${int(slope)}$")
        else:
            steps.append(f"$m = {answer_numeric}$")
            steps.append("")
            steps.append(f"**Final Answer:** ${answer_numeric}$")

    else:
        # Hard: Find t value for a given point
        # Use simple parametric equations and compute a point on the curve
        a = random.randint(2, 4)
        b = random.randint(1, 3)
        t_val = random.randint(2, 4)

        # x = at, y = t²
        x_point = a * t_val
        y_point = t_val ** 2

        question = f"Given the parametric equations $x = {a}t$ and $y = t^2$, find the value of $t$ when the point is $({x_point}, {y_point})$."

        steps = [
            f"We need to find $t$ such that $x = {x_point}$ and $y = {y_point}$.",
            "",
            "**Method 1: Use the $x$ equation**",
            f"$x = {a}t = {x_point}$",
            f"$t = \\frac{{{x_point}}}{{{a}}}$",
            f"$t = {t_val}$",
            "",
            "**Verify with the $y$ equation:**",
            f"$y = t^2 = ({t_val})^2 = {y_point}$ ✓",
            "",
            f"**Final Answer:** ${t_val}$"
        ]

        answer_numeric = t_val

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
