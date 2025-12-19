"""Quadratic equation question generator."""

import random
from math import sqrt, gcd
from typing import Dict, Any, Tuple


def _gcd_pair(a: int, b: int) -> int:
    """Calculate GCD of two numbers."""
    return gcd(abs(a), abs(b))


def _gcd_triple(a: int, b: int, c: int) -> int:
    """Calculate GCD of three numbers."""
    return gcd(_gcd_pair(a, b), abs(c))


def generate_quadratic_equation(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a quadratic equation problem: ax² + bx + c = 0

    Args:
        difficulty:
            1 (easy - simple factoring, integer roots)
            2 (medium - factoring with leading coefficient)
            3 (medium-hard - quadratic formula, two solutions)
            4 (hard - quadratic formula, may have irrational roots)
            5 (very hard - complex/imaginary solutions)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    if difficulty == 1:
        # Easy: Simple factoring (x + p)(x + q) = 0
        # Choose small integer roots
        root1 = random.randint(-5, 5)
        root2 = random.randint(-5, 5)

        # Expand to get coefficients
        # (x - root1)(x - root2) = x² - (root1+root2)x + root1*root2
        a = 1
        b = -(root1 + root2)
        c = root1 * root2

        method = "factoring"

    elif difficulty == 2:
        # Medium: Factoring with leading coefficient
        # (ax + p)(x + q) = 0
        a = random.choice([2, 3, 4])
        root1 = random.randint(-4, 4)
        root2 = random.randint(-4, 4)

        # Expand (x - root1)(ax - a*root2)
        # = ax² - a*root2*x - root1*ax + a*root1*root2
        # = ax² - (a*root2 + a*root1)x + a*root1*root2
        b = -(a * root2 + a * root1)
        c = a * root1 * root2

        method = "factoring"

    elif difficulty == 3:
        # Medium-hard: Quadratic formula, rational roots
        a = random.choice([1, 2, 3])
        # Choose b² - 4ac to be a perfect square for rational roots
        perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
        discriminant = random.choice(perfect_squares)

        b = random.randint(-10, 10)
        # c = (b² - discriminant) / (4a)
        # Ensure c is an integer
        numerator = b * b - discriminant
        if numerator % (4 * a) == 0:
            c = numerator // (4 * a)
        else:
            # Adjust b to make it work
            b = random.choice([-6, -4, -2, 2, 4, 6, 8, 10])
            c = (b * b - discriminant) // (4 * a)

        # Calculate actual roots
        sqrt_discriminant = sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)

        method = "quadratic_formula"

    elif difficulty == 4:
        # Hard: Quadratic formula, may have irrational roots
        a = random.randint(1, 5)
        b = random.randint(-15, 15)
        c = random.randint(-20, 20)

        # Ensure positive discriminant (real roots)
        discriminant = b * b - 4 * a * c
        while discriminant < 0:
            c = random.randint(-20, 20)
            discriminant = b * b - 4 * a * c

        sqrt_discriminant = sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)

        method = "quadratic_formula"

    else:  # difficulty == 5
        # Very hard: Complex/imaginary solutions
        a = random.randint(1, 4)
        b = random.randint(-10, 10)
        c = random.randint(1, 20)

        # Ensure negative discriminant (complex roots)
        discriminant = b * b - 4 * a * c
        while discriminant >= 0:
            c = random.randint(5, 25)
            discriminant = b * b - 4 * a * c

        # Complex roots: (-b ± i√|discriminant|) / 2a
        sqrt_neg_discriminant = sqrt(abs(discriminant))
        real_part = -b / (2 * a)
        imag_part = sqrt_neg_discriminant / (2 * a)

        method = "quadratic_formula_complex"

    # Format the equation
    equation = _format_quadratic(a, b, c)
    question = f"Solve for $x$: ${equation} = 0$"

    steps.append(f"Start with the equation: ${equation} = 0$")

    # Generate solution steps based on method
    if method == "factoring" and difficulty <= 2:
        answer_str = _solve_by_factoring(a, b, c, steps, difficulty)
    elif method == "quadratic_formula_complex":
        answer_str = _solve_complex(a, b, c, discriminant, real_part, imag_part, steps)
    else:
        answer_str = _solve_by_formula(a, b, c, steps, difficulty)

    return {
        "question": question,
        "answer": answer_str,
        "steps": steps,
        "difficulty": difficulty,
    }


def _format_quadratic(a: int, b: int, c: int) -> str:
    """Format quadratic equation as LaTeX string."""
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
    equation = equation.replace("+ -", "- ")

    return equation


def _solve_by_factoring(a: int, b: int, c: int, steps: list, difficulty: int) -> str:
    """Add factoring solution steps."""

    if difficulty == 1:
        # Simple factoring: x² + bx + c = (x + p)(x + q)
        # Find p and q such that p + q = b and p * q = c
        steps.append("Factor the quadratic expression")
        steps.append("Find two numbers that multiply to $c$ and add to $b$")

        # Find the factors
        for p in range(-20, 21):
            q = c // p if p != 0 and c % p == 0 else None
            if q is not None and p + q == b:
                break

        # Format factors
        p_sign = "+" if p >= 0 else "-"
        q_sign = "+" if q >= 0 else "-"
        steps.append(f"$(x {p_sign} {abs(p)})(x {q_sign} {abs(q)}) = 0$")

        # Solutions
        root1 = -p
        root2 = -q

    else:  # difficulty == 2
        # Factoring with leading coefficient
        steps.append("Factor the quadratic expression")
        steps.append(f"Find factors of $a \\cdot c = {a} \\cdot {c} = {a * c}$ that add to $b = {b}$")

        # This is complex - for now, just show the factored form
        # In practice, we'd reverse-engineer from our chosen roots
        steps.append("After factoring (using grouping or trial methods):")

        # For simplicity, calculate roots using quadratic formula
        discriminant = b * b - 4 * a * c
        sqrt_disc = sqrt(discriminant)
        root1 = (-b + sqrt_disc) / (2 * a)
        root2 = (-b - sqrt_disc) / (2 * a)

    steps.append("Set each factor equal to zero and solve:")

    if root1 == int(root1):
        steps.append(f"$x = {int(root1)}$ or $x = {int(root2)}$")
        answer_str = f"{int(root1)}, {int(root2)}" if root1 != root2 else str(int(root1))
        steps.append(f"**Final Answer:** $x = {int(root1)}$ and $x = {int(root2)}$" if root1 != root2 else f"**Final Answer:** $x = {int(root1)}$")
    else:
        steps.append(f"$x = {root1:.2f}$ or $x = {root2:.2f}$")
        answer_str = f"{root1:.2f}, {root2:.2f}" if abs(root1 - root2) > 0.01 else f"{root1:.2f}"
        steps.append(f"**Final Answer:** $x = {root1:.2f}$ and $x = {root2:.2f}$")

    return answer_str


def _solve_by_formula(a: int, b: int, c: int, steps: list, difficulty: int) -> str:
    """Add quadratic formula solution steps."""

    steps.append("Use the quadratic formula: $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$")
    steps.append(f"Identify coefficients: $a = {a}$, $b = {b}$, $c = {c}$")

    # Calculate discriminant
    discriminant = b * b - 4 * a * c
    steps.append(f"Calculate the discriminant: $b^2 - 4ac = {b}^2 - 4({a})({c}) = {discriminant}$")

    if discriminant == 0:
        steps.append("The discriminant is zero, so there is one repeated root")
        root = -b / (2 * a)
        if root == int(root):
            steps.append(f"$x = \\frac{{-{b}}}{{2({a})}} = {int(root)}$")
            steps.append(f"**Final Answer:** $x = {int(root)}$")
            return str(int(root))
        else:
            steps.append(f"$x = \\frac{{-{b}}}{{2({a})}} = {root:.2f}$")
            steps.append(f"**Final Answer:** $x = {root:.2f}$")
            return f"{root:.2f}"

    # Calculate square root of discriminant
    sqrt_disc = sqrt(discriminant)

    # Check if perfect square
    is_perfect_square = sqrt_disc == int(sqrt_disc)

    if is_perfect_square:
        steps.append(f"$\\sqrt{{{discriminant}}} = {int(sqrt_disc)}$")
        steps.append(f"$x = \\frac{{-{b} \\pm {int(sqrt_disc)}}}{{2({a})}}$")

        root1 = (-b + sqrt_disc) / (2 * a)
        root2 = (-b - sqrt_disc) / (2 * a)

        if root1 == int(root1) and root2 == int(root2):
            steps.append(f"$x = \\frac{{-{b} + {int(sqrt_disc)}}}{{{2 * a}}} = {int(root1)}$ or $x = \\frac{{-{b} - {int(sqrt_disc)}}}{{{2 * a}}} = {int(root2)}$")
            steps.append(f"**Final Answer:** $x = {int(root1)}$ and $x = {int(root2)}$")
            return f"{int(root1)}, {int(root2)}"
        else:
            steps.append(f"$x = {root1:.2f}$ or $x = {root2:.2f}$")
            steps.append(f"**Final Answer:** $x = {root1:.2f}$ and $x = {root2:.2f}$")
            return f"{root1:.2f}, {root2:.2f}"
    else:
        # Irrational roots
        steps.append(f"$\\sqrt{{{discriminant}}} \\approx {sqrt_disc:.2f}$")

        root1 = (-b + sqrt_disc) / (2 * a)
        root2 = (-b - sqrt_disc) / (2 * a)

        steps.append(f"$x = \\frac{{-{b} + {sqrt_disc:.2f}}}{{{2 * a}}} \\approx {root1:.2f}$")
        steps.append(f"$x = \\frac{{-{b} - {sqrt_disc:.2f}}}{{{2 * a}}} \\approx {root2:.2f}$")
        steps.append(f"**Final Answer:** $x \\approx {root1:.2f}$ and $x \\approx {root2:.2f}$")

        return f"{root1:.2f}, {root2:.2f}"


def _solve_complex(a: int, b: int, c: int, discriminant: int, real_part: float, imag_part: float, steps: list) -> str:
    """Add complex solution steps."""

    steps.append("Use the quadratic formula: $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$")
    steps.append(f"Identify coefficients: $a = {a}$, $b = {b}$, $c = {c}$")

    steps.append(f"Calculate the discriminant: $b^2 - 4ac = {b}^2 - 4({a})({c}) = {discriminant}$")
    steps.append("The discriminant is negative, so the solutions are complex numbers")

    steps.append(f"$\\sqrt{{{discriminant}}} = \\sqrt{{-{abs(discriminant)}}} = i\\sqrt{{{abs(discriminant)}}}$")

    sqrt_abs_disc = sqrt(abs(discriminant))
    if sqrt_abs_disc == int(sqrt_abs_disc):
        steps.append(f"$x = \\frac{{-{b} \\pm i\\cdot{int(sqrt_abs_disc)}}}{{2({a})}}$")
    else:
        steps.append(f"$x = \\frac{{-{b} \\pm i\\sqrt{{{abs(discriminant)}}}}}{{2({a})}}$")

    # Format complex answer
    if real_part == 0:
        if imag_part == int(imag_part):
            answer_str = f"±{int(imag_part)}i"
            steps.append(f"**Final Answer:** $x = \\pm {int(imag_part)}i$")
        else:
            answer_str = f"±{imag_part:.2f}i"
            steps.append(f"**Final Answer:** $x = \\pm {imag_part:.2f}i$")
    else:
        if real_part == int(real_part) and imag_part == int(imag_part):
            steps.append(f"**Final Answer:** $x = {int(real_part)} \\pm {int(imag_part)}i$")
            answer_str = f"{int(real_part)}±{int(imag_part)}i"
        else:
            steps.append(f"**Final Answer:** $x = {real_part:.2f} \\pm {imag_part:.2f}i$")
            answer_str = f"{real_part:.2f}±{imag_part:.2f}i"

    return answer_str
