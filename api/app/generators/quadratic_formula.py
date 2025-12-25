"""Quadratic formula generator."""

import random
from typing import Dict, Any, List
from math import sqrt, gcd

# Engaging word problems for quadratic formula
QUADRATIC_FORMULA_PROBLEMS = [
    {
        "context": "A drone is launched from ground level at 24 m/s. Its height is h(t) = -4.9t² + 24t.",
        "question": "When does it return to ground level?",
        "domain": "technology"
    },
    {
        "context": "A bridge arch is described by h = -0.1x² + 2x where h is height in meters.",
        "question": "At what horizontal distances is the arch 4 meters high?",
        "domain": "engineering"
    },
    {
        "context": "An animal population follows P(t) = -t² + 8t + 20 (in hundreds).",
        "question": "When will the population reach 32 hundred?",
        "domain": "biology"
    },
    {
        "context": "A video game player's score over time is S(t) = t² - 8t + 15.",
        "question": "At what times is the score zero (reset events)?",
        "domain": "gaming"
    },
]


def generate_quadratic_formula(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate quadratic formula problems: ax² + bx + c = 0.

    Args:
        difficulty: 1 (integer solutions), 2 (requires simplification), 3 (irrational solutions)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Integer solutions - create from factored form
        # (x - p)(x - q) = 0 where p, q are integers
        p = random.randint(-6, 6)
        q = random.randint(-6, 6)

        # Expand: x² - (p+q)x + pq = 0
        a = 1
        b = -(p + q)
        c = p * q

        # Format equation
        equation = f"x^2"
        if b != 0:
            equation += f" {'+' if b >= 0 else '-'} {abs(b)}x"
        if c != 0:
            equation += f" {'+' if c >= 0 else '-'} {abs(c)}"
        equation += " = 0"

        # Discriminant
        discriminant = b * b - 4 * a * c

        steps = [
            f"Given: ${equation}$",
            f"Use the quadratic formula: $x = \\frac{{-b \\pm \\sqrt{{b^2 - 4ac}}}}{{2a}}$",
            f"Identify: $a = {a}$, $b = {b}$, $c = {c}$",
            f"Calculate the discriminant: $b^2 - 4ac$",
            f"$({b})^2 - 4({a})({c}) = {b*b} - {4*a*c} = {discriminant}$",
            f"Substitute into the formula:",
            f"$x = \\frac{{-({b}) \\pm \\sqrt{{{discriminant}}}}}{{2({a})}}$",
            f"$x = \\frac{{{-b} \\pm {int(sqrt(discriminant))}}}{{2}}$",
            f"**Solution 1:** $x = \\frac{{{-b} + {int(sqrt(discriminant))}}}{{2}} = \\frac{{{-b + int(sqrt(discriminant))}}}{{2}} = {(-b + int(sqrt(discriminant))) // 2}$",
            f"**Solution 2:** $x = \\frac{{{-b} - {int(sqrt(discriminant))}}}{{2}} = \\frac{{{-b - int(sqrt(discriminant))}}}{{2}} = {(-b - int(sqrt(discriminant))) // 2}$",
            f"**Final Answer:** $x = {min(p, q)}$ or $x = {max(p, q)}$"
        ]

        answer = f"x = {min(p, q)}, {max(p, q)}"

    elif difficulty == 2:
        # Requires simplification - discriminant is a perfect square but needs reduction
        a = random.randint(2, 4)
        # Choose b and c such that discriminant is a perfect square
        p = random.randint(-4, 4)
        q = random.randint(-4, 4)

        # From (x - p)(x - q) = 0, multiply by a
        b = -a * (p + q)
        c = a * p * q

        equation = f"{a}x^2"
        if b != 0:
            equation += f" {'+' if b >= 0 else '-'} {abs(b)}x"
        if c != 0:
            equation += f" {'+' if c >= 0 else '-'} {abs(c)}"
        equation += " = 0"

        discriminant = b * b - 4 * a * c
        sqrt_disc = int(sqrt(discriminant))

        # Calculate solutions
        g = gcd(gcd(abs(-b + sqrt_disc), abs(-b - sqrt_disc)), 2 * a)

        steps = [
            f"Given: ${equation}$",
            f"Use the quadratic formula: $x = \\frac{{-b \\pm \\sqrt{{b^2 - 4ac}}}}{{2a}}$",
            f"Identify: $a = {a}$, $b = {b}$, $c = {c}$",
            f"Calculate the discriminant: $b^2 - 4ac$",
            f"$({b})^2 - 4({a})({c}) = {b*b} - {4*a*c} = {discriminant}$",
            f"$\\sqrt{{{discriminant}}} = {sqrt_disc}$",
            f"Substitute into the formula:",
            f"$x = \\frac{{-({b}) \\pm {sqrt_disc}}}{{2({a})}}$",
            f"$x = \\frac{{{-b} \\pm {sqrt_disc}}}{{{2*a}}}$",
            f"**Solution 1:** $x = \\frac{{{-b} + {sqrt_disc}}}{{{2*a}}} = \\frac{{{-b + sqrt_disc}}}{{{2*a}}}$",
        ]

        if (-b + sqrt_disc) % (2 * a) == 0:
            steps.append(f"$x = {(-b + sqrt_disc) // (2*a)}$")
        else:
            # Simplify fraction
            num1 = (-b + sqrt_disc) // g
            den1 = (2 * a) // g
            steps.append(f"Simplify: $x = \\frac{{{num1}}}{{{den1}}}$")

        steps.append(f"**Solution 2:** $x = \\frac{{{-b} - {sqrt_disc}}}{{{2*a}}} = \\frac{{{-b - sqrt_disc}}}{{{2*a}}}$")

        if (-b - sqrt_disc) % (2 * a) == 0:
            steps.append(f"$x = {(-b - sqrt_disc) // (2*a)}$")
            answer = f"x = {(-b - sqrt_disc) // (2*a)}, {(-b + sqrt_disc) // (2*a)}"
        else:
            num2 = (-b - sqrt_disc) // g
            den2 = (2 * a) // g
            steps.append(f"Simplify: $x = \\frac{{{num2}}}{{{den2}}}$")
            answer = f"x = {num2}/{den2}, {num1}/{den1}"

        steps.append(f"**Final Answer:** ${answer}$")

    else:  # difficulty == 3
        # Irrational solutions with radicals
        a = random.randint(1, 3)
        b = random.randint(-8, 8)
        if b == 0:
            b = 5
        c = random.randint(-6, 6)

        # Ensure discriminant is positive but not a perfect square
        discriminant = b * b - 4 * a * c
        while discriminant <= 0 or int(sqrt(discriminant)) ** 2 == discriminant:
            c = random.randint(-6, 6)
            discriminant = b * b - 4 * a * c

        equation = f"{a}x^2" if a != 1 else "x^2"
        if b != 0:
            equation += f" {'+' if b >= 0 else '-'} {abs(b)}x"
        if c != 0:
            equation += f" {'+' if c >= 0 else '-'} {abs(c)}"
        equation += " = 0"

        # Simplify the radical
        # Find largest perfect square factor
        radical = discriminant
        factor = 1
        for i in range(int(sqrt(discriminant)), 1, -1):
            if discriminant % (i * i) == 0:
                factor = i
                radical = discriminant // (i * i)
                break

        steps = [
            f"Given: ${equation}$",
            f"Use the quadratic formula: $x = \\frac{{-b \\pm \\sqrt{{b^2 - 4ac}}}}{{2a}}$",
            f"Identify: $a = {a}$, $b = {b}$, $c = {c}$",
            f"Calculate the discriminant: $b^2 - 4ac$",
            f"$({b})^2 - 4({a})({c}) = {b*b} - {4*a*c} = {discriminant}$",
        ]

        if factor > 1:
            steps.append(f"Simplify $\\sqrt{{{discriminant}}}$:")
            steps.append(f"$\\sqrt{{{discriminant}}} = \\sqrt{{{factor*factor} \\cdot {radical}}} = {factor}\\sqrt{{{radical}}}$")
            steps.append(f"Substitute into the formula:")
            steps.append(f"$x = \\frac{{-({b}) \\pm {factor}\\sqrt{{{radical}}}}}{{2({a})}}$")
            steps.append(f"$x = \\frac{{{-b} \\pm {factor}\\sqrt{{{radical}}}}}{{{2*a}}}$")

            # Check if we can simplify further
            g = gcd(gcd(abs(-b), factor), 2*a)
            if g > 1:
                steps.append(f"Factor out ${g}$:")
                steps.append(f"$x = \\frac{{{-b//g} \\pm {factor//g}\\sqrt{{{radical}}}}}{{{2*a//g}}}$")
                answer = f"x = ({-b//g} ± {factor//g}√{radical})/{2*a//g}"
            else:
                answer = f"x = ({-b} ± {factor}√{radical})/{2*a}"
        else:
            steps.append(f"Substitute into the formula:")
            steps.append(f"$x = \\frac{{-({b}) \\pm \\sqrt{{{discriminant}}}}}{{2({a})}}$")
            steps.append(f"$x = \\frac{{{-b} \\pm \\sqrt{{{discriminant}}}}}{{{2*a}}}$")
            answer = f"x = ({-b} ± √{discriminant})/{2*a}"

        steps.append(f"**Final Answer:** ${answer.replace('±', '\\pm').replace('√', '\\sqrt')}$")

    return {
        "question": f"Solve using the quadratic formula: ${equation}$",
        "answer": answer,
        "answer_numeric": None,
        "steps": steps,
        "difficulty": difficulty,
    }
