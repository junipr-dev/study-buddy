"""Vectors question generator."""

import random
import math
from typing import Dict, Any

# Word problem templates for engaging, real-world contexts
MAGNITUDE_WORD_PROBLEMS = [
    {
        "context": "A force vector represents a push or pull with components $\\vec{{F}} = \\langle {x}, {y} \\rangle$ (in Newtons).",
        "question": "What is the magnitude of the force?"
    },
    {
        "context": "A ship's velocity vector describes its speed and direction: $\\vec{{v}} = \\langle {x}, {y} \\rangle$ (in m/s).",
        "question": "What is the ship's actual speed?"
    },
    {
        "context": "A displacement vector shows how far an object moved: $\\vec{{d}} = \\langle {x}, {y} \\rangle$ (in meters).",
        "question": "What is the total distance traveled?"
    }
]

ADDITION_WORD_PROBLEMS = [
    {
        "context": "A boat moves with velocity $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ (m/s). A water current adds velocity $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$ (m/s).",
        "question": "What is the combined velocity?",
        "operation": "+"
    },
    {
        "context": "A game character has position $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$. They move by displacement $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$.",
        "question": "What is the new position?",
        "operation": "+"
    },
    {
        "context": "Two forces act on an object: $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ N and $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$ N.",
        "question": "What is the net force in the $x$-direction?",
        "operation": "+"
    },
    {
        "context": "A plane's heading is $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ and wind changes it by $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$.",
        "question": "What is the resulting velocity after the wind effect?",
        "operation": "-"
    }
]

DOTPRODUCT_WORD_PROBLEMS = [
    {
        "context": "A force $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ acts on an object, moving it along direction $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$.",
        "question": "What is the work done (force projected onto motion)?"
    },
    {
        "context": "Two vectors represent light rays: $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ and $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$.",
        "question": "What is their dot product (related to angle between them)?"
    },
    {
        "context": "In a game physics engine, velocity $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ collides with surface normal $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$.",
        "question": "Calculate the dot product to determine collision response."
    }
]


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
        use_word_problem = random.random() < 0.4

        # Randomly negate components
        if random.choice([True, False]):
            x = -x
        if random.choice([True, False]):
            y = -y

        if use_word_problem:
            context = random.choice(MAGNITUDE_WORD_PROBLEMS)
            context_text = context["context"].format(x=x, y=y)
            question = f"{context_text}\n\n{context['question']}"
        else:
            question = f"Find the magnitude of the vector $\\vec{{v}} = \\langle {x}, {y} \\rangle$."

        steps = [
            "The magnitude (or length) of a vector $\\vec{v} = \\langle x, y \\rangle$ is:",
            "$||\\vec{v}|| = \\sqrt{x^2 + y^2}$",
            "",
            f"Substitute the values:",
            f"$||\\vec{{v}}|| = \\sqrt{{({x})^2 + ({y})^2}}$",
            f"$||\\vec{{v}}|| = \\sqrt{{{x**2} + {y**2}}}$",
            f"$||\\vec{{v}}|| = \\sqrt{{{x**2 + y**2}}}$",
            f"$||\\vec{{v}}|| = {magnitude}$ units",
            "",
            f"**Final Answer:** ${magnitude}$ units"
        ]

        answer_numeric = magnitude

    elif difficulty == 2:
        # Medium: Vector addition/subtraction - find component
        x1 = random.randint(-5, 5)
        y1 = random.randint(-5, 5)
        x2 = random.randint(-5, 5)
        y2 = random.randint(-5, 5)
        use_word_problem = random.random() < 0.4

        if random.choice([True, False]):
            # Addition
            result_x = x1 + x2
            result_y = y1 + y2
            operation = "+"

            if use_word_problem:
                context = random.choice([p for p in ADDITION_WORD_PROBLEMS if p["operation"] == "+"])
                context_text = context["context"].format(x1=x1, y1=y1, x2=x2, y2=y2)
                question = f"{context_text}\n\n$\\vec{{u}} = \\langle {x1}, {y1} \\rangle$, $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$\n\n{context['question']} (Find the $x$-component.)"
            else:
                question = f"If $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ and $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$, find the $x$-component of $\\vec{{u}} + \\vec{{v}}$."

            steps = [
                "To add vectors, we add corresponding components (component-wise addition):",
                "$\\vec{u} + \\vec{v} = \\langle x_1 + x_2, y_1 + y_2 \\rangle$",
                "",
                f"Calculate each component:",
                f"$\\vec{{u}} + \\vec{{v}} = \\langle {x1} + ({x2}), {y1} + ({y2}) \\rangle$",
                f"$\\vec{{u}} + \\vec{{v}} = \\langle {result_x}, {result_y} \\rangle$",
                "",
                f"The $x$-component of the sum is ${result_x}$.",
                "",
                f"**Final Answer:** ${result_x}$"
            ]

            answer_numeric = result_x
        else:
            # Subtraction
            result_x = x1 - x2
            result_y = y1 - y2
            operation = "-"

            if use_word_problem:
                context = random.choice([p for p in ADDITION_WORD_PROBLEMS if p["operation"] == "-"])
                context_text = context["context"].format(x1=x1, y1=y1, x2=x2, y2=y2)
                question = f"{context_text}\n\n$\\vec{{u}} = \\langle {x1}, {y1} \\rangle$, $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$\n\n{context['question']} (Find the $y$-component.)"
            else:
                question = f"If $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ and $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$, find the $y$-component of $\\vec{{u}} - \\vec{{v}}$."

            steps = [
                "To subtract vectors, we subtract corresponding components (component-wise subtraction):",
                "$\\vec{u} - \\vec{v} = \\langle x_1 - x_2, y_1 - y_2 \\rangle$",
                "",
                f"Calculate each component:",
                f"$\\vec{{u}} - \\vec{{v}} = \\langle {x1} - ({x2}), {y1} - ({y2}) \\rangle$",
                f"$\\vec{{u}} - \\vec{{v}} = \\langle {result_x}, {result_y} \\rangle$",
                "",
                f"The $y$-component of the difference is ${result_y}$.",
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
        use_word_problem = random.random() < 0.4

        dot_product = x1 * x2 + y1 * y2

        if use_word_problem:
            context = random.choice(DOTPRODUCT_WORD_PROBLEMS)
            context_text = context["context"].format(x1=x1, y1=y1, x2=x2, y2=y2)
            question = f"{context_text}\n\n$\\vec{{u}} = \\langle {x1}, {y1} \\rangle$, $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$\n\n{context['question']}"
        else:
            question = f"Find the dot product of $\\vec{{u}} = \\langle {x1}, {y1} \\rangle$ and $\\vec{{v}} = \\langle {x2}, {y2} \\rangle$."

        steps = [
            "The dot product of two vectors $\\vec{u} = \\langle x_1, y_1 \\rangle$ and $\\vec{v} = \\langle x_2, y_2 \\rangle$ is:",
            "$\\vec{u} \\cdot \\vec{v} = x_1 x_2 + y_1 y_2$",
            "",
            "The dot product measures how much two vectors point in the same direction.",
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
