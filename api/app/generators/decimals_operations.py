"""Decimals operations question generator with word problems."""

import random
from typing import Dict, Any, List

# Word problem templates for decimals
DECIMAL_WORD_PROBLEMS = {
    "addition": [
        {"context": "shopping", "template": "You buy items costing ${a} and ${b}. What is your total?"},
        {"context": "distance", "template": "You walk {a} miles to school and {b} miles to the store. How far did you walk?"},
        {"context": "weight", "template": "A recipe needs {a} kg of flour and {b} kg of sugar. What is the total weight?"},
    ],
    "subtraction": [
        {"context": "money", "template": "You have ${a}. After buying lunch for ${b}, how much do you have left?"},
        {"context": "distance", "template": "The total trip is {a} miles. After driving {b} miles, how much is left?"},
        {"context": "weight", "template": "A bag weighs {a} kg. You remove {b} kg of items. What's the new weight?"},
    ],
    "multiplication": [
        {"context": "shopping", "template": "Apples cost ${a} per pound. How much for {b} pounds?"},
        {"context": "gas", "template": "Gas costs ${a} per gallon. What's the cost for {b} gallons?"},
        {"context": "rate", "template": "You earn ${a} per hour. How much do you earn in {b} hours?"},
    ],
    "division": [
        {"context": "sharing", "template": "You split ${a} equally among {b} people. How much does each get?"},
        {"context": "unit_price", "template": "{a} ounces of juice costs ${b}. What's the price per ounce?"},
        {"context": "rate", "template": "You drove {a} miles in {b} hours. What was your speed in mph?"},
    ],
}


def generate_decimals_operations(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate a decimals operations problem.

    Args:
        difficulty: 1 (addition/subtraction), 2 (multiplication/division), 3 (mixed operations)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps: List[str] = []

    # Use word problems 50% of the time
    use_word_problem = random.random() < 0.5

    if difficulty == 1:
        # Simple addition/subtraction
        operation = random.choice(["+", "-"])
        a = round(random.uniform(1, 10), 1)
        b = round(random.uniform(1, 10), 1)

        if operation == "+":
            answer = a + b

            if use_word_problem:
                wp = random.choice(DECIMAL_WORD_PROBLEMS["addition"])
                word_question = wp["template"].format(a=a, b=b)
                question = word_question
                steps.append(f"**Problem:** {word_question}")
                steps.append(f"**Identify:** Add ${a} + {b}$")
            else:
                question = f"${a} + {b}$"
                steps.append(f"Calculate: ${a} + {b}$")

            steps.append("**Method:** Line up the decimal points:")
            steps.append(f"$\\begin{{align*}} {a:.1f} \\\\ + {b:.1f} \\\\ \\hline {answer:.1f} \\end{{align*}}$")
        else:
            # Ensure non-negative result
            if a < b:
                a, b = b, a
            answer = a - b

            if use_word_problem:
                wp = random.choice(DECIMAL_WORD_PROBLEMS["subtraction"])
                word_question = wp["template"].format(a=a, b=b)
                question = word_question
                steps.append(f"**Problem:** {word_question}")
                steps.append(f"**Identify:** Subtract ${a} - {b}$")
            else:
                question = f"${a} - {b}$"
                steps.append(f"Calculate: ${a} - {b}$")

            steps.append("**Method:** Line up the decimal points:")
            steps.append(f"$\\begin{{align*}} {a:.1f} \\\\ - {b:.1f} \\\\ \\hline {answer:.1f} \\end{{align*}}$")

    elif difficulty == 2:
        # Multiplication/division
        operation = random.choice(["*", "/"])

        if operation == "*":
            a = round(random.uniform(1, 5), 1)
            b = round(random.uniform(1, 5), 1)
            answer = a * b

            if use_word_problem:
                wp = random.choice(DECIMAL_WORD_PROBLEMS["multiplication"])
                word_question = wp["template"].format(a=a, b=b)
                question = word_question
                steps.append(f"**Problem:** {word_question}")
                steps.append(f"**Identify:** Multiply ${a} \\times {b}$")
            else:
                question = f"${a} \\times {b}$"
                steps.append(f"Calculate: ${a} \\times {b}$")

            steps.append("**Method:** Multiply as if they were whole numbers:")
            a_no_decimal = int(a * 10)
            b_no_decimal = int(b * 10)
            product = a_no_decimal * b_no_decimal
            steps.append(f"${a_no_decimal} \\times {b_no_decimal} = {product}$")
            steps.append("Count decimal places: 1 in each number = 2 total")
            steps.append(f"Place decimal point 2 places from the right: ${answer:.2f}$")
        else:
            # Division - ensure clean result
            divisor = round(random.uniform(1, 5), 1)
            quotient = round(random.uniform(1, 10), 1)
            a = divisor * quotient
            answer = quotient

            if use_word_problem:
                wp = random.choice(DECIMAL_WORD_PROBLEMS["division"])
                word_question = wp["template"].format(a=round(a, 1), b=divisor)
                question = word_question
                steps.append(f"**Problem:** {word_question}")
                steps.append(f"**Identify:** Divide ${a:.1f} \\div {divisor}$")
            else:
                question = f"${a:.1f} \\div {divisor}$"
                steps.append(f"Calculate: ${a:.1f} \\div {divisor}$")

            steps.append(f"**Method:** Move decimal in both numbers one place right:")
            steps.append(f"${int(a * 10)} \\div {int(divisor * 10)}$")
            steps.append(f"Divide: ${int(a * 10)} \\div {int(divisor * 10)} = {answer:.1f}$")

    else:
        # Mixed operations with parentheses
        a = round(random.uniform(1, 5), 1)
        b = round(random.uniform(1, 5), 1)
        c = round(random.uniform(1, 3), 1)

        operation_choice = random.choice(["add_mult", "sub_mult"])

        if operation_choice == "add_mult":
            # (a + b) × c
            sum_ab = a + b
            answer = sum_ab * c
            question = f"$({a} + {b}) \\times {c}$"

            steps.append(f"Calculate: $({a} + {b}) \\times {c}$")
            steps.append("Step 1: Solve inside parentheses first")
            steps.append(f"${a} + {b} = {sum_ab:.1f}$")
            steps.append(f"Step 2: Multiply the result by ${c}$")
            steps.append(f"${sum_ab:.1f} \\times {c} = {answer:.2f}$")
        else:
            # (a - b) × c
            if a < b:
                a, b = b, a
            diff_ab = a - b
            answer = diff_ab * c
            question = f"$({a} - {b}) \\times {c}$"

            steps.append(f"Calculate: $({a} - {b}) \\times {c}$")
            steps.append("Step 1: Solve inside parentheses first")
            steps.append(f"${a} - {b} = {diff_ab:.1f}$")
            steps.append(f"Step 2: Multiply the result by ${c}$")
            steps.append(f"${diff_ab:.1f} \\times {c} = {answer:.2f}$")

    steps.append(f"**Final Answer:** ${answer:.2f}$")

    return {
        "question": f"Calculate: {question}",
        "answer": f"{answer:.2f}",
        "answer_numeric": round(answer, 2),
        "steps": steps,
        "difficulty": difficulty,
    }
