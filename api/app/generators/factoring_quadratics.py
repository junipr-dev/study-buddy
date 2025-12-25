"""Factoring quadratics question generator."""

import random
from math import gcd
from typing import Dict, Any

# Real-world contexts for factoring quadratics
FACTORING_CONTEXTS = [
    {
        "setup": "A volleyball player's jump height is h(t) = -16t² + 32t. Factor to find when she lands.",
        "domain": "sports"
    },
    {
        "setup": "Revenue from selling x items: R(x) = -2x² + 100x. Factor to find break-even points.",
        "domain": "finance"
    },
    {
        "setup": "Area of a rectangular photo frame with border: A = x² + 10x + 21. Factor to find dimensions.",
        "domain": "geometry"
    },
    {
        "setup": "A water fountain's spray path: h = -x² + 6x + 8. Factor to find where it touches ground.",
        "domain": "physics"
    },
]


def generate_factoring_quadratics(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a quadratic factoring problem.

    Args:
        difficulty:
            1 (easy - simple factoring, a=1)
            2 (medium - leading coefficient ≠ 1)
            3 (hard - difference of squares or complex patterns)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    if difficulty == 1:
        # Easy: x² + bx + c = (x + p)(x + q)
        # Choose two integers p and q
        p = random.randint(-8, 8)
        q = random.randint(-8, 8)

        # Expand to get coefficients
        a = 1
        b = p + q
        c = p * q

        # Format the equation
        equation = _format_quadratic(a, b, c)
        question = f"Factor completely: ${equation}$"

        steps.append(f"Start with: ${equation}$")
        steps.append(f"Find two numbers that multiply to ${c}$ and add to ${b}$")

        # Show the numbers
        steps.append(f"The numbers are ${p}$ and ${q}$ because:")
        steps.append(f"${p} \\times {q} = {c}$ and ${p} + {q} = {b}$")

        # Show factored form
        p_term = _format_binomial_term(p)
        q_term = _format_binomial_term(q)
        answer = f"(x {p_term})(x {q_term})"

        steps.append(f"Write in factored form: ${answer}$")
        steps.append(f"**Final Answer:** ${answer}$")

        answer_str = answer.replace("+ -", "- ").replace("- -", "+ ")

    elif difficulty == 2:
        # Medium: ax² + bx + c with a ≠ 1
        # Use (mx + p)(nx + q) = mnx² + (mq + np)x + pq
        m = random.choice([2, 3, 4])
        n = random.choice([1, 2, 3])
        p = random.randint(-6, 6)
        q = random.randint(-6, 6)

        # Expand
        a = m * n
        b = m * q + n * p
        c = p * q

        # Simplify by GCD if possible
        g = gcd(gcd(abs(a), abs(b)), abs(c))
        if g > 1:
            a, b, c = a // g, b // g, c // g

        equation = _format_quadratic(a, b, c)
        question = f"Factor completely: ${equation}$"

        steps.append(f"Start with: ${equation}$")
        steps.append(f"Find factors of $a \\cdot c = {a} \\times {c} = {a * c}$")
        steps.append(f"that add up to $b = {b}$")

        # Use AC method
        ac = a * c
        # Find two numbers that multiply to ac and add to b
        found = False
        for i in range(-abs(ac) - 1, abs(ac) + 2):
            if i != 0 and ac % i == 0:
                j = ac // i
                if i + j == b:
                    steps.append(f"The numbers are ${i}$ and ${j}$")
                    steps.append(f"${i} \\times {j} = {ac}$ and ${i} + {j} = {b}$")

                    # Rewrite middle term
                    steps.append(f"Rewrite the middle term:")
                    middle_term = _format_split_middle(a, i, j, c)
                    steps.append(f"${middle_term}$")

                    steps.append("Factor by grouping:")

                    # For simplicity in the answer, use trial factoring
                    # Reconstruct the original factors
                    found = True
                    break

        if not found:
            # Fallback to showing the factored form directly
            steps.append("Using factoring techniques:")

        # Calculate the factored form
        # Try to find the actual factors
        m_term = _format_factor_term(m, p)
        n_term = _format_factor_term(n, q)
        answer = f"({m_term})({n_term})"

        steps.append(f"Factored form: ${answer}$")
        steps.append(f"**Final Answer:** ${answer}$")

        answer_str = answer.replace("+ -", "- ").replace("- -", "+ ")

    else:  # difficulty == 3
        # Hard: Special patterns (difference of squares, perfect square trinomials)
        pattern = random.choice(["difference_of_squares", "perfect_square"])

        if pattern == "difference_of_squares":
            # a² - b² = (a + b)(a - b)
            # Choose coefficient for x² and constant
            a_coef = random.choice([1, 4, 9, 16, 25])  # Perfect squares
            c_coef = random.choice([1, 4, 9, 16, 25, 36, 49])

            a = a_coef
            b = 0
            c = -c_coef

            equation = _format_quadratic(a, b, c)
            question = f"Factor completely: ${equation}$"

            steps.append(f"Start with: ${equation}$")
            steps.append("This is a difference of squares: $a^2 - b^2 = (a + b)(a - b)$")

            # Find square roots
            import math
            sqrt_a = int(math.sqrt(a_coef))
            sqrt_c = int(math.sqrt(c_coef))

            if a == 1:
                a_term = "x"
            else:
                a_term = f"{sqrt_a}x"

            steps.append(f"Identify: $a = {a_term}$ and $b = {sqrt_c}$")

            answer = f"({a_term} + {sqrt_c})({a_term} - {sqrt_c})"
            steps.append(f"Apply the formula: ${answer}$")
            steps.append(f"**Final Answer:** ${answer}$")

            answer_str = answer

        else:  # perfect_square
            # (x + a)² = x² + 2ax + a²
            p = random.randint(2, 10)
            sign = random.choice([1, -1])
            p = p * sign

            a = 1
            b = 2 * p
            c = p * p

            equation = _format_quadratic(a, b, c)
            question = f"Factor completely: ${equation}$"

            steps.append(f"Start with: ${equation}$")
            steps.append("Check if this is a perfect square trinomial")
            steps.append(f"Is ${c}$ a perfect square? Yes, $\\sqrt{{{c}}} = {abs(p)}$")
            steps.append(f"Is ${b}$ equal to $2 \\times {abs(p)}$? Yes, ${b} = {2 * abs(p)}$")

            p_term = _format_binomial_term(p)
            answer = f"(x {p_term})^2"

            steps.append(f"This is a perfect square: ${answer}$")
            steps.append(f"**Final Answer:** ${answer}$")

            answer_str = answer.replace("+ -", "- ")

    return {
        "question": question,
        "answer": answer_str,
        "steps": steps,
        "difficulty": difficulty,
    }


def _format_quadratic(a: int, b: int, c: int) -> str:
    """Format quadratic expression as LaTeX string."""
    terms = []

    # x² term
    if a == 1:
        terms.append("x^2")
    elif a == -1:
        terms.append("-x^2")
    else:
        terms.append(f"{a}x^2")

    # x term
    if b != 0:
        if b == 1:
            terms.append("+ x")
        elif b == -1:
            terms.append("- x")
        elif b > 0:
            terms.append(f"+ {b}x")
        else:
            terms.append(f"- {abs(b)}x")

    # constant term
    if c != 0:
        if c > 0:
            terms.append(f"+ {c}")
        else:
            terms.append(f"- {abs(c)}")

    equation = " ".join(terms)
    return equation


def _format_binomial_term(value: int) -> str:
    """Format a term in a binomial (x + value)."""
    if value >= 0:
        return f"+ {value}"
    else:
        return f"- {abs(value)}"


def _format_factor_term(coef: int, const: int) -> str:
    """Format a factor term like 2x + 3."""
    if coef == 1:
        x_part = "x"
    elif coef == -1:
        x_part = "-x"
    else:
        x_part = f"{coef}x"

    if const == 0:
        return x_part
    elif const > 0:
        return f"{x_part} + {const}"
    else:
        return f"{x_part} - {abs(const)}"


def _format_split_middle(a: int, m: int, n: int, c: int) -> str:
    """Format the expression after splitting the middle term."""
    terms = []

    if a == 1:
        terms.append("x^2")
    else:
        terms.append(f"{a}x^2")

    if m > 0:
        terms.append(f"+ {m}x")
    else:
        terms.append(f"- {abs(m)}x")

    if n > 0:
        terms.append(f"+ {n}x")
    else:
        terms.append(f"- {abs(n)}x")

    if c > 0:
        terms.append(f"+ {c}")
    else:
        terms.append(f"- {abs(c)}")

    return " ".join(terms)
