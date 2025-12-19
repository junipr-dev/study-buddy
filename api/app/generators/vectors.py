"""Vectors question generator."""

import random
import math
from typing import Dict, Any


def generate_vectors(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a vectors problem.

    Args:
        difficulty: 1 (magnitude), 2 (vector addition), 3 (dot product)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Find magnitude of a vector
        # Use Pythagorean triples for 2D vectors
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10)]
        x, y, magnitude = random.choice(triples)

        # Randomly negate components
        if random.choice([True, False]):
            x = -x
        if random.choice([True, False]):
            y = -y

        question = f"Find the magnitude of the vector $\\vec{{v}} = \\langle {x}, {y} \\rangle$."

        steps = [
            "The magnitude of a vector $\\vec{v} = \\langle x, y \\rangle$ is:",
            "$||\\vec{v}|| = \\sqrt{x^2 + y^2}$",
            "",
            f"Substitute the values:",
            f"$||\\vec{{v}}|| = \\sqrt{{({x})^2 + ({y})^2}}$",
            f"$||\\vec{{v}}|| = \\sqrt{{{x**2} + {y**2}}}$",
            f"$||\\vec{{v}}|| = \\sqrt{{{x**2 + y**2}}}$",
            f"$||\\vec{{v}}|| = {magnitude}$",
            "",
            f"**Final Answer:** ${magnitude}$"
        ]

        answer_numeric = magnitude

    elif difficulty == 2:
        # Medium: Vector addition/subtraction - find component
        x1 = random.randint(-5, 5)
        y1 = random.randint(-5, 5)
        x2 = random.randint(-5, 5)
        y2 = random.randint(-5, 5)

        if random.choice([True, False]):
            # Addition
            result_x = x1 + x2
            result_y = y1 + y2
            operation = "+"

            question = f"If $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ and $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$, find the $x$-component of $\\vec{{u}} + \\vec{{v}}$."

            steps = [
                "To add vectors, add corresponding components:",
                "$\\vec{u} + \\vec{v} = \\langle x_1 + x_2, y_1 + y_2 \\rangle$",
                "",
                f"Calculate:",
                f"$\\vec{{u}} + \\vec{{v}} = \\langle {x1} + ({x2}), {y1} + ({y2}) \\rangle$",
                f"$\\vec{{u}} + \\vec{{v}} = \\langle {result_x}, {result_y} \\rangle$",
                "",
                f"The $x$-component is ${result_x}$.",
                "",
                f"**Final Answer:** ${result_x}$"
            ]

            answer_numeric = result_x
        else:
            # Subtraction
            result_x = x1 - x2
            result_y = y1 - y2
            operation = "-"

            question = f"If $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ and $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$, find the $y$-component of $\\vec{{u}} - \\vec{{v}}$."

            steps = [
                "To subtract vectors, subtract corresponding components:",
                "$\\vec{u} - \\vec{v} = \\langle x_1 - x_2, y_1 - y_2 \\rangle$",
                "",
                f"Calculate:",
                f"$\\vec{{u}} - \\vec{{v}} = \\langle {x1} - ({x2}), {y1} - ({y2}) \\rangle$",
                f"$\\vec{{u}} - \\vec{{v}} = \\langle {result_x}, {result_y} \\rangle$",
                "",
                f"The $y$-component is ${result_y}$.",
                "",
                f"**Final Answer:** ${result_y}$"
            ]

            answer_numeric = result_y

    else:
        # Hard: Dot product
        x1 = random.randint(-4, 4)
        y1 = random.randint(-4, 4)
        x2 = random.randint(-4, 4)
        y2 = random.randint(-4, 4)

        dot_product = x1 * x2 + y1 * y2

        question = f"Find the dot product of $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ and $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$."

        steps = [
            "The dot product of two vectors $\\vec{u} = \\langle x_1, y_1 \\rangle$ and $\\vec{v} = \\langle x_2, y_2 \\rangle$ is:",
            "$\\vec{u} \\cdot \\vec{v} = x_1 x_2 + y_1 y_2$",
            "",
            f"Substitute the values:",
            f"$\\vec{{u}} \\cdot \\vec{{v}} = ({x1})({x2}) + ({y1})({y2})$",
            f"$\\vec{{u}} \\cdot \\vec{{v}} = {x1 * x2} + {y1 * y2}$",
            f"$\\vec{{u}} \\cdot \\vec{{v}} = {dot_product}$",
            "",
            f"**Final Answer:** ${dot_product}$"
        ]

        answer_numeric = dot_product

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
