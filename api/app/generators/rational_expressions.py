"""Rational expressions generator."""

import random
from typing import Dict, Any, List
from math import gcd


def generate_rational_expressions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate rational expressions problems.

    Args:
        difficulty: 1 (simplify), 2 (add/subtract), 3 (multiply/divide)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Simplify rational expressions
        # Create expression with common factors
        common = random.randint(2, 5)
        a = random.randint(2, 6)
        b = random.randint(2, 6)

        numerator_coef = common * a
        denominator_coef = common * b

        # Format: (common*a)x / (common*b)x
        question = f"\\frac{{{numerator_coef}x}}{{{denominator_coef}x}}"

        # Simplify
        g = gcd(numerator_coef, denominator_coef)
        simplified_num = numerator_coef // g
        simplified_den = denominator_coef // g

        steps = [
            f"Simplify: ${question}$",
            f"Factor out the greatest common factor from numerator and denominator",
            f"Numerator: ${numerator_coef}x = {g} \\cdot {simplified_num}x$",
            f"Denominator: ${denominator_coef}x = {g} \\cdot {simplified_den}x$",
            f"$\\frac{{{g} \\cdot {simplified_num}x}}{{{g} \\cdot {simplified_den}x}}$",
            f"Cancel the common factor ${g}x$:",
            f"$\\frac{{{simplified_num}}}{{{simplified_den}}}$",
        ]

        if simplified_den == 1:
            steps.append(f"**Final Answer:** ${simplified_num}$")
            answer = str(simplified_num)
        else:
            steps.append(f"**Final Answer:** $\\frac{{{simplified_num}}}{{{simplified_den}}}$")
            answer = f"{simplified_num}/{simplified_den}"

    elif difficulty == 2:
        # Add or subtract with different denominators
        operation = random.choice(["+", "-"])

        # Create two fractions with different denominators
        # a/bx ± c/dx
        a = random.randint(1, 5)
        b = random.randint(2, 5)
        c = random.randint(1, 5)
        d = random.randint(2, 5)

        # Make sure b != d
        while b == d:
            d = random.randint(2, 5)

        question = f"\\frac{{{a}}}{{{b}x}} {operation} \\frac{{{c}}}{{{d}x}}"

        # Find LCD (least common denominator)
        # LCD of bx and dx is lcm(b,d) * x
        from math import lcm
        lcd_coef = lcm(b, d)

        # Convert fractions
        mult1 = lcd_coef // b
        mult2 = lcd_coef // d

        new_num1 = a * mult1
        new_num2 = c * mult2

        if operation == "+":
            result_num = new_num1 + new_num2
            op_word = "add"
        else:
            result_num = new_num1 - new_num2
            op_word = "subtract"

        steps = [
            f"${question}$",
            f"Find the LCD (Least Common Denominator) of ${b}x$ and ${d}x$",
            f"LCD = ${lcd_coef}x$",
            f"Convert each fraction to have denominator ${lcd_coef}x$:",
            f"$\\frac{{{a}}}{{{b}x}} = \\frac{{{a} \\cdot {mult1}}}{{{b}x \\cdot {mult1}}} = \\frac{{{new_num1}}}{{{lcd_coef}x}}$",
            f"$\\frac{{{c}}}{{{d}x}} = \\frac{{{c} \\cdot {mult2}}}{{{d}x \\cdot {mult2}}} = \\frac{{{new_num2}}}{{{lcd_coef}x}}$",
            f"Now {op_word}:",
            f"$\\frac{{{new_num1}}}{{{lcd_coef}x}} {operation} \\frac{{{new_num2}}}{{{lcd_coef}x}} = \\frac{{{new_num1} {operation} {new_num2}}}{{{lcd_coef}x}}$",
            f"$= \\frac{{{result_num}}}{{{lcd_coef}x}}$",
        ]

        # Simplify if possible
        if result_num != 0:
            g = gcd(abs(result_num), lcd_coef)
            if g > 1:
                steps.append(f"Simplify by dividing both numerator and denominator by ${g}$:")
                steps.append(f"$\\frac{{{result_num // g}}}{{{lcd_coef // g}x}}$")
                answer = f"{result_num // g}/{lcd_coef // g}x"
            else:
                answer = f"{result_num}/{lcd_coef}x"
            steps.append(f"**Final Answer:** ${answer.replace('/', '}{').replace('x', 'x}}').replace('{', '{', 1).replace('}', '', 1)}$".replace('}{', '}{'))
            answer = f"{result_num // g}/{lcd_coef // g}x" if g > 1 else f"{result_num}/{lcd_coef}x"
        else:
            steps.append(f"**Final Answer:** $0$")
            answer = "0"

    else:  # difficulty == 3
        # Multiply or divide rational expressions
        operation = random.choice(["multiply", "divide"])

        # Create fractions (ax/b) and (c/dx)
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(2, 6)
        d = random.randint(2, 6)

        if operation == "multiply":
            question = f"\\frac{{{a}x}}{{{b}}} \\cdot \\frac{{{c}}}{{{d}x}}"

            # Multiply: (ax/b) * (c/dx) = (acx)/(bdx) = ac/bd
            result_num = a * c
            result_den = b * d

            steps = [
                f"Multiply: ${question}$",
                f"Multiply numerators and denominators:",
                f"$\\frac{{{a}x \\cdot {c}}}{{{b} \\cdot {d}x}}$",
                f"$= \\frac{{{a * c}x}}{{{b * d}x}}$",
                f"Cancel $x$ from numerator and denominator:",
                f"$= \\frac{{{a * c}}}{{{b * d}}}$",
            ]

            # Simplify
            g = gcd(result_num, result_den)
            if g > 1:
                steps.append(f"Simplify by dividing by ${g}$:")
                steps.append(f"$\\frac{{{result_num // g}}}{{{result_den // g}}}$")
                answer = f"{result_num // g}/{result_den // g}"
            else:
                answer = f"{result_num}/{result_den}"

            steps.append(f"**Final Answer:** ${answer.replace('/', '}}{').replace('{', '\\frac{' + '{', 1)}$")

        else:  # divide
            question = f"\\frac{{{a}x}}{{{b}}} \\div \\frac{{{c}}}{{{d}x}}"

            # Divide: (ax/b) ÷ (c/dx) = (ax/b) * (dx/c) = (adx²)/(bc)
            steps = [
                f"Divide: ${question}$",
                f"Multiply by the reciprocal:",
                f"$\\frac{{{a}x}}{{{b}}} \\cdot \\frac{{{d}x}}{{{c}}}$",
                f"Multiply numerators and denominators:",
                f"$\\frac{{{a}x \\cdot {d}x}}{{{b} \\cdot {c}}}$",
                f"$= \\frac{{{a * d}x^2}}{{{b * c}}}$",
            ]

            result_num = a * d
            result_den = b * c

            # Simplify
            g = gcd(result_num, result_den)
            if g > 1:
                steps.append(f"Simplify by dividing by ${g}$:")
                steps.append(f"$\\frac{{{result_num // g}x^2}}{{{result_den // g}}}$")
                answer = f"{result_num // g}x²/{result_den // g}"
            else:
                answer = f"{result_num}x²/{result_den}"

            steps.append(f"**Final Answer:** $\\frac{{{result_num // g if g > 1 else result_num}x^2}}{{{result_den // g if g > 1 else result_den}}}$")

    return {
        "question": f"Simplify: ${question}$",
        "answer": answer,
        "answer_numeric": None,
        "steps": steps,
        "difficulty": difficulty,
    }
