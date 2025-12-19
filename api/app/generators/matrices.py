"""Matrices question generator."""

import random
from typing import Dict, Any


def generate_matrices(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a matrices problem.

    Args:
        difficulty: 1 (matrix addition/subtraction), 2 (matrix multiplication), 3 (determinant)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Matrix addition or subtraction - find one element
        # 2x2 matrices
        a11, a12 = random.randint(-5, 5), random.randint(-5, 5)
        a21, a22 = random.randint(-5, 5), random.randint(-5, 5)
        b11, b12 = random.randint(-5, 5), random.randint(-5, 5)
        b21, b22 = random.randint(-5, 5), random.randint(-5, 5)

        if random.choice([True, False]):
            # Addition
            operation = "+"
            r11, r12 = a11 + b11, a12 + b12
            r21, r22 = a21 + b21, a22 + b22

            # Choose which element to ask for
            positions = [("(1,1)", r11), ("(1,2)", r12), ("(2,1)", r21), ("(2,2)", r22)]
            pos_str, answer = random.choice(positions)

            question = f"Calculate $A + B$ and find the element at position {pos_str}:\n\n"
            question += f"$A = \\begin{{bmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{bmatrix}}$, "
            question += f"$B = \\begin{{bmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{bmatrix}}$"

            steps = [
                "To add matrices, add corresponding elements:",
                "",
                f"$A + B = \\begin{{bmatrix}} {a11} + {b11} & {a12} + {b12} \\\\ {a21} + {b21} & {a22} + {b22} \\end{{bmatrix}}$",
                "",
                f"$A + B = \\begin{{bmatrix}} {r11} & {r12} \\\\ {r21} & {r22} \\end{{bmatrix}}$",
                "",
                f"The element at position {pos_str} is ${answer}$.",
                "",
                f"**Final Answer:** ${answer}$"
            ]
        else:
            # Subtraction
            operation = "-"
            r11, r12 = a11 - b11, a12 - b12
            r21, r22 = a21 - b21, a22 - b22

            # Choose which element to ask for
            positions = [("(1,1)", r11), ("(1,2)", r12), ("(2,1)", r21), ("(2,2)", r22)]
            pos_str, answer = random.choice(positions)

            question = f"Calculate $A - B$ and find the element at position {pos_str}:\n\n"
            question += f"$A = \\begin{{bmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{bmatrix}}$, "
            question += f"$B = \\begin{{bmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{bmatrix}}$"

            steps = [
                "To subtract matrices, subtract corresponding elements:",
                "",
                f"$A - B = \\begin{{bmatrix}} {a11} - ({b11}) & {a12} - ({b12}) \\\\ {a21} - ({b21}) & {a22} - ({b22}) \\end{{bmatrix}}$",
                "",
                f"$A - B = \\begin{{bmatrix}} {r11} & {r12} \\\\ {r21} & {r22} \\end{{bmatrix}}$",
                "",
                f"The element at position {pos_str} is ${answer}$.",
                "",
                f"**Final Answer:** ${answer}$"
            ]

        answer_numeric = answer

    elif difficulty == 2:
        # Medium: Matrix multiplication (2x2)
        a11, a12 = random.randint(-3, 3), random.randint(-3, 3)
        a21, a22 = random.randint(-3, 3), random.randint(-3, 3)
        b11, b12 = random.randint(-3, 3), random.randint(-3, 3)
        b21, b22 = random.randint(-3, 3), random.randint(-3, 3)

        # Calculate product
        r11 = a11 * b11 + a12 * b21
        r12 = a11 * b12 + a12 * b22
        r21 = a21 * b11 + a22 * b21
        r22 = a21 * b12 + a22 * b22

        # Choose which element to ask for
        positions = [("(1,1)", r11), ("(1,2)", r12), ("(2,1)", r21), ("(2,2)", r22)]
        pos_str, answer = random.choice(positions)

        question = f"Calculate $AB$ and find the element at position {pos_str}:\n\n"
        question += f"$A = \\begin{{bmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{bmatrix}}$, "
        question += f"$B = \\begin{{bmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{bmatrix}}$"

        steps = [
            "To multiply 2×2 matrices, use the formula:",
            "$AB = \\begin{bmatrix} a_{11}b_{11}+a_{12}b_{21} & a_{11}b_{12}+a_{12}b_{22} \\\\ a_{21}b_{11}+a_{22}b_{21} & a_{21}b_{12}+a_{22}b_{22} \\end{bmatrix}$",
            "",
            "Calculate each element:",
            f"- $(1,1)$: $({a11})({b11}) + ({a12})({b21}) = {a11*b11} + {a12*b21} = {r11}$",
            f"- $(1,2)$: $({a11})({b12}) + ({a12})({b22}) = {a11*b12} + {a12*b22} = {r12}$",
            f"- $(2,1)$: $({a21})({b11}) + ({a22})({b21}) = {a21*b11} + {a22*b21} = {r21}$",
            f"- $(2,2)$: $({a21})({b12}) + ({a22})({b22}) = {a21*b12} + {a22*b22} = {r22}$",
            "",
            f"$AB = \\begin{{bmatrix}} {r11} & {r12} \\\\ {r21} & {r22} \\end{{bmatrix}}$",
            "",
            f"The element at position {pos_str} is ${answer}$.",
            "",
            f"**Final Answer:** ${answer}$"
        ]

        answer_numeric = answer

    else:
        # Hard: Determinant of 2x2 matrix
        a = random.randint(-5, 5)
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)
        d = random.randint(-5, 5)

        determinant = a * d - b * c

        question = f"Find the determinant of the matrix:\n\n$A = \\begin{{bmatrix}} {a} & {b} \\\\ {c} & {d} \\end{{bmatrix}}$"

        steps = [
            "The determinant of a 2×2 matrix $\\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}$ is:",
            "$\\det(A) = ad - bc$",
            "",
            f"Substitute the values:",
            f"$\\det(A) = ({a})({d}) - ({b})({c})$",
            f"$\\det(A) = {a * d} - {b * c}$",
            f"$\\det(A) = {determinant}$",
            "",
            f"**Final Answer:** ${determinant}$"
        ]

        answer_numeric = determinant

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
