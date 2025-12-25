"""Conic sections question generator."""

import random
import math
from typing import Dict, Any

# Word problem templates for engaging, real-world contexts
CIRCLE_WORD_PROBLEMS = [
    {
        "context": "A circular swimming pool has a center at ({h}, {k}) and a radius of {r} meters.",
        "question_template": "What is the radius of the swimming pool?",
        "equation_desc": "You need to write the equation and identify the radius."
    },
    {
        "context": "A satellite dish's circular reflector is centered at ({h}, {k}) meters from the ground station.",
        "question_template": "What is the x-coordinate of the dish's center?",
        "equation_desc": "The dish's boundary equation is given."
    }
]

PARABOLA_WORD_PROBLEMS = [
    {
        "context": "A parabolic mirror focuses light to its vertex for maximum reflection.",
        "question_template": "What is the y-coordinate of the vertex, where light is most focused?",
        "equation_desc": "The mirror's profile follows a parabola."
    },
    {
        "context": "An arched stadium roof follows a parabolic shape with vertex at ({h}, {k}).",
        "question_template": "What is the height of the highest point in the stadium?",
        "equation_desc": "Find the y-coordinate of the vertex."
    }
]

ELLIPSE_WORD_PROBLEMS = [
    {
        "context": "A satellite orbits Earth in an elliptical path with semi-major axis of {a} million km.",
        "question_template": "What is the length of the orbital path along the major axis?",
        "equation_desc": "The semi-major axis length determines orbital characteristics."
    },
    {
        "context": "An Olympic stadium track is elliptical with a major axis spanning {a} meters.",
        "question_template": "What is the semi-major axis length?",
        "equation_desc": "The track dimensions match the ellipse equation."
    }
]

HYPERBOLA_WORD_PROBLEMS = [
    {
        "context": "A navigation system uses hyperbolic curves to locate ships at sea. The system's reference points are {2*a} units apart.",
        "question_template": "What is the distance between the two navigation reference points?",
        "equation_desc": "Hyperbolic geometry helps determine position accurately."
    },
    {
        "context": "A cooling tower uses a hyperbolic cross-section for structural efficiency, with vertices {2*a} meters apart.",
        "question_template": "What is the distance between the narrowest points of the tower?",
        "equation_desc": "The hyperbola's vertices determine the structural spacing."
    }
]


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
        use_word_problem = random.random() < 0.4

        if random.choice([True, False]):
            # Find radius
            if use_word_problem:
                context = random.choice(CIRCLE_WORD_PROBLEMS)
                context_text = context["context"].format(h=h, k=k, r=r)
                question = f"{context_text}\n\nThe equation of the circle is $(x {-h:+d})^2 + (y {-k:+d})^2 = {r**2}$.\n\n{context['question_template']}"
            else:
                question = f"Find the radius of the circle with equation $(x {-h:+d})^2 + (y {-k:+d})^2 = {r**2}$."

            steps = [
                "The standard form of a circle is $(x - h)^2 + (y - k)^2 = r^2$",
                "where $(h, k)$ is the center and $r$ is the radius.",
                "",
                f"From the equation $(x {-h:+d})^2 + (y {-k:+d})^2 = {r**2}$, we can identify $r^2 = {r**2}$.",
                "",
                f"Taking the square root of both sides: $r = \\sqrt{{{r**2}}} = {r}$",
                "",
                f"**Final Answer:** ${r}$ units"
            ]

            answer_numeric = r
        else:
            # Find x-coordinate of center
            if use_word_problem:
                context = random.choice(CIRCLE_WORD_PROBLEMS)
                context_text = context["context"].format(h=h, k=k, r=r)
                question = f"{context_text}\n\nThe equation of the circle is $(x {-h:+d})^2 + (y {-k:+d})^2 = {r**2}$.\n\n{context['question_template']}"
            else:
                question = f"Find the $x$-coordinate of the center of the circle with equation $(x {-h:+d})^2 + (y {-k:+d})^2 = {r**2}$."

            steps = [
                "The standard form of a circle is $(x - h)^2 + (y - k)^2 = r^2$",
                "where $(h, k)$ is the center and $r$ is the radius.",
                "",
                f"In our equation $(x {-h:+d})^2 + (y {-k:+d})^2 = {r**2}$, we need to identify the center.",
            ]

            if h >= 0:
                steps.append(f"The term $(x - {h})^2$ tells us the $x$-coordinate of the center is $h = {h}$")
            else:
                steps.append(f"The term $(x - ({h}))^2 = (x + {-h})^2$ tells us the $x$-coordinate of the center is $h = {h}$")

            steps.extend([
                "",
                f"The center is located at $({h}, {k})$.",
                f"Therefore, the $x$-coordinate is ${h}$.",
                "",
                f"**Final Answer:** ${h}$"
            ])

            answer_numeric = h

    elif difficulty == 2:
        # Medium: Ellipse or Parabola
        use_word_problem = random.random() < 0.4

        if random.choice([True, False]):
            # Ellipse: Find semi-major axis length
            a = random.randint(4, 7)
            b = random.randint(2, a - 1)
            h = random.randint(-3, 3)
            k = random.randint(-3, 3)

            # a > b, so a is semi-major axis
            if use_word_problem:
                context = random.choice(ELLIPSE_WORD_PROBLEMS)
                context_text = context["context"].format(a=a, b=b, h=h, k=k)
                question = f"{context_text}\n\nThe ellipse equation is $\\frac{{(x {-h:+d})^2}}{{{a**2}}} + \\frac{{(y {-k:+d})^2}}{{{b**2}}} = 1$.\n\n{context['question_template']}"
            else:
                question = f"Find the length of the semi-major axis of the ellipse $\\frac{{(x {-h:+d})^2}}{{{a**2}}} + \\frac{{(y {-k:+d})^2}}{{{b**2}}} = 1$."

            steps = [
                "The standard form of an ellipse is $\\frac{{(x-h)^2}}{{a^2}} + \\frac{{(y-k)^2}}{{b^2}} = 1$",
                "where $a$ is the semi-major axis and $b$ is the semi-minor axis.",
                "",
                f"From the equation: $a^2 = {a**2}$ and $b^2 = {b**2}$",
                "",
                f"Taking square roots: $a = {a}$ and $b = {b}$",
                "",
                f"Since ${a} > {b}$, the longer axis is the major axis.",
                f"The semi-major axis has length $a = {a}$ units.",
                "",
                f"**Final Answer:** ${a}$ units"
            ]

            answer_numeric = a
        else:
            # Parabola: vertex form, find vertex coordinate
            h = random.randint(-4, 4)
            k = random.randint(-4, 4)
            a = random.choice([1, 2, 3, 4, -1, -2, -3, -4])

            if use_word_problem:
                context = random.choice(PARABOLA_WORD_PROBLEMS)
                context_text = context["context"].format(h=h, k=k, a=abs(a))
                question = f"{context_text}\n\nThe parabola equation is $y = {a}(x {-h:+d})^2 {k:+d}$.\n\n{context['question_template']}"
            else:
                question = f"Find the $y$-coordinate of the vertex of the parabola $y = {a}(x {-h:+d})^2 {k:+d}$."

            steps = [
                "The vertex form of a parabola is $y = a(x - h)^2 + k$",
                "where $(h, k)$ is the vertex (the turning point).",
                "",
                f"From the equation $y = {a}(x {-h:+d})^2 {k:+d}$:",
                f"We can identify that the vertex is located at $({h}, {k})$.",
                "",
                f"The $y$-coordinate of the vertex is ${k}$.",
                "",
                f"**Final Answer:** ${k}$ units"
            ]

            answer_numeric = k

    else:
        # Hard: Hyperbola
        # Standard form: (x-h)²/a² - (y-k)²/b² = 1
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        h = random.randint(-3, 3)
        k = random.randint(-3, 3)
        use_word_problem = random.random() < 0.4

        # For hyperbola, vertices are at (h±a, k)
        # Distance between vertices is 2a
        vertex_distance = 2 * a

        if use_word_problem:
            context = random.choice(HYPERBOLA_WORD_PROBLEMS)
            context_text = context["context"].format(h=h, k=k, a=a)
            question = f"{context_text}\n\nThe hyperbola equation is $\\frac{{(x {-h:+d})^2}}{{{a**2}}} - \\frac{{(y {-k:+d})^2}}{{{b**2}}} = 1$.\n\n{context['question_template']}"
        else:
            question = f"Find the distance between the vertices of the hyperbola $\\frac{{(x {-h:+d})^2}}{{{a**2}}} - \\frac{{(y {-k:+d})^2}}{{{b**2}}} = 1$."

        steps = [
            "The standard form of a horizontal hyperbola is $\\frac{{(x-h)^2}}{{a^2}} - \\frac{{(y-k)^2}}{{b^2}} = 1$",
            "The vertices are the closest points on each branch to the center.",
            "",
            f"From the equation: $a^2 = {a**2}$, so $a = {a}$",
            "",
            f"For a horizontal hyperbola, the vertices are at $(h \\pm a, k)$:",
            f"- Left vertex: $({h} - {a}, {k}) = ({h - a}, {k})$",
            f"- Right vertex: $({h} + {a}, {k}) = ({h + a}, {k})$",
            "",
            "The distance between the two vertices is:",
            f"Distance $= 2a = 2 \\times {a} = {vertex_distance}$ units",
            "",
            f"**Final Answer:** ${vertex_distance}$ units"
        ]

        answer_numeric = vertex_distance

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
