"""Ratios and proportions question generator."""

import random
from typing import Dict, Any, List


def generate_ratios_proportions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a ratios and proportions problem.

    Args:
        difficulty: 1 (simple ratios), 2 (word problems), 3 (complex proportions)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps: List[str] = []

    if difficulty == 1:
        # Simple ratio: a:b = x:d, find x
        a = random.randint(2, 8)
        b = random.randint(2, 8)
        multiplier = random.randint(2, 5)
        d = b * multiplier
        x = a * multiplier

        question = f"If ${a}:{b} = x:{d}$, find $x$"

        steps.append(f"Set up the proportion: $\\frac{{{a}}}{{{b}}} = \\frac{{x}}{{{d}}}$")
        steps.append("Cross multiply:")
        steps.append(f"${a} \\times {d} = {b} \\times x$")
        steps.append(f"${a * d} = {b}x$")
        steps.append(f"Divide both sides by ${b}$:")
        steps.append(f"$x = \\frac{{{a * d}}}{{{b}}} = {x}$")

        answer = x

    elif difficulty == 2:
        # Word problem: recipe scaling
        cups_flour = random.randint(2, 4)
        cups_sugar = random.randint(2, 5)
        new_flour = cups_flour * random.randint(2, 4)
        new_sugar = (new_flour * cups_sugar) // cups_flour

        question = (
            f"A recipe calls for {cups_flour} cups of flour and {cups_sugar} cups of sugar. "
            f"If you use {new_flour} cups of flour, how many cups of sugar do you need?"
        )

        steps.append(f"Set up a proportion:")
        steps.append(f"$\\frac{{\\text{{flour}}}}{{\\text{{sugar}}}} = \\frac{{{cups_flour}}}{{{cups_sugar}}} = \\frac{{{new_flour}}}{{x}}$")
        steps.append("Cross multiply:")
        steps.append(f"${cups_flour} \\times x = {cups_sugar} \\times {new_flour}$")
        steps.append(f"${cups_flour}x = {cups_sugar * new_flour}$")
        steps.append(f"Divide both sides by ${cups_flour}$:")
        steps.append(f"$x = \\frac{{{cups_sugar * new_flour}}}{{{cups_flour}}} = {new_sugar}$ cups of sugar")

        answer = new_sugar

    else:
        # Complex proportion with 3 quantities
        # a:b:c ratio, given total, find each part
        a = random.randint(1, 4)
        b = random.randint(2, 5)
        c = random.randint(2, 6)
        sum_parts = a + b + c
        total = sum_parts * random.randint(3, 8)

        part_a = (total * a) // sum_parts
        part_b = (total * b) // sum_parts
        part_c = (total * c) // sum_parts

        question = (
            f"Three numbers are in the ratio ${a}:{b}:{c}$. "
            f"If their sum is ${total}$, find the largest number."
        )

        steps.append(f"The ratio is ${a}:{b}:{c}$")
        steps.append(f"Let the numbers be ${a}x$, ${b}x$, and ${c}x$")
        steps.append(f"Their sum equals ${total}$:")
        steps.append(f"${a}x + {b}x + {c}x = {total}$")
        steps.append(f"${sum_parts}x = {total}$")
        steps.append(f"$x = \\frac{{{total}}}{{{sum_parts}}} = {total // sum_parts}$")
        steps.append(f"The three numbers are:")
        steps.append(f"${a}x = {a} \\times {total // sum_parts} = {part_a}$")
        steps.append(f"${b}x = {b} \\times {total // sum_parts} = {part_b}$")
        steps.append(f"${c}x = {c} \\times {total // sum_parts} = {part_c}$")
        steps.append(f"The largest number is ${max(part_a, part_b, part_c)}$")

        answer = max(part_a, part_b, part_c)

    steps.append(f"**Final Answer:** ${answer}$")

    return {
        "question": question,
        "answer": str(answer),
        "answer_numeric": answer,
        "steps": steps,
        "difficulty": difficulty,
    }
