"""Linear equation question generator (ax + b = c)."""

import random
from typing import Dict, Any


def generate_linear_equation(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a linear equation problem: ax + b = c

    Args:
        difficulty: 1 (easy), 2 (medium), 3-5 (hard)

    Returns:
        Dict with question, answer, and solution steps
    """
    # Adjust ranges based on difficulty
    if difficulty == 1:
        # Easy: small coefficients, integer solutions
        a = random.randint(2, 5)
        x_solution = random.randint(1, 10)
        b = random.randint(-10, 10)
    elif difficulty == 2:
        # Medium: larger coefficients, still integer solutions
        a = random.randint(2, 10)
        x_solution = random.randint(-10, 10)
        b = random.randint(-20, 20)
    else:
        # Hard: larger coefficients, may have decimal solutions
        a = random.randint(5, 20)
        x_solution = random.choice([i for i in range(-20, 20) if i != 0])
        b = random.randint(-50, 50)

    # Calculate c to ensure known solution
    c = a * x_solution + b

    # Format question with LaTeX
    # Handle signs properly
    sign_b = "+" if b >= 0 else "-"
    abs_b = abs(b)

    if a == 1:
        question = f"x {sign_b} {abs_b} = {c}"
    elif a == -1:
        question = f"-x {sign_b} {abs_b} = {c}"
    else:
        question = f"{a}x {sign_b} {abs_b} = {c}"

    question = question.replace("+ 0", "").replace("- 0", "").strip()

    # Wrap in LaTeX
    latex_question = f"${question}$"

    # Generate solution steps with LaTeX
    steps = []

    # Step 0: Show the original equation
    steps.append(f"Start with the equation: ${question}$")

    # Step 1: Isolate ax
    if b != 0:
        new_c = c - b
        operation = f"subtract ${abs(b)}$" if b > 0 else f"add ${abs(b)}$"
        steps.append(f"To isolate the variable term, {operation} from both sides")

        # Show the new equation
        if a == 1:
            new_eq = f"x = {new_c}"
        elif a == -1:
            new_eq = f"-x = {new_c}"
        else:
            new_eq = f"{a}x = {new_c}"
        steps.append(f"${new_eq}$")
    else:
        new_c = c

    # Step 2: Divide by a
    if a != 1:
        steps.append(f"Divide both sides by ${a}$ to solve for $x$")

        # Show division
        if new_c < 0 and a < 0:
            # Both negative
            steps.append(f"$x = \\frac{{{new_c}}}{{{a}}} = \\frac{{{abs(new_c)}}}{{{abs(a)}}}$")
        else:
            steps.append(f"$x = \\frac{{{new_c}}}{{{a}}}$")

        # Simplify if needed
        if new_c % a == 0:
            steps.append(f"Simplify: $x = {x_solution}$")
        else:
            # Show as decimal
            steps.append(f"Simplify: $x = {new_c/a:.2f}$")
    else:
        # Already solved
        if b != 0:
            steps.append(f"The equation is already solved: $x = {x_solution}$")

    # Final answer
    steps.append(f"**Final Answer:** $x = {x_solution}$")

    return {
        "question": f"Solve for $x$: {latex_question}",
        "answer": str(x_solution),
        "answer_numeric": x_solution,
        "steps": steps,
        "difficulty": difficulty,
    }


def validate_answer(user_answer: str, correct_answer: float, tolerance: float = 0.01) -> bool:
    """Validate user's answer against correct answer."""
    try:
        user_value = float(user_answer)
        return abs(user_value - correct_answer) < tolerance
    except ValueError:
        return False
