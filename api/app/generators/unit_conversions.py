"""Unit conversions question generator with real-world contexts."""

import random
from typing import Dict, Any, List, Tuple

# Engaging real-world contexts for conversions
CONVERSION_CONTEXTS = {
    "height": [
        "NBA player {name} is {value} {from_unit} tall. How tall is that in {to_unit}?",
        "The Statue of Liberty is {value} {from_unit} tall. Convert to {to_unit}.",
    ],
    "weight": [
        "A newborn puppy weighs {value} {from_unit}. How many {to_unit} is that?",
        "Your luggage weighs {value} {from_unit}. What's that in {to_unit}?",
    ],
    "distance": [
        "The school is {value} {from_unit} away. How many {to_unit} is that?",
        "A marathon is {value} {from_unit}. Express this in {to_unit}.",
    ],
    "cooking": [
        "The recipe needs {value} {from_unit} of milk. How many {to_unit} is that?",
        "You have {value} {from_unit} of flour. Convert to {to_unit}.",
    ],
    "speed": [
        "A cheetah runs at {value} {from_unit}. What's that in {to_unit}?",
        "The speed limit is {value} {from_unit}. Convert to {to_unit}.",
    ],
}

# Famous names for height problems
FAMOUS_HEIGHTS = ["LeBron James", "Shaq", "Michael Jordan", "Kevin Durant", "Yao Ming"]


def generate_unit_conversions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a unit conversion problem.

    Args:
        difficulty: 1 (basic), 2 (multi-step), 3 (rate conversions)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps: List[str] = []

    # Use engaging context 50% of the time
    use_context = random.random() < 0.5

    if difficulty == 1:
        # Basic conversions with categories for context matching
        conversions: List[Tuple[str, str, float, str, str]] = [
            ("inches", "feet", 12, "in to ft", "height"),
            ("feet", "yards", 3, "ft to yd", "distance"),
            ("ounces", "pounds", 16, "oz to lb", "weight"),
            ("cups", "pints", 2, "cups to pt", "cooking"),
            ("pints", "quarts", 2, "pt to qt", "cooking"),
            ("centimeters", "meters", 100, "cm to m", "height"),
            ("grams", "kilograms", 1000, "g to kg", "weight"),
        ]

        from_unit, to_unit, factor, name, category = random.choice(conversions)

        if from_unit in ["inches", "ounces", "cups", "pints", "centimeters", "grams"]:
            # Convert from smaller to larger
            value = random.randint(2, 10) * int(factor)
            answer = value / factor

            if use_context and category in CONVERSION_CONTEXTS:
                template = random.choice(CONVERSION_CONTEXTS[category])
                name = random.choice(FAMOUS_HEIGHTS) if category == "height" else ""
                question = template.format(value=value, from_unit=from_unit, to_unit=to_unit, name=name)
                steps.append(f"**Problem:** {question}")
            else:
                question = f"Convert ${value}$ {from_unit} to {to_unit}"

            steps.append(f"**Conversion factor:** $1$ {to_unit} $= {int(factor)}$ {from_unit}")
            steps.append(f"**Method:** Since we're going from smaller to larger units, divide")
            steps.append(f"${value} \\div {int(factor)} = {answer:.2f}$ {to_unit}")
        else:
            # Convert from larger to smaller
            value = random.randint(2, 10)
            answer = value * factor

            if use_context and category in CONVERSION_CONTEXTS:
                template = random.choice(CONVERSION_CONTEXTS[category])
                name = random.choice(FAMOUS_HEIGHTS) if category == "height" else ""
                question = template.format(value=value, from_unit=from_unit, to_unit=to_unit, name=name)
                steps.append(f"**Problem:** {question}")
            else:
                question = f"Convert ${value}$ {from_unit} to {to_unit}"

            steps.append(f"**Conversion factor:** $1$ {from_unit} $= {int(factor)}$ {to_unit}")
            steps.append(f"**Method:** Since we're going from larger to smaller units, multiply")
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
