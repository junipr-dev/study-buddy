"""Evaluating algebraic expressions question generator with real-world contexts."""

import random
from typing import Dict, Any

# Real-world contexts for evaluating expressions
EXPRESSION_CONTEXTS = [
    {"formula": "{a}x + {b}", "context": "cost", "question": "A phone plan costs ${b} per month plus ${a} per gigabyte of data. If you use {x} GB, what's your total bill?"},
    {"formula": "{a}x + {b}", "context": "earning", "question": "You earn ${a} per hour plus a ${b} bonus. How much do you make working {x} hours?"},
    {"formula": "{a}x + {b}", "context": "taxi", "question": "A taxi charges ${b} flat fee plus ${a} per mile. What's the cost for a {x}-mile trip?"},
    {"formula": "{a}x + {b}", "context": "temperature", "question": "To convert Celsius to Fahrenheit-ish, multiply by {a} and add {b}. What's {x}°C in this scale?"},
]

TWO_VAR_CONTEXTS = [
    {"formula": "{a}x + {b}y", "context": "shopping", "question": "Apples cost ${a} each and oranges cost ${b} each. How much for {x} apples and {y} oranges?"},
    {"formula": "{a}x + {b}y", "context": "points", "question": "In a game, goals are worth {a} points and assists are worth {b} points. What's the score with {x} goals and {y} assists?"},
]


def generate_evaluating_expressions(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate an evaluating expressions problem.

    Args:
        difficulty:
            1 (easy - single variable, simple operations)
            2 (medium - two variables, more complex operations)
            3 (hard - multiple variables with exponents)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []
    use_context = random.random() < 0.5

    if difficulty == 1:
        # Easy: Single variable with simple operations
        # Format: ax + b where x = value
        a = random.randint(2, 9)
        b = random.randint(1, 15)
        x_val = random.randint(1, 10)

        expression = f"{a}x + {b}"

        if use_context:
            ctx = random.choice(EXPRESSION_CONTEXTS)
            question = ctx["question"].format(a=a, b=b, x=x_val)
            steps.append(f"**Problem:** {question}")
            steps.append(f"**Expression:** ${expression}$ where $x = {x_val}$")
        else:
            steps.append(f"Evaluate the expression: ${expression}$ when $x = {x_val}$")

        steps.append("**Rule:** Substitute the given value for the variable, then simplify")
        steps.append(f"Substitute $x = {x_val}$ into the expression:")
        steps.append(f"${a}({x_val}) + {b}$")

        term1 = a * x_val
        steps.append(f"Multiply: ${a} \\times {x_val} = {term1}$")
        steps.append(f"Expression becomes: ${term1} + {b}$")

        answer = term1 + b
        steps.append(f"Add: ${term1} + {b} = {answer}$")

    elif difficulty == 2:
        # Medium: Two variables or exponents
        # Format: ax + by or ax^2 + b
        if random.choice([True, False]):
            # Two variables: ax + by
            a = random.randint(2, 8)
            b = random.randint(2, 8)
            x_val = random.randint(1, 8)
            y_val = random.randint(1, 8)

            expression = f"{a}x + {b}y"

            if use_context:
                ctx = random.choice(TWO_VAR_CONTEXTS)
                question = ctx["question"].format(a=a, b=b, x=x_val, y=y_val)
                steps.append(f"**Problem:** {question}")
                steps.append(f"**Expression:** ${expression}$ where $x = {x_val}$, $y = {y_val}$")
            else:
                steps.append(f"Evaluate the expression: ${expression}$ when $x = {x_val}$ and $y = {y_val}$")

            steps.append("**Rule:** Substitute the given values for each variable, then simplify")
            steps.append(f"Substitute $x = {x_val}$ and $y = {y_val}$:")
            steps.append(f"${a}({x_val}) + {b}({y_val})$")

            term1 = a * x_val
            term2 = b * y_val
            steps.append(f"Multiply each term:")
            steps.append(f"${a} \\times {x_val} = {term1}$")
            steps.append(f"${b} \\times {y_val} = {term2}$")
            steps.append(f"Expression becomes: ${term1} + {term2}$")

            answer = term1 + term2
            steps.append(f"Add: ${term1} + {term2} = {answer}$")
        else:
            # Exponent: ax^2 + b
            a = random.randint(1, 6)
            b = random.randint(1, 12)
            x_val = random.randint(2, 6)

            expression = f"{a}x^2 + {b}"
            steps.append(f"Evaluate the expression: ${expression}$ when $x = {x_val}$")
            steps.append("**Rule:** Substitute the value and follow order of operations (exponents before multiplication)")
            steps.append(f"Substitute $x = {x_val}$:")
            steps.append(f"${a}({x_val})^2 + {b}$")

            x_squared = x_val ** 2
            steps.append(f"Calculate the exponent: ${x_val}^2 = {x_squared}$")
            steps.append(f"Expression becomes: ${a}({x_squared}) + {b}$")

            term1 = a * x_squared
            steps.append(f"Multiply: ${a} \\times {x_squared} = {term1}$")
            steps.append(f"Expression becomes: ${term1} + {b}$")

            answer = term1 + b
            steps.append(f"Add: ${term1} + {b} = {answer}$")

    else:  # difficulty == 3
        # Hard: Multiple variables with exponents
        # Format: ax^2 + by - c or similar
        a = random.randint(1, 5)
        b = random.randint(2, 7)
        c = random.randint(1, 10)
        x_val = random.randint(2, 5)
        y_val = random.randint(1, 6)

        expression = f"{a}x^2 + {b}y - {c}"
        steps.append(f"Evaluate the expression: ${expression}$ when $x = {x_val}$ and $y = {y_val}$")
        steps.append("**Rule:** Substitute values and follow order of operations (PEMDAS)")
        steps.append(f"Substitute $x = {x_val}$ and $y = {y_val}$:")
        steps.append(f"${a}({x_val})^2 + {b}({y_val}) - {c}$")

        x_squared = x_val ** 2
        steps.append(f"**Step 1:** Calculate the exponent: ${x_val}^2 = {x_squared}$")
        steps.append(f"Expression becomes: ${a}({x_squared}) + {b}({y_val}) - {c}$")

        term1 = a * x_squared
        term2 = b * y_val
        steps.append(f"**Step 2:** Multiply each term:")
        steps.append(f"${a} \\times {x_squared} = {term1}$")
        steps.append(f"${b} \\times {y_val} = {term2}$")
        steps.append(f"Expression becomes: ${term1} + {term2} - {c}$")

        steps.append(f"**Step 3:** Add and subtract left to right:")
        intermediate = term1 + term2
        steps.append(f"${term1} + {term2} = {intermediate}$")
        steps.append(f"${intermediate} - {c} = {intermediate - c}$")

        answer = intermediate - c

    steps.append(f"**Final Answer:** ${answer}$")

    return {
        "question": f"Evaluate ${expression}$ when " +
                   (f"$x = {x_val}$" if difficulty == 1 else
                    f"$x = {x_val}$ and $y = {y_val}$" if difficulty >= 2 else ""),
        "answer": str(answer),
        "answer_numeric": answer,
        "steps": steps,
        "difficulty": difficulty,
    }
