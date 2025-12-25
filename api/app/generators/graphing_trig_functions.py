"""Graphing trigonometric functions question generator."""

import random
import math
from typing import Dict, Any

# Real-world contexts for trigonometric graph transformations
WORD_PROBLEMS = [
    {
        "context": "Sound waves and music production rely on sine waves with different amplitudes and frequencies.",
        "application": "Adjusting volume (amplitude) and pitch (frequency) of audio signals"
    },
    {
        "context": "Seasonal temperature variation can be modeled as a shifted and scaled sine function.",
        "application": "Climate modeling: representing annual temperature cycles"
    },
    {
        "context": "Ocean tides follow a predictable pattern that can be modeled with trigonometric functions.",
        "application": "Predicting tide heights and times for navigation and marine activities"
    },
    {
        "context": "Pendulum motion in clocks and physics experiments creates periodic oscillations.",
        "application": "Understanding periodic motion in mechanical systems"
    },
    {
        "context": "Ferris wheels, wheels, and rotating machinery create repeating height patterns.",
        "application": "Engineering rotating systems with predictable positions"
    },
]


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
        use_word_problem = random.random() < 0.4
        func_type = random.choice(['sin', 'cos'])
        property_type = random.choice(['amplitude', 'period', 'midline'])

        if property_type == 'amplitude':
            A = random.choice([2, 3, 4, 5])

            if use_word_problem:
                question = f"**Audio Engineering:** A sound wave is modeled by $y = {A}\\{func_type}(x)$, where $y$ represents the speaker displacement (in mm) and $x$ represents time. The amplitude determines the volume level. What is the amplitude of this wave?"
            else:
                question = f"What is the amplitude of the function $y = {A}\\{func_type}(x)$?"

            steps = [
                f"**Identify the form:** The function is $y = A\\{func_type}(x)$",
                f"In this standard form, $A$ is the **amplitude coefficient**.",
                "",
                f"**Extract the value:** $A = {A}$",
                "",
                f"**Interpret amplitude:** The amplitude is the distance from the centerline to the peak (or trough).",
                f"It's always the absolute value of $A$: $|A| = |{A}| = {A}$",
                "",
                f"This means the wave oscillates {A} units above and below the midline.",
                f"**Final Answer:** Amplitude = ${A}$ units"
            ]

            answer_numeric = A

        elif property_type == 'period':
            use_word_problem = random.random() < 0.4
            B = random.choice([2, 3, 4])
            period = 2 * math.pi / B

            if use_word_problem:
                question = f"**Ocean Tides:** A tide model uses $y = \\{func_type}({B}x)$, where $x$ is measured in hours and one complete tide cycle includes both high and low tides. What is the period (in hours) of one complete cycle?"
            else:
                question = f"What is the period of the function $y = \\{func_type}({B}x)$?"

            steps = [
                f"**Identify the form:** The function is $y = \\{func_type}(Bx)$",
                f"The coefficient $B$ affects how quickly the function repeats.",
                "",
                f"**Period formula:** Period = $\\frac{{2\\pi}}{{|B|}}$",
                f"This formula tells us how long it takes for one complete cycle.",
                "",
                f"**Apply the values:** $B = {B}$",
                f"Period = $\\frac{{2\\pi}}{{{B}}}$",
                "",
                f"**Calculate:** $\\frac{{2\\pi}}{{{B}}} \\approx {round(period, 2)}$ units",
                "",
                f"This means the function completes one full cycle every $\\frac{{2\\pi}}{{{B}}}$ units.",
                f"**Final Answer:** Period = $\\frac{{2\\pi}}{{{B}}}$ (approximately {round(period, 2)} units)"
            ]

            answer_numeric = round(period, 2)

        else:  # midline
            use_word_problem = random.random() < 0.4
            D = random.choice([-3, -2, -1, 1, 2, 3])

            if D > 0:
                question_func = f"$y = \\{func_type}(x) + {D}$"
            else:
                question_func = f"$y = \\{func_type}(x) - {abs(D)}$"

            if use_word_problem:
                question = f"**Temperature Cycles:** Annual temperature can be modeled by $y = {D + 10}\\{func_type}(x) + {D + 50}$, where the midline represents the average temperature. What is the midline (in degrees) for {question_func}?"
            else:
                question = f"What is the midline of the function {question_func}?"

            steps = [
                f"**Identify the form:** The function is $y = \\{func_type}(x) + D$",
                f"In this form, $D$ is called the **vertical shift**.",
                "",
                f"**Extract the value:** $D = {D}$",
                "",
                f"**Understand midline:** The midline is the horizontal line around which the function oscillates.",
                f"It's also called the **center line** or **equilibrium position**.",
                "",
                f"**Locate it:** Since the vertical shift is $D = {D}$,",
                f"the midline is at $y = {D}$",
                "",
                f"The function oscillates equally above and below this line.",
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
