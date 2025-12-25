"""Exponent rules question generator with scientific contexts."""

import random
from typing import Dict, Any
from math import gcd

# Scientific/computing contexts for exponents
EXPONENT_CONTEXTS = {
    "product": [
        "Bacteria double every hour. If you start with $x^{a}$ bacteria and wait for them to multiply by $x^{b}$, how many do you have?",
        "A computer processes $x^{a}$ operations per second. If speed increases by factor $x^{b}$, what's the new rate?",
    ],
    "quotient": [
        "A file is $x^{a}$ bytes. After compression by factor $x^{b}$, how large is it?",
        "A population of $x^{a}$ cells divides by $x^{b}$ groups. How many per group?",
    ],
    "power": [
        "If a quantity triples (grows by $x^{a}$) and this happens {b} times, what's the total growth?",
        "Each level of a video game requires $(x^{a})^{b}$ experience points. Simplify this.",
    ],
}


def generate_exponent_rules(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate an exponent rules problem.

    Args:
        difficulty:
            1 (easy - product rule: x^a * x^b)
            2 (medium - quotient rule: x^a / x^b or power rule: (x^a)^b)
            3 (hard - combinations of rules)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    if difficulty == 1:
        # Easy: Product rule x^a * x^b = x^(a+b)
        a = random.randint(2, 8)
        b = random.randint(2, 7)
        base = random.choice(['x', 'y', 'a', 'b', 'm', 'n'])

        expression = f"{base}^{a} \\cdot {base}^{b}"
        steps.append(f"Simplify the expression: ${expression}$")
        steps.append("**Rule:** Product Rule - When multiplying powers with the same base, add the exponents")
        steps.append(f"${base}^a \\cdot {base}^b = {base}^{{a+b}}$")
        steps.append(f"Add the exponents: ${a} + {b} = {a + b}$")

        result_exp = a + b
        answer_str = f"{base}^{result_exp}"
        steps.append(f"Result: ${answer_str}$")

    elif difficulty == 2:
        # Medium: Quotient rule or power rule
        base = random.choice(['x', 'y', 'a', 'b'])

        if random.choice([True, False]):
            # Quotient rule: x^a / x^b = x^(a-b)
            a = random.randint(5, 12)
            b = random.randint(2, min(a-1, 8))  # Ensure a > b for positive result

            expression = f"\\frac{{{base}^{a}}}{{{base}^{b}}}"
            steps.append(f"Simplify the expression: ${expression}$")
            steps.append("**Rule:** Quotient Rule - When dividing powers with the same base, subtract the exponents")
            steps.append(f"$\\frac{{{base}^a}}{{{base}^b}} = {base}^{{a-b}}$")
            steps.append(f"Subtract the exponents: ${a} - {b} = {a - b}$")

            result_exp = a - b
            answer_str = f"{base}^{result_exp}"
            steps.append(f"Result: ${answer_str}$")
        else:
            # Power rule: (x^a)^b = x^(a*b)
            a = random.randint(2, 6)
            b = random.randint(2, 5)

            expression = f"({base}^{a})^{b}"
            steps.append(f"Simplify the expression: ${expression}$")
            steps.append("**Rule:** Power Rule - When raising a power to a power, multiply the exponents")
            steps.append(f"$({base}^a)^b = {base}^{{a \\cdot b}}$")
            steps.append(f"Multiply the exponents: ${a} \\times {b} = {a * b}$")

            result_exp = a * b
            answer_str = f"{base}^{result_exp}"
            steps.append(f"Result: ${answer_str}$")

    else:  # difficulty == 3
        # Hard: Combination of rules
        base = random.choice(['x', 'y', 'a'])

        choice = random.randint(1, 3)

        if choice == 1:
            # (x^a * x^b) / x^c
            a = random.randint(3, 7)
            b = random.randint(2, 6)
            c = random.randint(2, 5)

            expression = f"\\frac{{{base}^{a} \\cdot {base}^{b}}}{{{base}^{c}}}"
            steps.append(f"Simplify the expression: ${expression}$")
            steps.append("**Step 1:** Apply the Product Rule to the numerator")
            steps.append(f"${base}^{a} \\cdot {base}^{b} = {base}^{{a+b}} = {base}^{{{a+b}}}$")

            numerator_exp = a + b
            steps.append(f"Expression becomes: $\\frac{{{base}^{{{numerator_exp}}}}}{{{base}^{c}}}$")

            steps.append("**Step 2:** Apply the Quotient Rule")
            steps.append(f"$\\frac{{{base}^{{{numerator_exp}}}}}{{{base}^{c}}} = {base}^{{{numerator_exp}-{c}}}$")

            result_exp = numerator_exp - c
            steps.append(f"Subtract the exponents: ${numerator_exp} - {c} = {result_exp}$")
            answer_str = f"{base}^{result_exp}"

        elif choice == 2:
            # (x^a)^b * x^c
            a = random.randint(2, 5)
            b = random.randint(2, 4)
            c = random.randint(2, 6)

            expression = f"({base}^{a})^{b} \\cdot {base}^{c}"
            steps.append(f"Simplify the expression: ${expression}$")
            steps.append("**Step 1:** Apply the Power Rule to the first term")
            steps.append(f"$({base}^{a})^{b} = {base}^{{a \\cdot b}} = {base}^{{{a*b}}}$")

            first_exp = a * b
            steps.append(f"Expression becomes: ${base}^{{{first_exp}}} \\cdot {base}^{c}$")

            steps.append("**Step 2:** Apply the Product Rule")
            steps.append(f"${base}^{{{first_exp}}} \\cdot {base}^{c} = {base}^{{{first_exp}+{c}}}$")

            result_exp = first_exp + c
            steps.append(f"Add the exponents: ${first_exp} + {c} = {result_exp}$")
            answer_str = f"{base}^{result_exp}"

        else:
            # (x^a / x^b)^c
            a = random.randint(6, 10)
            b = random.randint(2, 5)
            c = random.randint(2, 4)

            expression = f"\\left(\\frac{{{base}^{a}}}{{{base}^{b}}}\\right)^{c}"
            steps.append(f"Simplify the expression: ${expression}$")
            steps.append("**Step 1:** Apply the Quotient Rule inside the parentheses")
            steps.append(f"$\\frac{{{base}^{a}}}{{{base}^{b}}} = {base}^{{a-b}} = {base}^{{{a-b}}}$")

            inner_exp = a - b
            steps.append(f"Expression becomes: $({base}^{{{inner_exp}}})^{c}$")

            steps.append("**Step 2:** Apply the Power Rule")
            steps.append(f"$({base}^{{{inner_exp}}})^{c} = {base}^{{{inner_exp} \\cdot {c}}}$")

            result_exp = inner_exp * c
            steps.append(f"Multiply the exponents: ${inner_exp} \\times {c} = {result_exp}$")
            answer_str = f"{base}^{result_exp}"

        steps.append(f"Result: ${answer_str}$")

    steps.append(f"**Final Answer:** ${answer_str}$")

    return {
        "question": f"Simplify: ${expression}$",
        "answer": answer_str,
        "steps": steps,
        "difficulty": difficulty,
    }
