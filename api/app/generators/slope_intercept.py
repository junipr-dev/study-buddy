"""Slope-intercept form question generator."""

import random
from typing import Dict, Any
from fractions import Fraction


def generate_slope_intercept(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a slope-intercept form problem (y = mx + b).

    Args:
        difficulty:
            1 (easy - identify slope and y-intercept from equation)
            2 (medium - write equation from slope and y-intercept)
            3 (hard - write equation from two points)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    if difficulty == 1:
        # Easy: Identify slope and y-intercept from equation
        m = random.randint(-8, 8)
        while m == 0:
            m = random.randint(-8, 8)
        b = random.randint(-12, 12)

        # Format equation
        if m == 1:
            m_str = ""
        elif m == -1:
            m_str = "-"
        else:
            m_str = str(m)

        if b >= 0:
            equation = f"y = {m_str}x + {b}"
        else:
            equation = f"y = {m_str}x - {abs(b)}"

        steps.append(f"Given the equation: ${equation}$")
        steps.append("**Rule:** Slope-intercept form is $y = mx + b$ where:")
        steps.append("- $m$ = slope (coefficient of $x$)")
        steps.append("- $b$ = y-intercept (constant term)")
        steps.append(f"From the equation ${equation}$:")
        steps.append(f"- Slope $m = {m}$")
        steps.append(f"- Y-intercept $b = {b}$")

        answer_str = f"m={m}, b={b}"

    elif difficulty == 2:
        # Medium: Write equation from slope and y-intercept
        # Use fractions for slope sometimes
        if random.choice([True, False]):
            # Integer slope
            m = random.randint(-6, 6)
            while m == 0:
                m = random.randint(-6, 6)
            m_str = str(m)
            m_latex = str(m)
        else:
            # Fraction slope
            numerator = random.randint(-5, 5)
            while numerator == 0:
                numerator = random.randint(-5, 5)
            denominator = random.randint(2, 5)
            m = Fraction(numerator, denominator)
            m_str = f"{m.numerator}/{m.denominator}"
            m_latex = f"\\frac{{{m.numerator}}}{{{m.denominator}}}"

        b = random.randint(-10, 10)

        steps.append(f"Write the equation of a line with slope $m = {m_latex}$ and y-intercept $b = {b}$")
        steps.append("**Rule:** Use slope-intercept form: $y = mx + b$")
        steps.append(f"Substitute $m = {m_latex}$ and $b = {b}$:")

        # Build equation string
        if isinstance(m, Fraction):
            if m == 1:
                eq_m = "x"
            elif m == -1:
                eq_m = "-x"
            else:
                eq_m = f"\\frac{{{m.numerator}}}{{{m.denominator}}}x"
        else:
            if m == 1:
                eq_m = "x"
            elif m == -1:
                eq_m = "-x"
            else:
                eq_m = f"{m}x"

        if b >= 0:
            answer_str = f"y = {eq_m} + {b}"
        else:
            answer_str = f"y = {eq_m} - {abs(b)}"

        steps.append(f"${answer_str}$")

    else:  # difficulty == 3
        # Hard: Write equation from two points
        x1 = random.randint(-8, 8)
        y1 = random.randint(-10, 10)
        x2 = random.randint(-8, 8)
        while x2 == x1:
            x2 = random.randint(-8, 8)
        y2 = random.randint(-10, 10)

        steps.append(f"Write the equation of the line passing through $({x1}, {y1})$ and $({x2}, {y2})$")
        steps.append("**Step 1:** Find the slope using the formula $m = \\frac{{y_2 - y_1}}{{x_2 - x_1}}$")

        delta_y = y2 - y1
        delta_x = x2 - x1
        steps.append(f"$m = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\frac{{{delta_y}}}{{{delta_x}}}$")

        # Simplify slope
        m = Fraction(delta_y, delta_x)
        if m.denominator == 1:
            steps.append(f"Slope: $m = {m.numerator}$")
            m_latex = str(m.numerator)
            m_val = m.numerator
        else:
            steps.append(f"Slope: $m = \\frac{{{m.numerator}}}{{{m.denominator}}}$")
            m_latex = f"\\frac{{{m.numerator}}}{{{m.denominator}}}"
            m_val = m

        steps.append("**Step 2:** Use slope-intercept form $y = mx + b$ with one point to find $b$")
        steps.append(f"Using point $({x1}, {y1})$, substitute $x = {x1}$ and $y = {y1}$:")

        if m.denominator == 1:
            steps.append(f"${y1} = {m.numerator}({x1}) + b$")
            mx_val = m.numerator * x1
        else:
            steps.append(f"${y1} = \\frac{{{m.numerator}}}{{{m.denominator}}}({x1}) + b$")
            mx_val = float(m) * x1

        steps.append(f"${y1} = {mx_val} + b$")
        b = y1 - mx_val
        steps.append(f"$b = {y1} - {mx_val} = {b}$")

        # Check if b is integer
        if b == int(b):
            b = int(b)

        steps.append("**Step 3:** Write the final equation")

        # Build equation
        if m.denominator == 1:
            if m.numerator == 1:
                eq_m = "x"
            elif m.numerator == -1:
                eq_m = "-x"
            else:
                eq_m = f"{m.numerator}x"
        else:
            eq_m = f"\\frac{{{m.numerator}}}{{{m.denominator}}}x"

        if b >= 0:
            if b == int(b):
                answer_str = f"y = {eq_m} + {int(b)}"
            else:
                answer_str = f"y = {eq_m} + {b:.2f}"
        else:
            if b == int(b):
                answer_str = f"y = {eq_m} - {abs(int(b))}"
            else:
                answer_str = f"y = {eq_m} - {abs(b):.2f}"

        steps.append(f"${answer_str}$")

    steps.append(f"**Final Answer:** ${answer_str}$")

    return {
        "question": f"Find the slope-intercept form equation" if difficulty > 1 else f"Identify the slope and y-intercept of ${equation}$",
        "answer": answer_str,
        "steps": steps,
        "difficulty": difficulty,
    }
