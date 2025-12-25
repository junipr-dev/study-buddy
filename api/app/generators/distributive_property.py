"""Distributive property question generator with real-world contexts."""

import random
from typing import Dict, Any

# Real-world contexts for distributive property
DISTRIBUTIVE_CONTEXTS = [
    {"template": "A group of {a} friends each buy a drink (${b}) and a snack (${c}). What's the total cost?", "format": "{a}({b} + {c})"},
    {"template": "You buy {a} gift bags. Each bag contains a toy worth ${b} and candy worth ${c}. What's the total?", "format": "{a}({b} + {c})"},
    {"template": "A classroom has {a} rows of desks. Each row has {b} students plus {c} empty chairs. How many spots total?", "format": "{a}({b} + {c})"},
]

# Mental math tip contexts
MENTAL_MATH_CONTEXTS = [
    {"expression": "{a}({b} + {c})", "tip": "Mental math trick: Instead of multiplying {a} × {total}, break it into {a} × {b} + {a} × {c}"},
]


def generate_distributive_property(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a distributive property problem: a(b + c) = ab + ac.

    Args:
        difficulty:
            1 (easy - simple positive integers)
            2 (medium - includes negative numbers)
            3 (hard - variables and multiple terms)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []
    use_context = random.random() < 0.4

    if difficulty == 1:
        # Easy: a(b + c) with positive integers
        a = random.randint(2, 9)
        b = random.randint(1, 10)
        c = random.randint(1, 10)

        expression = f"{a}({b} + {c})"

        if use_context:
            ctx = random.choice(DISTRIBUTIVE_CONTEXTS)
            question = ctx["template"].format(a=a, b=b, c=c)
            steps.append(f"**Problem:** {question}")
            steps.append(f"**Expression:** ${expression}$")
        else:
            steps.append(f"Start with the expression: ${a}({b} + {c})$")

        steps.append("**Rule:** Distribute the outside term to each term inside the parentheses")
        steps.append(f"Multiply ${a}$ by each term inside: ${a} \\times {b}$ and ${a} \\times {c}$")

        term1 = a * b
        term2 = a * c
        steps.append(f"${a} \\times {b} = {term1}$")
        steps.append(f"${a} \\times {c} = {term2}$")
        steps.append(f"Combine: ${term1} + {term2}$")

        answer = term1 + term2
        steps.append(f"Add the results: ${term1} + {term2} = {answer}$")

    elif difficulty == 2:
        # Medium: Include negative numbers and subtraction
        a = random.randint(-8, -2) if random.choice([True, False]) else random.randint(2, 8)
        b = random.randint(1, 12)
        c = random.randint(1, 12)

        # Randomly choose addition or subtraction inside
        if random.choice([True, False]):
            # Subtraction
            expression = f"{a}({b} - {c})"
            steps.append(f"Start with the expression: ${a}({b} - {c})$")
            steps.append("**Rule:** Distribute the outside term to each term inside the parentheses")
            steps.append(f"Distribute ${a}$ to both ${b}$ and ${-c}$ (note the negative sign)")

            term1 = a * b
            term2 = a * (-c)
            steps.append(f"${a} \\times {b} = {term1}$")
            steps.append(f"${a} \\times ({-c}) = {term2}$")

            sign = "+" if term2 >= 0 else "-"
            abs_term2 = abs(term2)
            steps.append(f"Combine: ${term1} {sign} {abs_term2}$")

            answer = term1 + term2
            steps.append(f"Simplify: ${answer}$")
        else:
            # Addition with negative a
            expression = f"{a}({b} + {c})"
            steps.append(f"Start with the expression: ${a}({b} + {c})$")
            steps.append("**Rule:** Distribute the outside term to each term inside")
            steps.append(f"Distribute ${a}$ to both ${b}$ and ${c}$")

            term1 = a * b
            term2 = a * c
            steps.append(f"${a} \\times {b} = {term1}$")
            steps.append(f"${a} \\times {c} = {term2}$")

            sign = "+" if term2 >= 0 else "-"
            abs_term2 = abs(term2)
            steps.append(f"Combine: ${term1} {sign} {abs_term2}$")

            answer = term1 + term2
            steps.append(f"Simplify: ${answer}$")

    else:  # difficulty == 3
        # Hard: Variables with coefficients
        a = random.randint(2, 7)
        b_coef = random.randint(1, 6)
        c = random.randint(1, 10)

        # Format: a(bx + c) or a(bx - c)
        use_subtraction = random.choice([True, False])

        if use_subtraction:
            expression = f"{a}({b_coef}x - {c})"
            steps.append(f"Start with the expression: ${a}({b_coef}x - {c})$")
            steps.append("**Rule:** Distribute the outside term to each term inside the parentheses")
            steps.append(f"Distribute ${a}$ to both ${b_coef}x$ and ${-c}$")

            term1_coef = a * b_coef
            term2 = a * (-c)

            steps.append(f"${a} \\times {b_coef}x = {term1_coef}x$")
            steps.append(f"${a} \\times ({-c}) = {term2}$")

            if term2 >= 0:
                answer_str = f"{term1_coef}x + {term2}"
                steps.append(f"Combine: ${term1_coef}x + {term2}$")
            else:
                answer_str = f"{term1_coef}x - {abs(term2)}"
                steps.append(f"Combine: ${term1_coef}x - {abs(term2)}$")
        else:
            expression = f"{a}({b_coef}x + {c})"
            steps.append(f"Start with the expression: ${a}({b_coef}x + {c})$")
            steps.append("**Rule:** Distribute the outside term to each term inside")
            steps.append(f"Distribute ${a}$ to both ${b_coef}x$ and ${c}$")

            term1_coef = a * b_coef
            term2 = a * c

            steps.append(f"${a} \\times {b_coef}x = {term1_coef}x$")
            steps.append(f"${a} \\times {c} = {term2}$")

            answer_str = f"{term1_coef}x + {term2}"
            steps.append(f"Combine: ${term1_coef}x + {term2}$")

        answer = answer_str
        steps.append(f"**Final Answer:** ${answer_str}$")

        return {
            "question": f"Apply the distributive property: ${expression}$",
            "answer": answer_str,
            "steps": steps,
            "difficulty": difficulty,
        }

    steps.append(f"**Final Answer:** ${answer}$")

    return {
        "question": f"Apply the distributive property: ${expression}$",
        "answer": str(answer),
        "answer_numeric": answer,
        "steps": steps,
        "difficulty": difficulty,
    }
