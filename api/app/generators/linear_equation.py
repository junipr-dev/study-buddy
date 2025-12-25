"""Linear equation question generator (ax + b = c) with word problems."""

import random
from typing import Dict, Any

# Word problem templates for linear equations
LINEAR_EQUATION_WORD_PROBLEMS = [
    {
        "context": "age",
        "template": "In {b} years, Alex will be {c} years old. How old is Alex now?",
        "equation": "x + {b} = {c}",
        "a": 1,
    },
    {
        "context": "money",
        "template": "After saving ${b} per week for {a} weeks, you have ${c}. How much did you start with?",
        "equation": "x + {a}*{b} = {c}",
        "uses_ab": True,
    },
    {
        "context": "perimeter",
        "template": "A rectangle's length is {a} times its width. If the perimeter is {c} units, find the width.",
        "equation": "2w + 2*{a}w = {c}",
        "uses_a": True,
    },
    {
        "context": "tickets",
        "template": "Concert tickets cost ${a} each. With a ${b_abs} {fee_or_discount}, the total is ${c}. How many tickets were bought?",
        "equation": "{a}x + {b} = {c}",
    },
    {
        "context": "temperature",
        "template": "The temperature rose {a} degrees per hour. After starting at {b}°F, it reached {c}°F. How many hours passed?",
        "equation": "{a}x + {b} = {c}",
    },
]


def generate_linear_equation(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a linear equation problem: ax + b = c

    Args:
        difficulty: 1 (easy), 2 (medium), 3-5 (hard)

    Returns:
        Dict with question, answer, and solution steps
    """
    # Use word problems 40% of the time for easier difficulties
    use_word_problem = difficulty <= 2 and random.random() < 0.4

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
        equation = f"x {sign_b} {abs_b} = {c}"
    elif a == -1:
        equation = f"-x {sign_b} {abs_b} = {c}"
    else:
        equation = f"{a}x {sign_b} {abs_b} = {c}"

    equation = equation.replace("+ 0", "").replace("- 0", "").strip()

    # Generate solution steps with LaTeX
    steps = []

    # Word problem version or standard equation
    if use_word_problem and b != 0:
        # Pick a suitable word problem
        if a == 1 and b > 0:
            # Age problem: x + b = c
            question = f"In {b} years, Alex will be {c} years old. How old is Alex now?"
            steps.append(f"**Problem:** {question}")
            steps.append(f"**Set up equation:** Let $x$ = Alex's current age")
            steps.append(f"${equation}$")
        elif b > 0:
            # Temperature problem: ax + b = c
            question = f"The temperature rose {a} degrees per hour. After starting at {b}°F, it reached {c}°F. How many hours passed?"
            steps.append(f"**Problem:** {question}")
            steps.append(f"**Set up equation:** Let $x$ = hours passed")
            steps.append(f"${equation}$")
        else:
            # Ticket problem with discount: ax - b = c
            question = f"Movie tickets cost ${a} each. After a ${abs_b} discount, the total was ${c}. How many tickets were bought?"
            steps.append(f"**Problem:** {question}")
            steps.append(f"**Set up equation:** Let $x$ = number of tickets")
            steps.append(f"${equation}$")
    else:
        question = equation
        steps.append(f"Start with the equation: ${equation}$")

    # Wrap in LaTeX for display
    latex_question = f"${equation}$"

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
