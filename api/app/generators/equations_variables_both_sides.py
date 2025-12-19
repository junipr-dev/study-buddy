"""Equations with variables on both sides generator."""

import random
from typing import Dict, Any, List
from math import gcd


def generate_equations_variables_both_sides(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate equations with variables on both sides.

    Args:
        difficulty: 1 (simple), 2 (with distribution), 3 (complex with fractions)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Simple: ax + b = cx + d
        a = random.randint(2, 6)
        c = random.randint(1, a - 1)  # Ensure a > c for positive coefficient
        x_solution = random.randint(1, 10)
        b = random.randint(-10, 10)
        d = (a - c) * x_solution + b

        # Format equation
        question = f"{a}x {'+' if b >= 0 else '-'} {abs(b)} = {c}x {'+' if d >= 0 else '-'} {abs(d)}"

        steps = [
            f"Start with: ${question}$",
            f"Move variable terms to the left by subtracting ${c}x$ from both sides",
            f"${a}x - {c}x {'+' if b >= 0 else '-'} {abs(b)} = {abs(d) if d >= 0 else f'({d})'}$",
            f"${a - c}x {'+' if b >= 0 else '-'} {abs(b)} = {d}$",
        ]

        if b != 0:
            operation = f"subtract ${abs(b)}$" if b > 0 else f"add ${abs(b)}$"
            steps.append(f"{operation.capitalize()} from both sides")
            steps.append(f"${a - c}x = {d - b}$")

        steps.append(f"Divide both sides by ${a - c}$")
        steps.append(f"$x = \\frac{{{d - b}}}{{{a - c}}} = {x_solution}$")
        steps.append(f"**Final Answer:** $x = {x_solution}$")

    elif difficulty == 2:
        # With distribution: a(x + b) = cx + d
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 4)
        x_solution = random.randint(1, 8)

        # Calculate d to ensure solution
        d = a * x_solution + a * b - c * x_solution

        question = f"{a}(x {'+' if b >= 0 else '-'} {abs(b)}) = {c}x {'+' if d >= 0 else '-'} {abs(d)}"

        steps = [
            f"Start with: ${question}$",
            f"Distribute ${a}$ on the left side",
            f"${a} \\cdot x {'+' if b >= 0 else '-'} {a} \\cdot {abs(b)} = {c}x {'+' if d >= 0 else '-'} {abs(d)}$",
            f"${a}x {'+' if a*b >= 0 else '-'} {abs(a*b)} = {c}x {'+' if d >= 0 else '-'} {abs(d)}$",
            f"Subtract ${c}x$ from both sides",
            f"${a - c}x {'+' if a*b >= 0 else '-'} {abs(a*b)} = {d}$",
        ]

        if a * b != 0:
            operation = f"subtract ${abs(a*b)}$" if a*b > 0 else f"add ${abs(a*b)}$"
            steps.append(f"{operation.capitalize()} from both sides")
            steps.append(f"${a - c}x = {d - a*b}$")

        steps.append(f"Divide both sides by ${a - c}$")
        steps.append(f"$x = {x_solution}$")
        steps.append(f"**Final Answer:** $x = {x_solution}$")

    else:  # difficulty == 3
        # Complex with fractions: x/a + b = x/c + d
        # Choose denominators that will give clean solution
        a = random.choice([2, 3, 4, 6])
        c = random.choice([d for d in [2, 3, 4, 6] if d != a])

        # Find LCM to ensure integer solution
        from math import lcm
        common = lcm(a, c)
        x_solution = common * random.randint(1, 5)

        b = random.randint(1, 8)
        d = x_solution // a + b - x_solution // c

        question = f"\\frac{{x}}{{{a}}} {'+' if b >= 0 else '-'} {abs(b)} = \\frac{{x}}{{{c}}} {'+' if d >= 0 else '-'} {abs(d)}"

        steps = [
            f"Start with: ${question}$",
            f"Multiply everything by ${common}$ (LCM of ${a}$ and ${c}$) to clear fractions",
            f"${common} \\cdot \\frac{{x}}{{{a}}} {'+' if b >= 0 else '-'} {common} \\cdot {abs(b)} = {common} \\cdot \\frac{{x}}{{{c}}} {'+' if d >= 0 else '-'} {common} \\cdot {abs(d)}$",
            f"${common//a}x {'+' if b >= 0 else '-'} {abs(common*b)} = {common//c}x {'+' if d >= 0 else '-'} {abs(common*d)}$",
            f"Subtract ${common//c}x$ from both sides",
            f"${common//a - common//c}x {'+' if b >= 0 else '-'} {abs(common*b)} = {common*d if d >= 0 else f'({common*d})'}$",
        ]

        if b != 0:
            operation = f"subtract ${abs(common*b)}$" if b > 0 else f"add ${abs(common*b)}$"
            steps.append(f"{operation.capitalize()} from both sides")
            steps.append(f"${common//a - common//c}x = {common*d - common*b}$")

        steps.append(f"Divide both sides by ${common//a - common//c}$")
        steps.append(f"$x = {x_solution}$")
        steps.append(f"**Final Answer:** $x = {x_solution}$")

    return {
        "question": f"Solve for $x$: ${question}$",
        "answer": str(x_solution),
        "answer_numeric": x_solution,
        "steps": steps,
        "difficulty": difficulty,
    }
