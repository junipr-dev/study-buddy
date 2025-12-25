"""Parametric equations question generator."""

import random
from typing import Dict, Any

# Word problem templates for engaging, real-world contexts
PARAMETRIC_WORD_PROBLEMS = [
    {
        "context": "An animation system uses parametric equations to move an object. Time $t$ (in seconds) determines the position.",
        "difficulty": 1,
        "type": "evaluate"
    },
    {
        "context": "A roller coaster's path can be described using parametric equations, where $t$ represents time in seconds.",
        "difficulty": 1,
        "type": "evaluate"
    },
    {
        "context": "A projectile is launched with initial velocity. The parametric equations describe its horizontal and vertical position over time $t$.",
        "difficulty": 1,
        "type": "evaluate"
    },
    {
        "context": "A camera follows a predetermined path in a video game using parametric equations, where $t$ is the animation frame number.",
        "difficulty": 2,
        "type": "eliminate"
    },
    {
        "context": "A satellite follows an elliptical orbit described by parametric equations. The parameter $t$ eliminates to a standard ellipse equation.",
        "difficulty": 2,
        "type": "eliminate"
    },
    {
        "context": "A bouncing ball's trajectory can be modeled with parametric equations. Find the ball's position at a specific time.",
        "difficulty": 3,
        "type": "find_t"
    },
    {
        "context": "A pendulum's swing is tracked with parametric equations. At what time does it reach a specific point?",
        "difficulty": 3,
        "type": "find_t"
    }
]


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
        use_word_problem = random.random() < 0.4

        # Choose whether to ask for x or y
        if random.choice([True, False]):
            # Ask for x
            x_result = a * t_val + b

            if use_word_problem:
                context = random.choice([p for p in PARAMETRIC_WORD_PROBLEMS if p["difficulty"] == 1])
                question = f"{context['context']}\n\n"
                question += f"The parametric equations are $x = {a}t {b:+d}$ and $y = {c}t {d:+d}$.\n\n"
                question += f"Find the value of $x$ when $t = {t_val}$."
            else:
                question = f"Given the parametric equations $x = {a}t {b:+d}$ and $y = {c}t {d:+d}$, find the value of $x$ when $t = {t_val}$."

            steps = [
                f"We have the equation $x = {a}t {b:+d}$",
                "",
                f"To find the position at $t = {t_val}$, substitute this value:",
                f"$x = {a}({t_val}) {b:+d}$",
                f"$x = {a * t_val} {b:+d}$",
                f"$x = {x_result}$",
                "",
                f"**Final Answer:** ${x_result}$ units"
            ]

            answer_numeric = x_result
        else:
            # Ask for y
            y_result = c * t_val + d

            if use_word_problem:
                context = random.choice([p for p in PARAMETRIC_WORD_PROBLEMS if p["difficulty"] == 1])
                question = f"{context['context']}\n\n"
                question += f"The parametric equations are $x = {a}t {b:+d}$ and $y = {c}t {d:+d}$.\n\n"
                question += f"Find the value of $y$ when $t = {t_val}$."
            else:
                question = f"Given the parametric equations $x = {a}t {b:+d}$ and $y = {c}t {d:+d}$, find the value of $y$ when $t = {t_val}$."

            steps = [
                f"We have the equation $y = {c}t {d:+d}$",
                "",
                f"To find the position at $t = {t_val}$, substitute this value:",
                f"$y = {c}({t_val}) {d:+d}$",
                f"$y = {c * t_val} {d:+d}$",
                f"$y = {y_result}$",
                "",
                f"**Final Answer:** ${y_result}$ units"
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
        use_word_problem = random.random() < 0.4

        slope = c / a
        if slope == int(slope):
            slope = int(slope)
            answer_numeric = slope
        else:
            answer_numeric = round(slope, 2)

        if use_word_problem:
            context = random.choice([p for p in PARAMETRIC_WORD_PROBLEMS if p["difficulty"] == 2])
            question = f"{context['context']}\n\n"
            question += f"The parametric equations are $x = {a}t {b:+d}$ and $y = {c}t {d:+d}$.\n\n"
            question += "Eliminate the parameter $t$ to find the slope of the path."
        else:
            question = f"Eliminate the parameter $t$ from the parametric equations $x = {a}t {b:+d}$ and $y = {c}t {d:+d}$ to find the slope of the resulting line."

        steps = [
            "**Step 1:** Solve for $t$ from the $x$ equation:",
            f"$x = {a}t {b:+d}$",
            f"$x {-b:+d} = {a}t$",
            f"$t = \\frac{{x {-b:+d}}}{{{a}}}$",
            "",
            "**Step 2:** Substitute this expression for $t$ into the $y$ equation:",
            f"$y = {c}t {d:+d}$",
            f"$y = {c} \\cdot \\frac{{x {-b:+d}}}{{{a}}} {d:+d}$",
            f"$y = \\frac{{{c}}}{{{a}}}x - \\frac{{{c * b}}}{{{a}}} {d:+d}$",
            "",
            "**Step 3:** Identify the slope from the equation $y = mx + b$:",
            f"The slope is $m = \\frac{{{c}}}{{{a}}}$",
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
        use_word_problem = random.random() < 0.4

        # x = at, y = t²
        x_point = a * t_val
        y_point = t_val ** 2

        if use_word_problem:
            context = random.choice([p for p in PARAMETRIC_WORD_PROBLEMS if p["difficulty"] == 3])
            question = f"{context['context']}\n\n"
            question += f"The parametric equations are $x = {a}t$ and $y = t^2$.\n\n"
            question += f"At what value of $t$ is the object at point $({x_point}, {y_point})$?"
        else:
            question = f"Given the parametric equations $x = {a}t$ and $y = t^2$, find the value of $t$ when the point is $({x_point}, {y_point})$."

        steps = [
            f"We need to find $t$ such that both coordinates match: $x = {x_point}$ and $y = {y_point}$.",
            "",
            "**Method: Use the $x$ equation to solve for $t$**",
            f"$x = {a}t = {x_point}$",
            f"$t = \\frac{{{x_point}}}{{{a}}}$",
            f"$t = {t_val}$",
            "",
            "**Verify with the $y$ equation:**",
            f"$y = t^2 = ({t_val})^2 = {y_point}$ ✓",
            "",
            f"Both equations check out, so the parameter value is correct.",
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
