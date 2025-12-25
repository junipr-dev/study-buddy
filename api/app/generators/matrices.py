"""Matrices question generator."""

import random
from typing import Dict, Any

# Word problem templates for engaging, real-world contexts
ADDITION_WORD_PROBLEMS = [
    {
        "context": "A video game tracks player stats across two levels. Level 1 has the matrix A, and Level 2 has matrix B.",
        "question_template": "What are the combined stats after both levels?",
        "element_ask": "Find the value at position {pos_str} in the combined result."
    },
    {
        "context": "A network has two servers with traffic matrices A and B representing different time periods.",
        "question_template": "What is the total traffic load?",
        "element_ask": "Calculate the combined value at position {pos_str}."
    }
]

MULTIPLICATION_WORD_PROBLEMS = [
    {
        "context": "In a video game, matrix A represents rotation and scaling transformations, while matrix B represents a second transformation.",
        "question_template": "What is the combined transformation when applied in sequence?",
        "element_ask": "Find the resulting value at position {pos_str} after both transformations."
    },
    {
        "context": "A computer graphics engine uses matrix A for rotation and matrix B to apply textures. The product AB gives the final transformation.",
        "question_template": "What is the final transformation matrix?",
        "element_ask": "Calculate the element at position {pos_str} of the combined transformation."
    },
    {
        "context": "A weather model uses matrix A for temperature changes and B for humidity effects. Their product predicts combined environmental changes.",
        "question_template": "What are the predicted combined environmental effects?",
        "element_ask": "Find the combined effect value at position {pos_str}."
    }
]

DETERMINANT_WORD_PROBLEMS = [
    {
        "context": "In computer graphics, the determinant of a transformation matrix determines if the transformation preserves or flips orientation.",
        "question_template": "Does this transformation preserve orientation (positive determinant) or flip it (negative)?",
        "calculation": "Find the determinant of the matrix."
    },
    {
        "context": "A 2D encryption system uses a matrix to scramble data. The determinant must be non-zero for the matrix to be invertible (decodable).",
        "question_template": "Is this encryption matrix invertible?",
        "calculation": "Calculate the determinant to check if decryption is possible."
    },
    {
        "context": "In structural engineering, the determinant of a stiffness matrix indicates system stability.",
        "question_template": "Is the structure stable?",
        "calculation": "Find the determinant—zero means the structure is unstable."
    }
]


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
        use_word_problem = random.random() < 0.4

        if random.choice([True, False]):
            # Addition
            operation = "+"
            r11, r12 = a11 + b11, a12 + b12
            r21, r22 = a21 + b21, a22 + b22

            # Choose which element to ask for
            positions = [("(1,1)", r11), ("(1,2)", r12), ("(2,1)", r21), ("(2,2)", r22)]
            pos_str, answer = random.choice(positions)

            if use_word_problem:
                context = random.choice(ADDITION_WORD_PROBLEMS)
                question = f"{context['context']}\n\n"
                question += f"$A = \\begin{{bmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{bmatrix}}$, "
                question += f"$B = \\begin{{bmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{bmatrix}}$\n\n"
                question += context['element_ask'].format(pos_str=pos_str)
            else:
                question = f"Calculate $A + B$ and find the element at position {pos_str}:\n\n"
                question += f"$A = \\begin{{bmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{bmatrix}}$, "
                question += f"$B = \\begin{{bmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{bmatrix}}$"

            steps = [
                "To add matrices, we add corresponding elements (element-by-element):",
                "",
                f"$A + B = \\begin{{bmatrix}} {a11} + ({b11}) & {a12} + ({b12}) \\\\ {a21} + ({b21}) & {a22} + ({b22}) \\end{{bmatrix}}$",
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

            if use_word_problem:
                context = random.choice(ADDITION_WORD_PROBLEMS)
                question = f"{context['context']} (Now we're looking at differences.)\n\n"
                question += f"$A = \\begin{{bmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{bmatrix}}$, "
                question += f"$B = \\begin{{bmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{bmatrix}}$\n\n"
                question += f"Calculate $A - B$ and find the element at position {pos_str}."
            else:
                question = f"Calculate $A - B$ and find the element at position {pos_str}:\n\n"
                question += f"$A = \\begin{{bmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{bmatrix}}$, "
                question += f"$B = \\begin{{bmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{bmatrix}}$"

            steps = [
                "To subtract matrices, we subtract corresponding elements (element-by-element):",
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
        use_word_problem = random.random() < 0.4

        # Calculate product
        r11 = a11 * b11 + a12 * b21
        r12 = a11 * b12 + a12 * b22
        r21 = a21 * b11 + a22 * b21
        r22 = a21 * b12 + a22 * b22

        # Choose which element to ask for
        positions = [("(1,1)", r11), ("(1,2)", r12), ("(2,1)", r21), ("(2,2)", r22)]
        pos_str, answer = random.choice(positions)

        if use_word_problem:
            context = random.choice(MULTIPLICATION_WORD_PROBLEMS)
            question = f"{context['context']}\n\n"
            question += f"$A = \\begin{{bmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{bmatrix}}$, "
            question += f"$B = \\begin{{bmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{bmatrix}}$\n\n"
            question += context['element_ask'].format(pos_str=pos_str)
        else:
            question = f"Calculate $AB$ and find the element at position {pos_str}:\n\n"
            question += f"$A = \\begin{{bmatrix}} {a11} & {a12} \\\\ {a21} & {a22} \\end{{bmatrix}}$, "
            question += f"$B = \\begin{{bmatrix}} {b11} & {b12} \\\\ {b21} & {b22} \\end{{bmatrix}}$"

        steps = [
            "To multiply 2×2 matrices, each element is the dot product of the corresponding row and column:",
            "",
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
        use_word_problem = random.random() < 0.4

        determinant = a * d - b * c

        if use_word_problem:
            context = random.choice(DETERMINANT_WORD_PROBLEMS)
            question = f"{context['context']}\n\n"
            question += f"$A = \\begin{{bmatrix}} {a} & {b} \\\\ {c} & {d} \\end{{bmatrix}}$\n\n"
            question += context['calculation']
        else:
            question = f"Find the determinant of the matrix:\n\n$A = \\begin{{bmatrix}} {a} & {b} \\\\ {c} & {d} \\end{{bmatrix}}$"

        steps = [
            "The determinant of a 2×2 matrix $\\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}$ is:",
            "$\\det(A) = ad - bc$",
            "",
            "The determinant tells us about the transformation: whether it flips the orientation, scales area, or inverses the matrix.",
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
