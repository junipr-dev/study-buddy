"""Order of operations question generator (PEMDAS/BODMAS) with word problems."""

import random
from typing import Dict, Any, List

# Word problem templates for order of operations
ORDER_OF_OPS_WORD_PROBLEMS = {
    "difficulty_1": [
        {"template": "You buy {c} packs of cards. Each pack has ({a} + {b}) cards. How many cards total?", "format": "({a} + {b}) * {c}"},
        {"template": "You have ${a}. You earn ${b} per hour for {c} hours. How much money do you have now?", "format": "{a} + {b} * {c}"},
        {"template": "A movie ticket costs ${b}. You buy {c} tickets and have ${a} left over. How much did you start with?", "format": "{a} + {b} * {c}"},
    ],
    "difficulty_2": [
        {"template": "You have {a} boxes. You add {b} more items per box, then square the result and remove {c}. What's the answer?", "format": "(a + b)^2 - c"},
        {"template": "A square room has sides of ({a} + {b}) feet. You remove {c} square feet for a closet. What's the remaining area?", "format": "(a + b)^2 - c"},
    ],
}


def generate_order_of_operations(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate an order of operations problem (PEMDAS/BODMAS).

    Args:
        difficulty:
            1 (easy - simple operations with parentheses)
            2 (medium - multiple operations including exponents)
            3 (hard - complex expressions with all operations)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    # Use word problems 40% of the time for easier difficulties
    use_word_problem = difficulty <= 2 and random.random() < 0.4

    if difficulty == 1:
        # Easy: Simple operations with parentheses
        # Format: (a + b) * c or a + b * c
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(2, 5)

        use_parentheses = random.choice([True, False])

        if use_parentheses:
            # With parentheses
            expression = f"({a} + {b}) \\times {c}"

            if use_word_problem:
                wp = ORDER_OF_OPS_WORD_PROBLEMS["difficulty_1"][0]  # Cards problem
                question = wp["template"].format(a=a, b=b, c=c)
                steps.append(f"**Problem:** {question}")
                steps.append(f"**Identify:** Calculate $({a} + {b}) \\times {c}$")
            else:
                steps.append(f"Start with the expression: $({a} + {b}) \\times {c}$")

            steps.append("**Rule:** Evaluate operations inside **parentheses** first (P in PEMDAS)")
            steps.append(f"Calculate inside parentheses: ${a} + {b} = {a + b}$")
            result = a + b
            steps.append(f"Now multiply: ${result} \\times {c} = {result * c}$")
            answer = result * c
        else:
            # Without parentheses (multiplication first)
            expression = f"{a} + {b} \\times {c}"

            if use_word_problem:
                wp = ORDER_OF_OPS_WORD_PROBLEMS["difficulty_1"][1]  # Money problem
                question = wp["template"].format(a=a, b=b, c=c)
                steps.append(f"**Problem:** {question}")
                steps.append(f"**Identify:** Calculate ${a} + {b} \\times {c}$")
            else:
                steps.append(f"Start with the expression: ${a} + {b} \\times {c}$")

            steps.append("**Rule:** Multiplication comes before addition (MD before AS in PEMDAS)")
            steps.append(f"First multiply: ${b} \\times {c} = {b * c}$")
            result = b * c
            steps.append(f"Then add: ${a} + {result} = {a + result}$")
            answer = a + result

    elif difficulty == 2:
        # Medium: Include exponents and multiple operations
        # Format: a + b^2 * c or (a + b)^2 - c
        a = random.randint(1, 5)
        b = random.randint(2, 4)
        c = random.randint(1, 3)

        if random.choice([True, False]):
            # a + b^2 * c
            expression = f"{a} + {b}^2 \\times {c}"
            steps.append(f"Start with the expression: ${a} + {b}^2 \\times {c}$")
            steps.append("**Rule:** Follow PEMDAS order - Exponents before Multiplication before Addition")

            b_squared = b ** 2
            steps.append(f"First calculate the exponent: ${b}^2 = {b_squared}$")
            steps.append(f"Expression becomes: ${a} + {b_squared} \\times {c}$")

            mult_result = b_squared * c
            steps.append(f"Next multiply: ${b_squared} \\times {c} = {mult_result}$")
            steps.append(f"Expression becomes: ${a} + {mult_result}$")

            answer = a + mult_result
            steps.append(f"Finally add: ${a} + {mult_result} = {answer}$")
        else:
            # (a + b)^2 - c
            expression = f"({a} + {b})^2 - {c}"
            steps.append(f"Start with the expression: $({a} + {b})^2 - {c}$")
            steps.append("**Rule:** Parentheses first, then Exponents, then Subtraction")

            paren_result = a + b
            steps.append(f"Calculate inside parentheses: ${a} + {b} = {paren_result}$")
            steps.append(f"Expression becomes: ${paren_result}^2 - {c}$")

            squared_result = paren_result ** 2
            steps.append(f"Calculate the exponent: ${paren_result}^2 = {squared_result}$")
            steps.append(f"Expression becomes: ${squared_result} - {c}$")

            answer = squared_result - c
            steps.append(f"Finally subtract: ${squared_result} - {c} = {answer}$")

    else:  # difficulty == 3
        # Hard: Complex expression with all operations
        # Format: a^2 + (b - c) * d / e
        a = random.randint(2, 4)
        b = random.randint(10, 20)
        c = random.randint(1, 9)
        d = random.randint(2, 6)
        # Choose e so that division is clean
        paren_val = b - c
        e = random.choice([i for i in range(2, 5) if (paren_val * d) % i == 0])

        expression = f"{a}^2 + ({b} - {c}) \\times {d} \\div {e}"
        steps.append(f"Start with the expression: ${a}^2 + ({b} - {c}) \\times {d} \\div {e}$")
        steps.append("**Rule:** PEMDAS - Parentheses, Exponents, Multiplication/Division (left to right), Addition")

        # Exponents
        a_squared = a ** 2
        steps.append(f"**Step 1:** Calculate exponent: ${a}^2 = {a_squared}$")

        # Parentheses
        paren_result = b - c
        steps.append(f"**Step 2:** Calculate inside parentheses: ${b} - {c} = {paren_result}$")
        steps.append(f"Expression becomes: ${a_squared} + {paren_result} \\times {d} \\div {e}$")

        # Multiplication (left to right)
        mult_result = paren_result * d
        steps.append(f"**Step 3:** Multiply (left to right): ${paren_result} \\times {d} = {mult_result}$")
        steps.append(f"Expression becomes: ${a_squared} + {mult_result} \\div {e}$")

        # Division
        div_result = mult_result // e
        steps.append(f"**Step 4:** Divide: ${mult_result} \\div {e} = {div_result}$")
        steps.append(f"Expression becomes: ${a_squared} + {div_result}$")

        # Addition
        answer = a_squared + div_result
        steps.append(f"**Step 5:** Add: ${a_squared} + {div_result} = {answer}$")

    steps.append(f"**Final Answer:** ${answer}$")

    return {
        "question": f"Evaluate: ${expression}$",
        "answer": str(answer),
        "answer_numeric": answer,
        "steps": steps,
        "difficulty": difficulty,
    }
