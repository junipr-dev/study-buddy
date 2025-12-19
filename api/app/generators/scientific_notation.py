"""Scientific notation generator."""

import random
from typing import Dict, Any, List


def generate_scientific_notation(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate scientific notation problems.

    Args:
        difficulty: 1 (convert to/from), 2 (multiply/divide), 3 (mixed operations)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Convert to/from scientific notation
        conversion_type = random.choice(["to_scientific", "from_scientific"])

        if conversion_type == "to_scientific":
            # Generate a large or small number
            if random.choice([True, False]):
                # Large number
                exponent = random.randint(3, 8)
                coefficient = random.randint(1, 9) + random.randint(0, 99) / 100
                number = coefficient * (10 ** exponent)

                # Adjust coefficient to be between 1 and 10
                adjusted_coef = coefficient
                adjusted_exp = exponent

                steps = [
                    f"Convert ${number:,.0f}$ to scientific notation",
                    f"Move the decimal point left until we have a number between 1 and 10",
                    f"Count how many places we moved: ${adjusted_exp}$ places",
                    f"The coefficient is ${adjusted_coef:.2f}$",
                    f"**Final Answer:** ${adjusted_coef:.2f} \\times 10^{{{adjusted_exp}}}$"
                ]

                answer = f"{adjusted_coef:.2f}×10^{adjusted_exp}"
            else:
                # Small number
                exponent = random.randint(-6, -2)
                coefficient = random.randint(1, 9) + random.randint(0, 99) / 100
                number = coefficient * (10 ** exponent)

                steps = [
                    f"Convert ${number}$ to scientific notation",
                    f"Move the decimal point right until we have a number between 1 and 10",
                    f"Count how many places we moved: ${abs(exponent)}$ places",
                    f"Since we moved right, the exponent is negative: ${exponent}$",
                    f"The coefficient is ${coefficient:.2f}$",
                    f"**Final Answer:** ${coefficient:.2f} \\times 10^{{{exponent}}}$"
                ]

                answer = f"{coefficient:.2f}×10^{exponent}"
        else:
            # From scientific notation
            exponent = random.randint(-4, 6)
            coefficient = random.randint(10, 99) / 10

            result = coefficient * (10 ** exponent)

            steps = [
                f"Convert ${coefficient} \\times 10^{{{exponent}}}$ to standard form",
                f"Multiply ${coefficient}$ by $10^{{{exponent}}}$",
                f"Move the decimal point ${abs(exponent)}$ places {'right' if exponent > 0 else 'left'}",
                f"**Final Answer:** ${result:,.10g}$"
            ]

            answer = f"{result:,.10g}"

        question = f"Convert ${number:,.10g}$ to scientific notation" if conversion_type == "to_scientific" else f"Convert ${coefficient} \\times 10^{{{exponent}}}$ to standard form"

    elif difficulty == 2:
        # Multiply or divide in scientific notation
        operation = random.choice(["multiply", "divide"])

        coef1 = random.randint(10, 99) / 10
        exp1 = random.randint(-3, 5)
        coef2 = random.randint(10, 99) / 10
        exp2 = random.randint(-3, 5)

        if operation == "multiply":
            result_coef = coef1 * coef2
            result_exp = exp1 + exp2

            # Adjust if coefficient >= 10
            if result_coef >= 10:
                result_coef /= 10
                result_exp += 1

            steps = [
                f"Multiply: $({coef1} \\times 10^{{{exp1}}}) \\times ({coef2} \\times 10^{{{exp2}}})$",
                f"Multiply the coefficients: ${coef1} \\times {coef2} = {coef1 * coef2}$",
                f"Add the exponents: ${exp1} + {exp2} = {exp1 + exp2}$",
                f"Result: ${coef1 * coef2} \\times 10^{{{exp1 + exp2}}}$",
            ]

            if coef1 * coef2 >= 10:
                steps.append(f"Adjust coefficient to be between 1 and 10:")
                steps.append(f"${coef1 * coef2} = {result_coef:.1f} \\times 10^1$")
                steps.append(f"So: ${result_coef:.1f} \\times 10^1 \\times 10^{{{exp1 + exp2}}} = {result_coef:.1f} \\times 10^{{{result_exp}}}$")

            steps.append(f"**Final Answer:** ${result_coef:.1f} \\times 10^{{{result_exp}}}$")

            answer = f"{result_coef:.1f}×10^{result_exp}"
            question = f"Multiply: $({coef1} \\times 10^{{{exp1}}}) \\times ({coef2} \\times 10^{{{exp2}}})$"

        else:  # divide
            result_coef = coef1 / coef2
            result_exp = exp1 - exp2

            # Adjust if coefficient < 1
            if result_coef < 1:
                result_coef *= 10
                result_exp -= 1

            steps = [
                f"Divide: $\\frac{{{coef1} \\times 10^{{{exp1}}}}}{{{coef2} \\times 10^{{{exp2}}}}}$",
                f"Divide the coefficients: $\\frac{{{coef1}}}{{{coef2}}} = {coef1 / coef2:.2f}$",
                f"Subtract the exponents: ${exp1} - ({exp2}) = {exp1 - exp2}$",
                f"Result: ${coef1 / coef2:.2f} \\times 10^{{{exp1 - exp2}}}$",
            ]

            if coef1 / coef2 < 1:
                steps.append(f"Adjust coefficient to be between 1 and 10:")
                steps.append(f"${coef1 / coef2:.2f} = {result_coef:.2f} \\times 10^{{-1}}$")
                steps.append(f"So: ${result_coef:.2f} \\times 10^{{-1}} \\times 10^{{{exp1 - exp2}}} = {result_coef:.2f} \\times 10^{{{result_exp}}}$")

            steps.append(f"**Final Answer:** ${result_coef:.2f} \\times 10^{{{result_exp}}}$")

            answer = f"{result_coef:.2f}×10^{result_exp}"
            question = f"Divide: $\\frac{{{coef1} \\times 10^{{{exp1}}}}}{{{coef2} \\times 10^{{{exp2}}}}}$"

    else:  # difficulty == 3
        # Mixed operations
        coef1 = random.randint(10, 99) / 10
        exp1 = random.randint(-2, 4)
        coef2 = random.randint(10, 99) / 10
        exp2 = random.randint(-2, 4)
        coef3 = random.randint(10, 99) / 10
        exp3 = random.randint(-2, 4)

        # (a × 10^n)(b × 10^m) / (c × 10^p)
        question = f"$\\frac{{({coef1} \\times 10^{{{exp1}}}) \\times ({coef2} \\times 10^{{{exp2}}})}}{{({coef3} \\times 10^{{{exp3}}})}}$"

        # Step 1: Multiply numerator
        num_coef = coef1 * coef2
        num_exp = exp1 + exp2

        # Step 2: Divide
        result_coef = num_coef / coef3
        result_exp = num_exp - exp3

        # Adjust coefficient
        while result_coef >= 10:
            result_coef /= 10
            result_exp += 1
        while result_coef < 1:
            result_coef *= 10
            result_exp -= 1

        steps = [
            f"Simplify: {question}",
            f"**Step 1:** Multiply the numerator",
            f"$({coef1} \\times 10^{{{exp1}}}) \\times ({coef2} \\times 10^{{{exp2}}})$",
            f"Coefficients: ${coef1} \\times {coef2} = {num_coef}$",
            f"Exponents: ${exp1} + {exp2} = {num_exp}$",
            f"Numerator: ${num_coef} \\times 10^{{{num_exp}}}$",
            f"**Step 2:** Divide by the denominator",
            f"$\\frac{{{num_coef} \\times 10^{{{num_exp}}}}}{{{coef3} \\times 10^{{{exp3}}}}}$",
            f"Coefficients: $\\frac{{{num_coef}}}{{{coef3}}} = {num_coef/coef3:.2f}$",
            f"Exponents: ${num_exp} - {exp3} = {num_exp - exp3}$",
            f"Result: ${num_coef/coef3:.2f} \\times 10^{{{num_exp - exp3}}}$",
        ]

        if abs(result_coef - num_coef/coef3) > 0.01 or result_exp != num_exp - exp3:
            steps.append(f"Adjust to proper scientific notation:")
            steps.append(f"${result_coef:.2f} \\times 10^{{{result_exp}}}$")

        steps.append(f"**Final Answer:** ${result_coef:.2f} \\times 10^{{{result_exp}}}$")

        answer = f"{result_coef:.2f}×10^{result_exp}"

    return {
        "question": question,
        "answer": answer,
        "answer_numeric": None,
        "steps": steps,
        "difficulty": difficulty,
    }
