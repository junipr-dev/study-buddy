"""Graphing trigonometric functions question generator."""

import random
import math
from typing import Dict, Any


def generate_graphing_trig_functions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate problems about graphing trigonometric functions.

    Args:
        difficulty: 1 (identify properties), 2 (amplitude/period), 3 (transformations)

    Returns:
        Dict with question, answer, and solution steps
    """
    if difficulty == 1:
        # Easy: Identify amplitude, period, or midline of basic trig functions
        func_type = random.choice(['sin', 'cos'])
        property_type = random.choice(['amplitude', 'period', 'midline'])

        if property_type == 'amplitude':
            A = random.choice([2, 3, 4, 5])

            question = f"What is the amplitude of the function $y = {A}\\{func_type}(x)$?"

            steps = [
                f"The general form is $y = A\\{func_type}(x)$, where $A$ is the amplitude",
                f"In this case, $A = {A}$",
                "The amplitude is the absolute value of $A$",
                f"**Final Answer:** Amplitude = ${A}$"
            ]

            answer_numeric = A

        elif property_type == 'period':
            B = random.choice([2, 3, 4])
            period = 2 * math.pi / B

            question = f"What is the period of the function $y = \\{func_type}({B}x)$?"

            steps = [
                f"The general form is $y = \\{func_type}(Bx)$, where the period is $\\frac{{2\\pi}}{{B}}$",
                f"In this case, $B = {B}$",
                f"Period = $\\frac{{2\\pi}}{{{B}}}$",
                f"**Final Answer:** Period = $\\frac{{2\\pi}}{{{B}}}$ $\\approx {round(period, 2)}$"
            ]

            answer_numeric = round(period, 2)

        else:  # midline
            D = random.choice([-3, -2, -1, 1, 2, 3])

            question = f"What is the midline of the function $y = \\{func_type}(x) + {D}$?" if D > 0 else f"What is the midline of the function $y = \\{func_type}(x) - {abs(D)}$?"

            steps = [
                f"The general form is $y = \\{func_type}(x) + D$, where $y = D$ is the midline",
                f"In this case, $D = {D}$",
                "The midline is the horizontal line the function oscillates around",
                f"**Final Answer:** Midline is $y = {D}$"
            ]

            answer_numeric = D

    elif difficulty == 2:
        # Medium: Given function with amplitude and period changes, find properties
        func_type = random.choice(['sin', 'cos'])
        A = random.choice([2, 3, 4])
        B = random.choice([2, 3, 4])

        period = 2 * math.pi / B

        question = f"For the function $y = {A}\\{func_type}({B}x)$, find the amplitude and period."

        steps = [
            f"The general form is $y = A\\{func_type}(Bx)$",
            f"where amplitude = $|A|$ and period = $\\frac{{2\\pi}}{{B}}$",
            "",
            "**Finding Amplitude:**",
            f"$A = {A}$, so amplitude = ${A}$",
            "",
            "**Finding Period:**",
            f"$B = {B}$",
            f"Period = $\\frac{{2\\pi}}{{{B}}}$",
            f"Period $\\approx {round(period, 2)}$",
            "",
            f"**Final Answer:** Amplitude = ${A}$, Period = $\\frac{{2\\pi}}{{{B}}}$ $\\approx {round(period, 2)}$"
        ]

        answer_numeric = A  # Return amplitude as the numeric answer

    else:
        # Hard: Full transformation with amplitude, period, phase shift, and vertical shift
        func_type = random.choice(['sin', 'cos'])
        A = random.choice([2, 3])
        B = random.choice([2, 4])
        C = random.choice([1, 2]) * (math.pi / 4)  # Phase shift in terms of pi
        D = random.choice([-2, -1, 1, 2])

        # Format phase shift nicely
        if C == math.pi / 4:
            C_str = "\\frac{\\pi}{4}"
            phase_str = "\\frac{\\pi}{4}"
            phase_value = math.pi / 4
        elif C == math.pi / 2:
            C_str = "\\frac{\\pi}{2}"
            phase_str = "\\frac{\\pi}{2}"
            phase_value = math.pi / 2
        else:
            C_str = str(C)
            phase_str = str(C)
            phase_value = C

        # Calculate actual phase shift (horizontal shift)
        horizontal_shift = C / B
        period = 2 * math.pi / B

        if D > 0:
            D_str = f"+ {D}"
        else:
            D_str = f"- {abs(D)}"

        question = f"Identify all transformations of the function $y = {A}\\{func_type}({B}x - {C_str}) {D_str}$."

        steps = [
            f"The general form is $y = A\\{func_type}(B(x - C)) + D$",
            f"where:",
            "- $A$ = amplitude",
            "- $B$ affects the period: period = $\\frac{2\\pi}{B}$",
            "- $C$ = horizontal (phase) shift",
            "- $D$ = vertical shift (midline)",
            "",
            "**Identifying values:**",
            f"Rewrite: $y = {A}\\{func_type}({B}(x - {phase_str}/{B})) {D_str}$",
            "",
            f"- Amplitude: $|A| = {A}$",
            f"- Period: $\\frac{{2\\pi}}{{{B}}}$ = $\\frac{{\\pi}}{{{B//2}}}$ $\\approx {round(period, 2)}$",
            f"- Phase shift: ${phase_str}/{B}$ units to the right",
            f"- Vertical shift: ${D}$ (midline at $y = {D}$)",
            "",
            f"**Final Answer:** Amplitude = ${A}$, Period = $\\frac{{2\\pi}}{{{B}}}$, Phase shift = ${phase_str}/{B}$, Midline = $y = {D}$"
        ]

        answer_numeric = A  # Return amplitude as the numeric answer

    return {
        "question": question,
        "answer": str(answer_numeric),
        "answer_numeric": answer_numeric,
        "steps": steps,
        "difficulty": difficulty,
    }
