"""Polynomial long division question generator."""

import random
from typing import Dict, Any, List, Tuple

# Contextual word problems for polynomial division
POLYNOMIAL_DIVISION_CONTEXTS = [
    {
        "setup": "Rate of water flow: dividing a polynomial volume by time gives flow rate.",
        "domain": "engineering"
    },
    {
        "setup": "Breaking down cost functions: total cost divided by units gives unit cost.",
        "domain": "finance"
    },
    {
        "setup": "Mechanical efficiency: power output divided by power input efficiency.",
        "domain": "physics"
    },
    {
        "setup": "Data compression: total data size divided by compression factor.",
        "domain": "technology"
    },
]


def generate_polynomial_long_division(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a polynomial long division problem.

    Args:
        difficulty: 1 (divide by linear), 2 (with remainder), 3 (divide by quadratic)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Divide quadratic by linear, no remainder
        # (x + a)(x + b) = x² + (a+b)x + ab
        a = random.randint(1, 4)
        b = random.randint(1, 4)

        # Dividend: x² + (a+b)x + ab
        # Divisor: x + a
        # Quotient: x + b

        coef_x = a + b
        constant = a * b

        dividend_str = f"x^2 {coef_x:+d}x {constant:+d}"
        divisor_str = f"x {a:+d}"
        quotient_str = f"x {b:+d}"

        question = f"Divide using polynomial long division: $\\frac{{{dividend_str}}}{{{divisor_str}}}$. What is the coefficient of the constant term in the quotient?"

        steps = [
            f"Divide ${dividend_str}$ by ${divisor_str}$ using long division.",
            "",
            "**Step 1:** Divide the leading terms:",
            f"$\\frac{{x^2}}{{x}} = x$",
            "",
            f"**Step 2:** Multiply $x$ by ${divisor_str}$:",
            f"$x \\cdot ({divisor_str}) = x^2 {a:+d}x$",
            "",
            "**Step 3:** Subtract from the dividend:",
            f"$(x^2 {coef_x:+d}x {constant:+d}) - (x^2 {a:+d}x) = {b}x {constant:+d}$",
            "",
            "**Step 4:** Divide the new leading terms:",
            f"$\\frac{{{b}x}}{{x}} = {b}$",
            "",
            f"**Step 5:** Multiply ${b}$ by ${divisor_str}$:",
            f"${b} \\cdot ({divisor_str}) = {b}x {a*b:+d}$",
            "",
            "**Step 6:** Subtract:",
            f"$({b}x {constant:+d}) - ({b}x {a*b:+d}) = 0$",
            "",
            f"The quotient is ${quotient_str}$ with remainder $0$.",
            "",
            f"**Final Answer:** ${b}$"
        ]

        answer_numeric = b

    elif difficulty == 2:
        # Medium: Division with remainder
        # Create (x + a)(x + b) + r where r is a small remainder
        a = random.randint(1, 3)
        b = random.randint(1, 4)
        r = random.randint(1, 5)

        # Dividend: x² + (a+b)x + ab + r
        coef_x = a + b
        constant = a * b + r

        dividend_str = f"x^2 {coef_x:+d}x {constant:+d}"
        divisor_str = f"x {a:+d}"
        quotient_str = f"x {b:+d}"

        question = f"Divide using polynomial long division: $\\frac{{{dividend_str}}}{{{divisor_str}}}$. What is the remainder?"

        steps = [
            f"Divide ${dividend_str}$ by ${divisor_str}$ using long division.",
            "",
            "**Step 1:** Divide the leading terms:",
            f"$\\frac{{x^2}}{{x}} = x$",
            "",
            f"**Step 2:** Multiply and subtract:",
            f"$x \\cdot ({divisor_str}) = x^2 {a:+d}x$",
            f"$(x^2 {coef_x:+d}x {constant:+d}) - (x^2 {a:+d}x) = {b}x {constant:+d}$",
            "",
            "**Step 3:** Divide the new leading terms:",
            f"$\\frac{{{b}x}}{{x}} = {b}$",
            "",
            f"**Step 4:** Multiply and subtract:",
            f"${b} \\cdot ({divisor_str}) = {b}x {a*b:+d}$",
            f"$({b}x {constant:+d}) - ({b}x {a*b:+d}) = {r}$",
            "",
            f"The quotient is ${quotient_str}$ with remainder ${r}$.",
            "",
            f"**Final Answer:** ${r}$"
        ]

        answer_numeric = r

    else:
        # Hard: Divide cubic by linear
        # (x² + bx + c)(x + a) = x³ + ax² + bx² + abx + cx + ac
        #                      = x³ + (a+b)x² + (ab+c)x + ac
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = random.randint(1, 4)

        coef_x2 = a + b
        coef_x = a * b + c
        constant = a * c

        dividend_str = f"x^3 {coef_x2:+d}x^2 {coef_x:+d}x {constant:+d}"
        divisor_str = f"x {a:+d}"
        quotient_str = f"x^2 {b:+d}x {c:+d}"

        question = f"Divide using polynomial long division: $\\frac{{{dividend_str}}}{{{divisor_str}}}$. What is the coefficient of $x$ in the quotient?"

        steps = [
            f"Divide ${dividend_str}$ by ${divisor_str}$ using long division.",
            "",
            "**Step 1:** Divide leading terms: $\\frac{{x^3}}{{x}} = x^2$",
            f"Multiply and subtract: $x^2 \\cdot ({divisor_str}) = x^3 {a:+d}x^2$",
            f"Remainder: ${b}x^2 {coef_x:+d}x {constant:+d}$",
            "",
            "**Step 2:** Divide leading terms: $\\frac{{{b}x^2}}{{x}} = {b}x$",
            f"Multiply and subtract: ${b}x \\cdot ({divisor_str}) = {b}x^2 {a*b:+d}x$",
            f"Remainder: ${c}x {constant:+d}$",
            "",
            "**Step 3:** Divide leading terms: $\\frac{{{c}x}}{{x}} = {c}$",
            f"Multiply and subtract: ${c} \\cdot ({divisor_str}) = {c}x {a*c:+d}$",
            f"Remainder: $0$",
            "",
            f"The quotient is ${quotient_str}$.",
            f"The coefficient of $x$ is ${b}$.",
            "",
            f"**Final Answer:** ${b}$"
        ]

        answer_numeric = b

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
