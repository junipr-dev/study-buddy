"""Unit conversions question generator."""

import random
from typing import Dict, Any, List, Tuple


def generate_unit_conversions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a unit conversion problem.

    Args:
        difficulty: 1 (basic), 2 (multi-step), 3 (rate conversions)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps: List[str] = []

    if difficulty == 1:
        # Basic conversions
        conversions: List[Tuple[str, str, float, str]] = [
            ("inches", "feet", 12, "in to ft"),
            ("feet", "yards", 3, "ft to yd"),
            ("ounces", "pounds", 16, "oz to lb"),
            ("cups", "pints", 2, "cups to pt"),
            ("pints", "quarts", 2, "pt to qt"),
            ("centimeters", "meters", 100, "cm to m"),
            ("grams", "kilograms", 1000, "g to kg"),
        ]

        from_unit, to_unit, factor, name = random.choice(conversions)

        if from_unit in ["inches", "ounces", "cups", "pints", "centimeters", "grams"]:
            # Convert from smaller to larger
            value = random.randint(2, 10) * int(factor)
            answer = value / factor
            question = f"Convert ${value}$ {from_unit} to {to_unit}"

            steps.append(f"Conversion: $1$ {to_unit} $= {int(factor)}$ {from_unit}")
            steps.append(f"Divide ${value}$ by ${int(factor)}$:")
            steps.append(f"${value} \\div {int(factor)} = {answer:.2f}$ {to_unit}")
        else:
            # Convert from larger to smaller
            value = random.randint(2, 10)
            answer = value * factor
            question = f"Convert ${value}$ {from_unit} to {to_unit}"

            steps.append(f"Conversion: $1$ {from_unit} $= {int(factor)}$ {to_unit}")
            steps.append(f"Multiply ${value}$ by ${int(factor)}$:")
            steps.append(f"${value} \\times {int(factor)} = {int(answer)}$ {to_unit}")

    elif difficulty == 2:
        # Multi-step conversions
        conversions = [
            ("yards", "inches", [("yards", "feet", 3), ("feet", "inches", 12)]),
            ("miles", "feet", [("miles", "feet", 5280)]),
            ("kilograms", "grams", [("kilograms", "grams", 1000)]),
            ("meters", "centimeters", [("meters", "centimeters", 100)]),
        ]

        from_unit, to_unit, conversion_steps = random.choice(conversions)
        value = random.randint(2, 8)

        question = f"Convert ${value}$ {from_unit} to {to_unit}"

        steps.append(f"Convert ${value}$ {from_unit} to {to_unit}")

        current_value = value
        for step_from, step_to, factor in conversion_steps:
            steps.append(f"$1$ {step_from} $= {factor}$ {step_to}")
            current_value = current_value * factor
            steps.append(f"${value}$ {from_unit} $= {value} \\times {factor} = {current_value}$ {step_to}")

        answer = current_value

    else:
        # Rate conversions
        rate_conversions = [
            {
                "from": "60 mph",
                "to": "feet per second",
                "from_val": 60,
                "from_unit": "miles per hour",
                "steps_data": [
                    ("miles to feet", 5280),
                    ("hours to seconds", 3600),
                ],
            },
            {
                "from": "30 meters per second",
                "to": "kilometers per hour",
                "from_val": 30,
                "from_unit": "meters per second",
                "steps_data": [
                    ("meters to kilometers", 1/1000),
                    ("seconds to hours", 3600),
                ],
            },
        ]

        conversion = random.choice(rate_conversions)
        from_val = conversion["from_val"]
        from_display = conversion["from"]
        to_unit = conversion["to"]

        question = f"Convert ${from_display}$ to {to_unit}"

        steps.append(f"Convert ${from_display}$ to {to_unit}")

        if "mph" in from_display:
            # mph to ft/s
            steps.append(f"Convert miles to feet: $1$ mile $= 5280$ feet")
            feet_per_hour = from_val * 5280
            steps.append(f"${from_val}$ miles/hour $= {feet_per_hour}$ feet/hour")
            steps.append(f"Convert hours to seconds: $1$ hour $= 3600$ seconds")
            steps.append(f"$\\frac{{{feet_per_hour} \\text{{ ft}}}}{{1 \\text{{ hr}}}} \\times \\frac{{1 \\text{{ hr}}}}{{3600 \\text{{ sec}}}} = \\frac{{{feet_per_hour}}}{{3600}}$ ft/sec")
            answer = feet_per_hour / 3600
            steps.append(f"$= {answer:.2f}$ feet per second")
        else:
            # m/s to km/h
            steps.append(f"Convert meters to kilometers: $1$ km $= 1000$ m")
            km_per_second = from_val / 1000
            steps.append(f"${from_val}$ m/s $= {km_per_second}$ km/s")
            steps.append(f"Convert seconds to hours: $1$ hour $= 3600$ seconds")
            steps.append(f"${km_per_second}$ km/s $\\times 3600$ s/hr $= {km_per_second * 3600}$ km/hr")
            answer = km_per_second * 3600

    steps.append(f"**Final Answer:** ${answer:.2f}$ {to_unit if difficulty != 1 else ''}")

    return {
        "question": question,
        "answer": f"{answer:.2f}",
        "answer_numeric": round(answer, 2),
        "steps": steps,
        "difficulty": difficulty,
    }
