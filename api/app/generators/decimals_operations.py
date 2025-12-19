"""Decimals operations question generator."""

import random
from typing import Dict, Any, List


def generate_decimals_operations(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a decimals operations problem.

    Args:
        difficulty: 1 (addition/subtraction), 2 (multiplication/division), 3 (mixed operations)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps: List[str] = []

    if difficulty == 1:
        # Simple addition/subtraction
        operation = random.choice(["+", "-"])
        a = round(random.uniform(1, 10), 1)
        b = round(random.uniform(1, 10), 1)

        if operation == "+":
            answer = a + b
            question = f"${a} + {b}$"
            steps.append(f"Calculate: ${a} + {b}$")
            steps.append("Line up the decimal points:")
            steps.append(f"$\\begin{{align*}} {a:.1f} \\\\ + {b:.1f} \\\\ \\hline {answer:.1f} \\end{{align*}}$")
        else:
            # Ensure non-negative result
            if a < b:
                a, b = b, a
            answer = a - b
            question = f"${a} - {b}$"
            steps.append(f"Calculate: ${a} - {b}$")
            steps.append("Line up the decimal points:")
            steps.append(f"$\\begin{{align*}} {a:.1f} \\\\ - {b:.1f} \\\\ \\hline {answer:.1f} \\end{{align*}}$")

    elif difficulty == 2:
        # Multiplication/division
        operation = random.choice(["*", "/"])

        if operation == "*":
            a = round(random.uniform(1, 5), 1)
            b = round(random.uniform(1, 5), 1)
            answer = a * b
            question = f"${a} \\times {b}$"

            steps.append(f"Calculate: ${a} \\times {b}$")
            steps.append("Multiply as if they were whole numbers:")
            a_no_decimal = int(a * 10)
            b_no_decimal = int(b * 10)
            product = a_no_decimal * b_no_decimal
            steps.append(f"${a_no_decimal} \\times {b_no_decimal} = {product}$")
            steps.append("Count decimal places: 1 in each number = 2 total")
            steps.append(f"Place decimal point 2 places from the right: ${answer:.2f}$")
        else:
            # Division - ensure clean result
            divisor = round(random.uniform(1, 5), 1)
            quotient = round(random.uniform(1, 10), 1)
            a = divisor * quotient
            answer = quotient
            question = f"${a:.1f} \\div {divisor}$"

            steps.append(f"Calculate: ${a:.1f} \\div {divisor}$")
            steps.append(f"Move decimal in both numbers one place right:")
            steps.append(f"${int(a * 10)} \\div {int(divisor * 10)}$")
            steps.append(f"Divide: ${int(a * 10)} \\div {int(divisor * 10)} = {answer:.1f}$")

    else:
        # Mixed operations with parentheses
        a = round(random.uniform(1, 5), 1)
        b = round(random.uniform(1, 5), 1)
        c = round(random.uniform(1, 3), 1)

        operation_choice = random.choice(["add_mult", "sub_mult"])

        if operation_choice == "add_mult":
            # (a + b) × c
            sum_ab = a + b
            answer = sum_ab * c
            question = f"$({a} + {b}) \\times {c}$"

            steps.append(f"Calculate: $({a} + {b}) \\times {c}$")
            steps.append("Step 1: Solve inside parentheses first")
            steps.append(f"${a} + {b} = {sum_ab:.1f}$")
            steps.append(f"Step 2: Multiply the result by ${c}$")
            steps.append(f"${sum_ab:.1f} \\times {c} = {answer:.2f}$")
        else:
            # (a - b) × c
            if a < b:
                a, b = b, a
            diff_ab = a - b
            answer = diff_ab * c
            question = f"$({a} - {b}) \\times {c}$"

            steps.append(f"Calculate: $({a} - {b}) \\times {c}$")
            steps.append("Step 1: Solve inside parentheses first")
            steps.append(f"${a} - {b} = {diff_ab:.1f}$")
            steps.append(f"Step 2: Multiply the result by ${c}$")
            steps.append(f"${diff_ab:.1f} \\times {c} = {answer:.2f}$")

    steps.append(f"**Final Answer:** ${answer:.2f}$")

    return {
        "question": f"Calculate: {question}",
        "answer": f"{answer:.2f}",
        "answer_numeric": round(answer, 2),
        "steps": steps,
        "difficulty": difficulty,
    }
