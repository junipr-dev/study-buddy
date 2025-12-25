"""Graphing linear equations generator with real-world contexts."""

import random
from typing import Dict, Any, List

# Real-world contexts for graphing linear equations
GRAPHING_CONTEXTS = [
    {"context": "business", "description": "A business's profit equation where x is items sold and y is total profit", "slope_meaning": "profit per item", "intercept_meaning": "fixed costs (negative) or starting capital"},
    {"context": "temperature", "description": "Temperature throughout the day where x is hours and y is temperature", "slope_meaning": "degrees change per hour", "intercept_meaning": "starting temperature"},
    {"context": "savings", "description": "Your savings account where x is months and y is balance", "slope_meaning": "monthly deposit", "intercept_meaning": "initial deposit"},
    {"context": "driving", "description": "Distance traveled where x is hours driving and y is miles from home", "slope_meaning": "speed (mph)", "intercept_meaning": "starting distance from home"},
]


def generate_graphing_linear_equations(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate graphing linear equations problems.

    Args:
        difficulty: 1 (find y-intercept and slope), 2 (provide points), 3 (write equation from description)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Find y-intercept and slope from equation in slope-intercept form
        m = random.randint(-5, 5)
        if m == 0:
            m = 1
        b = random.randint(-8, 8)

        # Create equation
        if m == 1:
            equation = f"y = x {'+' if b >= 0 else '-'} {abs(b)}"
        elif m == -1:
            equation = f"y = -x {'+' if b >= 0 else '-'} {abs(b)}"
        else:
            equation = f"y = {m}x {'+' if b >= 0 else '-'} {abs(b)}"

        if b == 0:
            equation = equation.replace(" + 0", "").replace(" - 0", "")

        question = f"y = {m}x {'+' if b >= 0 else '-'} {abs(b)}" if b != 0 else f"y = {m}x"

        steps = [
            f"Given equation: ${question}$",
            f"This is in slope-intercept form: $y = mx + b$",
            f"Where $m$ is the slope and $b$ is the y-intercept",
            f"**Slope:** $m = {m}$",
            f"**Y-intercept:** $b = {b}$ (point $(0, {b})$)",
            f"To graph:",
            f"1. Plot the y-intercept at $(0, {b})$",
            f"2. From that point, use the slope: rise = ${m}$, run = $1$",
            f"3. Draw a line through the points",
            f"**Final Answer:** Slope = ${m}$, Y-intercept = ${b}$"
        ]

        answer = f"m={m}, b={b}"

    elif difficulty == 2:
        # Provide 2-3 points on the line
        m = random.randint(-4, 4)
        if m == 0:
            m = 2
        b = random.randint(-6, 6)

        # Generate 3 points
        x1 = random.randint(-3, 0)
        x2 = random.randint(1, 3)
        x3 = random.randint(4, 6)

        y1 = m * x1 + b
        y2 = m * x2 + b
        y3 = m * x3 + b

        equation = f"y = {m}x {'+' if b >= 0 else '-'} {abs(b)}" if b != 0 else f"y = {m}x"
        if m == 1:
            equation = f"y = x {'+' if b >= 0 else '-'} {abs(b)}" if b != 0 else "y = x"
        elif m == -1:
            equation = f"y = -x {'+' if b >= 0 else '-'} {abs(b)}" if b != 0 else "y = -x"

        steps = [
            f"Given equation: ${equation}$",
            f"To find points on this line, substitute x-values and solve for y",
            f"**Point 1:** When $x = {x1}$",
            f"$y = {m}({x1}) {'+' if b >= 0 else '-'} {abs(b)} = {m*x1} {'+' if b >= 0 else '-'} {abs(b)} = {y1}$",
            f"Point: $({x1}, {y1})$",
            f"**Point 2:** When $x = {x2}$",
            f"$y = {m}({x2}) {'+' if b >= 0 else '-'} {abs(b)} = {m*x2} {'+' if b >= 0 else '-'} {abs(b)} = {y2}$",
            f"Point: $({x2}, {y2})$",
            f"**Point 3:** When $x = {x3}$",
            f"$y = {m}({x3}) {'+' if b >= 0 else '-'} {abs(b)} = {m*x3} {'+' if b >= 0 else '-'} {abs(b)} = {y3}$",
            f"Point: $({x3}, {y3})$",
            f"**Final Answer:** Points on the line are $({x1}, {y1})$, $({x2}, {y2})$, $({x3}, {y3})$"
        ]

        answer = f"({x1},{y1}), ({x2},{y2}), ({x3},{y3})"

    else:  # difficulty == 3
        # Write equation from description
        m = random.randint(-5, 5)
        if m == 0:
            m = 3
        b = random.randint(-8, 8)

        # Create description
        descriptions = [
            f"a line with slope ${m}$ and y-intercept ${b}$",
            f"a line that crosses the y-axis at ${b}$ and has slope ${m}$",
            f"a line with slope ${m}$ passing through $(0, {b})$"
        ]
        description = random.choice(descriptions)

        equation = f"y = {m}x {'+' if b >= 0 else '-'} {abs(b)}" if b != 0 else f"y = {m}x"
        if m == 1:
            equation = f"y = x {'+' if b >= 0 else '-'} {abs(b)}" if b != 0 else "y = x"
        elif m == -1:
            equation = f"y = -x {'+' if b >= 0 else '-'} {abs(b)}" if b != 0 else "y = -x"

        steps = [
            f"We need to write an equation for {description}",
            f"Use slope-intercept form: $y = mx + b$",
            f"Where $m$ is the slope and $b$ is the y-intercept",
            f"Given:",
            f"- Slope: $m = {m}$",
            f"- Y-intercept: $b = {b}$",
            f"Substitute into the formula:",
            f"${equation}$",
            f"**Final Answer:** ${equation}$"
        ]

        answer = equation

    return {
        "question": f"Graph the linear equation: ${question}$" if difficulty == 1 else
                   (f"Find three points on the line: ${equation}$" if difficulty == 2 else
                    f"Write the equation for {description}"),
        "answer": answer,
        "answer_numeric": None,
        "steps": steps,
        "difficulty": difficulty,
    }
