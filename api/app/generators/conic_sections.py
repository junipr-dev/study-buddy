"""Conic sections question generator."""

import random
import math
from typing import Dict, Any


def generate_conic_sections(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a conic sections problem.

    Args:
        difficulty: 1 (circle center/radius), 2 (ellipse/parabola), 3 (hyperbola)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Find radius or center coordinate of a circle
        h = random.randint(-5, 5)
        k = random.randint(-5, 5)
        r = random.randint(2, 6)

        if random.choice([True, False]):
            # Find radius
            question = f"Find the radius of the circle with equation $(x {-h:+d})^2 + (y {-k:+d})^2 = {r**2}$."

            steps = [
                "The standard form of a circle is $(x - h)^2 + (y - k)^2 = r^2$",
                "where $(h, k)$ is the center and $r$ is the radius.",
                "",
                f"From the equation $(x {-h:+d})^2 + (y {-k:+d})^2 = {r**2}$:",
                f"- $r^2 = {r**2}$",
                "",
                f"Take the square root: $r = \\sqrt{{{r**2}}} = {r}$",
                "",
                f"**Final Answer:** ${r}$"
            ]

            answer_numeric = r
        else:
            # Find x-coordinate of center
            question = f"Find the $x$-coordinate of the center of the circle with equation $(x {-h:+d})^2 + (y {-k:+d})^2 = {r**2}$."

            steps = [
                "The standard form of a circle is $(x - h)^2 + (y - k)^2 = r^2$",
                "where $(h, k)$ is the center and $r$ is the radius.",
                "",
                f"From the equation $(x {-h:+d})^2 + (y {-k:+d})^2 = {r**2}$:",
            ]

            if h >= 0:
                steps.append(f"- $(x - ({h}))^2$ means $h = {h}$")
            else:
                steps.append(f"- $(x - ({h}))^2 = (x + {-h})^2$ means $h = {h}$")

            steps.extend([
                "",
                f"The center is at $({h}, {k})$.",
                f"The $x$-coordinate is ${h}$.",
                "",
                f"**Final Answer:** ${h}$"
            ])

            answer_numeric = h

    elif difficulty == 2:
        # Medium: Ellipse or Parabola
        if random.choice([True, False]):
            # Ellipse: Find semi-major axis length
            a = random.randint(4, 7)
            b = random.randint(2, a - 1)
            h = random.randint(-3, 3)
            k = random.randint(-3, 3)

            # a > b, so a is semi-major axis
            question = f"Find the length of the semi-major axis of the ellipse $\\frac{{(x {-h:+d})^2}}{{{a**2}}} + \\frac{{(y {-k:+d})^2}}{{{b**2}}} = 1$."

            steps = [
                "The standard form of an ellipse is $\\frac{{(x-h)^2}}{{a^2}} + \\frac{{(y-k)^2}}{{b^2}} = 1$",
                "",
                f"From the equation: $a^2 = {a**2}$ and $b^2 = {b**2}$",
                "",
                f"Taking square roots: $a = {a}$ and $b = {b}$",
                "",
                f"Since ${a} > {b}$, the semi-major axis is $a = {a}$.",
                "",
                f"**Final Answer:** ${a}$"
            ]

            answer_numeric = a
        else:
            # Parabola: vertex form, find vertex coordinate
            h = random.randint(-4, 4)
            k = random.randint(-4, 4)
            a = random.choice([1, 2, 3, 4, -1, -2, -3, -4])

            question = f"Find the $y$-coordinate of the vertex of the parabola $y = {a}(x {-h:+d})^2 {k:+d}$."

            steps = [
                "The vertex form of a parabola is $y = a(x - h)^2 + k$",
                "where $(h, k)$ is the vertex.",
                "",
                f"From the equation $y = {a}(x {-h:+d})^2 {k:+d}$:",
                f"- The vertex is at $({h}, {k})$",
                "",
                f"The $y$-coordinate is ${k}$.",
                "",
                f"**Final Answer:** ${k}$"
            ]

            answer_numeric = k

    else:
        # Hard: Hyperbola
        # Standard form: (x-h)²/a² - (y-k)²/b² = 1
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        h = random.randint(-3, 3)
        k = random.randint(-3, 3)

        # For hyperbola, vertices are at (h±a, k)
        # Distance between vertices is 2a
        vertex_distance = 2 * a

        question = f"Find the distance between the vertices of the hyperbola $\\frac{{(x {-h:+d})^2}}{{{a**2}}} - \\frac{{(y {-k:+d})^2}}{{{b**2}}} = 1$."

        steps = [
            "The standard form of a horizontal hyperbola is $\\frac{{(x-h)^2}}{{a^2}} - \\frac{{(y-k)^2}}{{b^2}} = 1$",
            "",
            f"From the equation: $a^2 = {a**2}$, so $a = {a}$",
            "",
            f"For a horizontal hyperbola, the vertices are at $(h \\pm a, k)$:",
            f"- Vertex 1: $({h} - {a}, {k}) = ({h - a}, {k})$",
            f"- Vertex 2: $({h} + {a}, {k}) = ({h + a}, {k})$",
            "",
            "The distance between vertices is $2a$:",
            f"Distance $= 2 \\times {a} = {vertex_distance}$",
            "",
            f"**Final Answer:** ${vertex_distance}$"
        ]

        answer_numeric = vertex_distance

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
