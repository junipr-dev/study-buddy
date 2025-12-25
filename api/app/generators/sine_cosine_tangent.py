"""Basic trigonometric ratios question generator."""

import random
import math
from typing import Dict, Any

# Real-world word problem contexts for trigonometric ratios
WORD_PROBLEMS = [
    # Architecture contexts
    {
        "context": "An architect is designing a building. A support beam makes an angle with the ground. To find the height of the wall the beam reaches, knowing the beam length and angle.",
        "scenario": "A construction support beam of {length} feet leans against a building at an angle of {angle}° from the ground.",
        "question": "How high up the building does the beam reach?",
        "setup": "Use sine: sin(angle) = height/hypotenuse"
    },
    # Navigation contexts
    {
        "context": "A ship captain needs to navigate. Using the angle of the stars or landmarks, they determine distances.",
        "scenario": "A ship travels at an angle of {angle}° and travels {length} miles. How far north (vertical component) did it travel?",
        "question": "What is the northward displacement?",
        "setup": "Use sine: vertical = hypotenuse × sin(angle)"
    },
    # Engineering contexts
    {
        "context": "A bridge engineer designs a ramp. The incline angle and length are known, and they need the height difference.",
        "scenario": "A bridge ramp has a length of {length} feet and rises at {angle}° from horizontal.",
        "question": "What is the total height change?",
        "setup": "Use sine for vertical rise"
    },
    # Sports contexts
    {
        "context": "A basketball player shoots from an angle. The trajectory involves understanding the vertical component of motion.",
        "scenario": "A basketball shot travels {length} feet at an angle of {angle}° upward.",
        "question": "What is the vertical height component of the shot?",
        "setup": "Use sine: height = distance × sin(angle)"
    },
    # Shadow problems (sun angle contexts)
    {
        "context": "The sun casts shadows at different times of day. The angle of elevation and shadow length determine object height.",
        "scenario": "A flagpole casts a shadow. The sun's rays make an angle of {angle}° with the ground. A nearby tree is {length} feet away.",
        "question": "How tall is the object if the sun angle is {angle}°?",
        "setup": "Use tangent: tan(angle) = height/distance"
    },
]


def generate_sine_cosine_tangent(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate basic trigonometric ratio problems.

    Args:
        difficulty: 1 (evaluate at standard angles), 2 (solve for angle), 3 (word problems)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Evaluate trig functions at standard angles
        # (degrees, radians_str, sin, cos, tan)
        standard_angles = [
            (0, "0", 0, 1, 0),
            (30, "\\frac{\\pi}{6}", 0.5, math.sqrt(3)/2, 1/math.sqrt(3)),
            (45, "\\frac{\\pi}{4}", math.sqrt(2)/2, math.sqrt(2)/2, 1),
            (60, "\\frac{\\pi}{3}", math.sqrt(3)/2, 0.5, math.sqrt(3)),
            (90, "\\frac{\\pi}{2}", 1, 0, None),  # tan undefined
        ]

        degrees, radian_str, sin_val, cos_val, tan_val = random.choice(standard_angles)
        trig_func = random.choice(['sin', 'cos'] if tan_val is None else ['sin', 'cos', 'tan'])

        if trig_func == 'sin':
            value = sin_val
            if value == 0:
                value_str = "0"
            elif value == 1:
                value_str = "1"
            elif value == 0.5:
                value_str = "\\frac{1}{2}"
            elif value == math.sqrt(2)/2:
                value_str = "\\frac{\\sqrt{2}}{2}"
            elif value == math.sqrt(3)/2:
                value_str = "\\frac{\\sqrt{3}}{2}"
        elif trig_func == 'cos':
            value = cos_val
            if value == 0:
                value_str = "0"
            elif value == 1:
                value_str = "1"
            elif value == 0.5:
                value_str = "\\frac{1}{2}"
            elif value == math.sqrt(2)/2:
                value_str = "\\frac{\\sqrt{2}}{2}"
            elif value == math.sqrt(3)/2:
                value_str = "\\frac{\\sqrt{3}}{2}"
        else:  # tan
            value = tan_val
            if value == 0:
                value_str = "0"
            elif value == 1:
                value_str = "1"
            elif value == 1/math.sqrt(3):
                value_str = "\\frac{1}{\\sqrt{3}} = \\frac{\\sqrt{3}}{3}"
            elif value == math.sqrt(3):
                value_str = "\\sqrt{3}"

        question = f"Evaluate $\\{trig_func}({degrees}°)$."

        steps = [
            f"${degrees}°$ is equivalent to ${radian_str}$ radians",
            f"This is a standard angle on the unit circle",
        ]

        if trig_func == 'sin':
            steps.append(f"$\\sin({degrees}°)$ is the $y$-coordinate on the unit circle")
            steps.append(f"At ${degrees}°$, the $y$-coordinate is ${value_str}$")
        elif trig_func == 'cos':
            steps.append(f"$\\cos({degrees}°)$ is the $x$-coordinate on the unit circle")
            steps.append(f"At ${degrees}°$, the $x$-coordinate is ${value_str}$")
        else:
            steps.append(f"$\\tan({degrees}°) = \\frac{{\\sin({degrees}°)}}{{\\cos({degrees}°)}}$")
            steps.append(f"$\\tan({degrees}°) = {value_str}$")

        steps.append(f"**Final Answer:** ${value_str}$")
        answer_numeric = round(value, 4)

    elif difficulty == 2:
        # Medium: Find the angle given a trig value
        # Use inverse relationships
        angle_values = [
            (30, "\\frac{\\pi}{6}", "sin", 0.5, "\\frac{1}{2}"),
            (30, "\\frac{\\pi}{6}", "cos", math.sqrt(3)/2, "\\frac{\\sqrt{3}}{2}"),
            (45, "\\frac{\\pi}{4}", "sin", math.sqrt(2)/2, "\\frac{\\sqrt{2}}{2}"),
            (45, "\\frac{\\pi}{4}", "cos", math.sqrt(2)/2, "\\frac{\\sqrt{2}}{2}"),
            (60, "\\frac{\\pi}{3}", "sin", math.sqrt(3)/2, "\\frac{\\sqrt{3}}{2}"),
            (60, "\\frac{\\pi}{3}", "cos", 0.5, "\\frac{1}{2}"),
            (0, "0", "sin", 0, "0"),
            (90, "\\frac{\\pi}{2}", "sin", 1, "1"),
            (0, "0", "cos", 1, "1"),
        ]

        degrees, radian_str, func, value, value_str = random.choice(angle_values)

        question = f"Find the angle $\\theta$ (in degrees, where $0° \\leq \\theta \\leq 90°$) such that $\\{func}(\\theta) = {value_str}$."

        steps = [
            f"We need to find $\\theta$ where $\\{func}(\\theta) = {value_str}$",
            "Recall the standard angle values:",
        ]

        if func == "sin":
            steps.append("$\\sin(0°) = 0$, $\\sin(30°) = \\frac{1}{2}$, $\\sin(45°) = \\frac{\\sqrt{2}}{2}$, $\\sin(60°) = \\frac{\\sqrt{3}}{2}$, $\\sin(90°) = 1$")
        else:
            steps.append("$\\cos(0°) = 1$, $\\cos(30°) = \\frac{\\sqrt{3}}{2}$, $\\cos(45°) = \\frac{\\sqrt{2}}{2}$, $\\cos(60°) = \\frac{1}{2}$, $\\cos(90°) = 0$")

        steps.append(f"Comparing with ${value_str}$, we find:")
        steps.append(f"**Final Answer:** $\\theta = {degrees}°$")

        answer_numeric = degrees

    else:
        # Hard: Right triangle word problems
        use_word_problem = random.random() < 0.4  # 40% of time use engaging contexts
        problem_types = ["ladder", "ramp", "height"]
        problem_type = random.choice(problem_types)

        if problem_type == "ladder":
            # Ladder against wall - find height or angle
            length = random.choice([10, 12, 15, 20])
            angle = random.choice([30, 45, 60])

            if angle == 30:
                height = length * 0.5
                height_str = f"{length}/2 = {height}"
            elif angle == 45:
                height = length * math.sqrt(2)/2
                height_str = f"{length} \\cdot \\frac{{\\sqrt{{2}}}}{{2}} \\approx {round(height, 2)}"
            else:  # 60
                height = length * math.sqrt(3)/2
                height_str = f"{length} \\cdot \\frac{{\\sqrt{{3}}}}{{2}} \\approx {round(height, 2)}"

            if use_word_problem:
                question = f"**Construction Problem:** A {length}-foot support beam leans against a building at ${angle}°$ from the ground. This is a common scenario in architecture where engineers need to calculate how high a support structure will reach. How high up the wall does the beam reach?"
            else:
                question = f"A {length}-foot ladder leans against a wall at an angle of ${angle}°$ from the ground. How high up the wall does the ladder reach?"

            steps = [
                f"**Setup:** Draw a right triangle with the {length}-foot beam as the hypotenuse.",
                "The angle of ${angle}°$ is measured from the ground.",
                f"The height we're solving for is the **opposite** side to this angle.",
                "",
                f"**Identify the right trigonometric ratio:**",
                f"We have the hypotenuse ({length} ft) and need the opposite side (height).",
                f"Use sine: $\\sin(\\theta) = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}}$",
                "",
                f"**Apply the formula:**",
                f"$\\sin({angle}°) = \\frac{{h}}{{{length}}}$",
                "",
                f"**Solve for the unknown:**",
                f"Multiply both sides by ${length}$: $h = {length} \\cdot \\sin({angle}°)$",
                "",
                f"**Calculate the result:**",
                f"$h = {height_str}$ feet",
                "",
                f"**Final Answer:** ${round(height, 2)}$ feet"
            ]

            answer_numeric = round(height, 2)

        elif problem_type == "ramp":
            # Wheelchair ramp - find length or angle
            height = random.choice([2, 3, 4])
            angle = random.choice([5, 10, 15])  # ADA compliant angles

            # Using sin(angle) = height/length
            length = height / math.sin(math.radians(angle))

            if use_word_problem:
                question = f"**Accessibility Engineering:** A wheelchair ramp must safely rise ${height}$ feet at an angle of ${angle}°$ (which meets ADA compliance standards). Engineers must calculate the required length to ensure safe accessibility. How long must the ramp be?"
            else:
                question = f"A wheelchair ramp must rise ${height}$ feet at an angle of ${angle}°$. How long must the ramp be?"

            steps = [
                f"**Setup:** The ramp forms a right triangle where:",
                f"- Vertical rise (opposite) = ${height}$ feet",
                f"- Ramp angle from horizontal = ${angle}°$",
                "- Ramp length = hypotenuse (what we're finding)",
                "",
                f"**Identify the right trigonometric ratio:**",
                f"We have the opposite side and need the hypotenuse.",
                f"Use sine: $\\sin(\\theta) = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}}$",
                "",
                f"**Apply the formula:**",
                f"$\\sin({angle}°) = \\frac{{{height}}}{{L}}$",
                "",
                f"**Solve for the unknown:**",
                f"Rearrange: $L = \\frac{{{height}}}{{\\sin({angle}°)}}$",
                "",
                f"**Calculate the result:**",
                f"$L = \\frac{{{height}}}{{\\sin({angle}°)}} \\approx {round(length, 2)}$ feet",
                "",
                f"**Final Answer:** ${round(length, 2)}$ feet"
            ]

            answer_numeric = round(length, 2)

        else:  # height
            # Tree height from distance and angle (or building, flagpole, etc.)
            distance = random.choice([30, 40, 50, 60])
            angle = random.choice([30, 45, 60])

            if angle == 30:
                height = distance / math.sqrt(3)
                height_str = f"{distance}/\\sqrt{{3}} \\approx {round(height, 2)}"
            elif angle == 45:
                height = distance
                height_str = f"{distance}"
            else:  # 60
                height = distance * math.sqrt(3)
                height_str = f"{distance}\\sqrt{{3}} \\approx {round(height, 2)}"

            if use_word_problem:
                question = f"**Surveying Problem:** A surveyor stands ${distance}$ feet away from the base of a building or tree. Using a surveying instrument, they measure the angle of elevation to the top as ${angle}°$. This angle measurement is a fundamental technique in land surveying and construction. How tall is the structure?"
            else:
                question = f"From a point ${distance}$ feet from the base of a tree, the angle of elevation to the top is ${angle}°$. How tall is the tree?"

            steps = [
                f"**Setup:** The observer, tree base, and tree top form a right triangle where:",
                f"- Distance from tree (adjacent) = ${distance}$ feet",
                "- Tree height (opposite) = unknown",
                f"- Angle of elevation = ${angle}°$ (angle looking up from horizontal)",
                "",
                f"**Identify the right trigonometric ratio:**",
                f"We have the adjacent side and need the opposite side.",
                f"Use tangent: $\\tan(\\theta) = \\frac{{\\text{{opposite}}}}{{\\text{{adjacent}}}}$",
                "",
                f"**Apply the formula:**",
                f"$\\tan({angle}°) = \\frac{{h}}{{{distance}}}$",
                "",
                f"**Solve for the unknown:**",
                f"Multiply both sides by ${distance}$: $h = {distance} \\cdot \\tan({angle}°)$",
                "",
                f"**Calculate the result:**",
                f"$h = {height_str}$ feet",
                "",
                f"**Final Answer:** ${round(height, 2)}$ feet"
            ]

            answer_numeric = round(height, 2)

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
