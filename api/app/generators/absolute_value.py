"""Absolute value question generator."""

import random
from typing import Dict, Any


def generate_absolute_value(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate an absolute value problem.

    Args:
        difficulty:
            1 (easy - simple absolute value of a number)
            2 (medium - absolute value with operations)
            3 (hard - absolute value equations)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    if difficulty == 1:
        # Easy: Simple absolute value
        num = random.randint(-50, 50)

        expression = f"|{num}|"
        steps.append(f"Find the absolute value: ${expression}$")
        steps.append("**Rule:** Absolute value is the distance from zero (always non-negative)")

        if num >= 0:
            steps.append(f"Since ${num}$ is positive, $|{num}| = {num}$")
            answer = num
        else:
            steps.append(f"Since ${num}$ is negative, $|{num}| = {abs(num)}$")
            steps.append(f"The absolute value removes the negative sign: ${abs(num)}$")
            answer = abs(num)

    elif difficulty == 2:
        # Medium: Absolute value with operations inside
        # Format: |a + b| or |a - b| or |a * b|
        operation = random.choice(['add', 'subtract', 'multiply'])

        if operation == 'add':
            a = random.randint(-15, 15)
            b = random.randint(-15, 15)
            expression = f"|{a} + {b}|"

            steps.append(f"Evaluate: ${expression}$")
            steps.append("**Rule:** First calculate inside the absolute value, then take absolute value")
            steps.append(f"**Step 1:** Calculate inside: ${a} + {b} = {a + b}$")

            result = a + b
            steps.append(f"**Step 2:** Take absolute value: $|{result}| = {abs(result)}$")
            answer = abs(result)

        elif operation == 'subtract':
            a = random.randint(-12, 12)
            b = random.randint(-12, 12)
            expression = f"|{a} - {b}|"

            steps.append(f"Evaluate: ${expression}$")
            steps.append("**Rule:** First calculate inside the absolute value, then take absolute value")
            steps.append(f"**Step 1:** Calculate inside: ${a} - {b} = {a - b}$")

            result = a - b
            steps.append(f"**Step 2:** Take absolute value: $|{result}| = {abs(result)}$")
            answer = abs(result)

        else:  # multiply
            a = random.randint(-8, 8)
            while a == 0:
                a = random.randint(-8, 8)
            b = random.randint(-6, 6)
            while b == 0:
                b = random.randint(-6, 6)
            expression = f"|{a} \\times {b}|"

            steps.append(f"Evaluate: ${expression}$")
            steps.append("**Rule:** First calculate inside the absolute value, then take absolute value")
            steps.append(f"**Step 1:** Multiply inside: ${a} \\times {b} = {a * b}$")

            result = a * b
            steps.append(f"**Step 2:** Take absolute value: $|{result}| = {abs(result)}$")
            answer = abs(result)

    else:  # difficulty == 3
        # Hard: Absolute value equation |x + a| = b
        a = random.randint(-10, 10)
        b = random.randint(1, 15)  # Always positive for valid solutions

        if a >= 0:
            expression = f"|x + {a}| = {b}"
        else:
            expression = f"|x - {abs(a)}| = {b}"

        steps.append(f"Solve the equation: ${expression}$")
        steps.append("**Rule:** Absolute value equation $|X| = b$ has two solutions: $X = b$ or $X = -b$")

        if a >= 0:
            steps.append(f"This means: $x + {a} = {b}$ or $x + {a} = -{b}$")

            steps.append(f"**Case 1:** $x + {a} = {b}$")
            sol1 = b - a
            steps.append(f"$x = {b} - {a} = {sol1}$")

            steps.append(f"**Case 2:** $x + {a} = -{b}$")
            sol2 = -b - a
            steps.append(f"$x = -{b} - {a} = {sol2}$")
        else:
            steps.append(f"This means: $x - {abs(a)} = {b}$ or $x - {abs(a)} = -{b}$")

            steps.append(f"**Case 1:** $x - {abs(a)} = {b}$")
            sol1 = b + abs(a)
            steps.append(f"$x = {b} + {abs(a)} = {sol1}$")

            steps.append(f"**Case 2:** $x - {abs(a)} = -{b}$")
            sol2 = -b + abs(a)
            steps.append(f"$x = -{b} + {abs(a)} = {sol2}$")

        steps.append(f"**Verification:** Check both solutions in the original equation")
        answer_str = f"{sol1}, {sol2}" if sol1 < sol2 else f"{sol2}, {sol1}"
        steps.append(f"The solutions are: $x = {sol1}$ and $x = {sol2}$")

        steps.append(f"**Final Answer:** $x = {answer_str}$")

        return {
            "question": f"Solve: ${expression}$",
            "answer": answer_str,
            "steps": steps,
            "difficulty": difficulty,
        }

    steps.append(f"**Final Answer:** ${answer}$")

    return {
        "question": f"Evaluate: ${expression}$",
        "answer": str(answer),
        "answer_numeric": answer,
        "steps": steps,
        "difficulty": difficulty,
    }
