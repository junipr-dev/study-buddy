"""Piecewise functions question generator."""

import random
from typing import Dict, Any


def generate_piecewise_functions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a piecewise function evaluation problem.

    Args:
        difficulty: 1 (simple two-piece), 2 (three-piece), 3 (boundary values)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Two-piece linear function
        a1 = random.randint(2, 5)
        b1 = random.randint(-5, 5)
        a2 = random.randint(2, 5)
        b2 = random.randint(-5, 5)
        cutoff = random.randint(0, 3)

        # Choose evaluation point
        if random.choice([True, False]):
            # Evaluate in first piece
            x_val = cutoff - random.randint(1, 3)
            result = a1 * x_val + b1
            piece_used = "first"
            condition = f"x < {cutoff}"
        else:
            # Evaluate in second piece
            x_val = cutoff + random.randint(1, 3)
            result = a2 * x_val + b2
            piece_used = "second"
            condition = f"x \\geq {cutoff}"

        question = f"Evaluate the piecewise function at $x = {x_val}$:\n\n"
        question += "$f(x) = \\begin{cases}\n"
        question += f"{a1}x {b1:+d} & \\text{{if }} x < {cutoff} \\\\\n"
        question += f"{a2}x {b2:+d} & \\text{{if }} x \\geq {cutoff}\n"
        question += "\\end{cases}$"

        steps = [
            f"We need to evaluate $f({x_val})$.",
            "",
            f"First, determine which piece to use:",
            f"Since ${x_val}$ satisfies ${condition}$, we use the {piece_used} piece.",
            "",
            f"The {piece_used} piece is: $f(x) = {a1 if piece_used == 'first' else a2}x {(b1 if piece_used == 'first' else b2):+d}$",
            "",
            f"Substitute $x = {x_val}$:",
            f"$f({x_val}) = {a1 if piece_used == 'first' else a2}({x_val}) {(b1 if piece_used == 'first' else b2):+d}$",
            f"$f({x_val}) = {(a1 if piece_used == 'first' else a2) * x_val} {(b1 if piece_used == 'first' else b2):+d}$",
            f"$f({x_val}) = {result}$",
            "",
            f"**Final Answer:** ${result}$"
        ]

        answer_numeric = result

    elif difficulty == 2:
        # Medium: Three-piece function
        c1 = random.randint(-3, -1)
        c2 = random.randint(1, 3)

        # Define three pieces
        pieces = [
            (f"x^2", lambda x: x**2, f"x < {c1}"),
            (f"{random.randint(2, 4)}x", lambda x: random.randint(2, 4) * x, f"{c1} \\leq x < {c2}"),
            (f"{random.randint(1, 3)}", lambda x: random.randint(1, 3), f"x \\geq {c2}")
        ]

        # Store the constant and coefficient for middle piece
        middle_coef = random.randint(2, 4)
        constant_val = random.randint(1, 3)
        pieces = [
            (f"x^2", lambda x: x**2, f"x < {c1}"),
            (f"{middle_coef}x", lambda x: middle_coef * x, f"{c1} \\leq x < {c2}"),
            (f"{constant_val}", lambda x: constant_val, f"x \\geq {c2}")
        ]

        # Choose which piece to evaluate
        piece_choice = random.randint(0, 2)
        if piece_choice == 0:
            x_val = c1 - random.randint(1, 2)
            result = x_val ** 2
        elif piece_choice == 1:
            x_val = random.randint(c1, c2 - 1)
            result = middle_coef * x_val
        else:
            x_val = c2 + random.randint(0, 2)
            result = constant_val

        question = f"Evaluate the piecewise function at $x = {x_val}$:\n\n"
        question += "$f(x) = \\begin{cases}\n"
        question += f"x^2 & \\text{{if }} x < {c1} \\\\\n"
        question += f"{middle_coef}x & \\text{{if }} {c1} \\leq x < {c2} \\\\\n"
        question += f"{constant_val} & \\text{{if }} x \\geq {c2}\n"
        question += "\\end{cases}$"

        steps = [
            f"We need to evaluate $f({x_val})$.",
            "",
            "Determine which piece to use:",
        ]

        if piece_choice == 0:
            steps.extend([
                f"Since ${x_val} < {c1}$, we use the first piece: $f(x) = x^2$",
                "",
                f"Substitute $x = {x_val}$:",
                f"$f({x_val}) = ({x_val})^2 = {result}$",
            ])
        elif piece_choice == 1:
            steps.extend([
                f"Since ${c1} \\leq {x_val} < {c2}$, we use the second piece: $f(x) = {middle_coef}x$",
                "",
                f"Substitute $x = {x_val}$:",
                f"$f({x_val}) = {middle_coef}({x_val}) = {result}$",
            ])
        else:
            steps.extend([
                f"Since ${x_val} \\geq {c2}$, we use the third piece: $f(x) = {constant_val}$",
                "",
                f"This piece is constant, so $f({x_val}) = {constant_val}$",
            ])

        steps.extend([
            "",
            f"**Final Answer:** ${result}$"
        ])

        answer_numeric = result

    else:
        # Hard: Boundary value evaluation
        cutoff = random.randint(0, 3)
        a = random.randint(2, 4)
        b = random.randint(1, 5)

        # Evaluate exactly at the boundary
        x_val = cutoff
        result = a * x_val + b  # Using the second piece since x ≥ cutoff

        question = f"Evaluate the piecewise function at the boundary point $x = {x_val}$:\n\n"
        question += "$f(x) = \\begin{cases}\n"
        question += f"x^2 - {b} & \\text{{if }} x < {cutoff} \\\\\n"
        question += f"{a}x + {b} & \\text{{if }} x \\geq {cutoff}\n"
        question += "\\end{cases}$"

        steps = [
            f"We need to evaluate $f({x_val})$.",
            "",
            f"Notice that $x = {x_val}$ is exactly at the boundary between the two pieces.",
            "",
            f"Check the conditions:",
            f"- First piece applies when $x < {cutoff}$",
            f"- Second piece applies when $x \\geq {cutoff}$",
            "",
            f"Since ${x_val} \\geq {cutoff}$ (equality holds), we use the second piece.",
            "",
            f"The second piece is: $f(x) = {a}x + {b}$",
            "",
            f"Substitute $x = {x_val}$:",
            f"$f({x_val}) = {a}({x_val}) + {b}$",
            f"$f({x_val}) = {a * x_val} + {b}$",
            f"$f({x_val}) = {result}$",
            "",
            f"**Final Answer:** ${result}$"
        ]

        answer_numeric = result

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
