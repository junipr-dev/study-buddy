"""Integer operations question generator with word problems."""

import random
from typing import Dict, Any

# Word problem templates for more engaging questions
WORD_PROBLEM_CONTEXTS = [
    {
        "context": "temperature",
        "scenarios": [
            "The temperature was {a}°F in the morning. It {change_word} by {b_abs}°F. What is the new temperature?",
            "At midnight, the temperature was {a}°F. By noon, it had {change_word} {b_abs}°F. What was the noon temperature?",
        ],
        "change_words": {"positive": "rose", "negative": "dropped"},
    },
    {
        "context": "money",
        "scenarios": [
            "You had ${a_abs} in your account. You {action} ${b_abs}. What is your new balance?",
            "A business had a {status} of ${a_abs}. After a transaction of {sign}${b_abs}, what is the new balance?",
        ],
        "action_words": {"positive": "deposited", "negative": "withdrew"},
    },
    {
        "context": "elevation",
        "scenarios": [
            "A submarine is at {a} feet (negative = below sea level). It {move_word} {b_abs} feet. What is its new depth?",
            "A hiker starts at {a} feet elevation. They {move_word} {b_abs} feet. What is their new elevation?",
        ],
        "move_words": {"positive": "ascends", "negative": "descends"},
    },
    {
        "context": "football",
        "scenarios": [
            "A football team gained {a} yards on the first play. On the second play, they {result} {b_abs} yards. What is their total yardage?",
            "The team started at the {a}-yard line. After {result} {b_abs} yards, where are they now?",
        ],
        "result_words": {"positive": "gained", "negative": "lost"},
    },
    {
        "context": "game_score",
        "scenarios": [
            "In a video game, you have {a} points. You {action} {b_abs} points. What is your new score?",
            "Your game character has {a} health points. After the battle, your health {action} by {b_abs}. What is your new health?",
        ],
        "action_words": {"positive": "gain", "negative": "lose"},
    },
]


def generate_word_problem(a: int, b: int, operation: str) -> tuple[str, list]:
    """Generate a word problem for integer operations."""
    context = random.choice(WORD_PROBLEM_CONTEXTS)
    scenario = random.choice(context["scenarios"])
    steps = []

    # Build the word problem
    a_abs = abs(a)
    b_abs = abs(b)

    if "change_word" in scenario:
        change_word = context["change_words"]["positive" if b >= 0 else "negative"]
        question = scenario.format(a=a, b_abs=b_abs, a_abs=a_abs, change_word=change_word)
    elif "action" in scenario and "action_words" in context:
        action = context["action_words"]["positive" if b >= 0 else "negative"]
        status = "profit" if a >= 0 else "debt"
        sign = "+" if b >= 0 else "-"
        question = scenario.format(a=a, a_abs=a_abs, b_abs=b_abs, action=action, status=status, sign=sign)
    elif "move_word" in scenario:
        move_word = context["move_words"]["positive" if b >= 0 else "negative"]
        question = scenario.format(a=a, b_abs=b_abs, a_abs=a_abs, move_word=move_word)
    elif "result" in scenario:
        result = context["result_words"]["positive" if b >= 0 else "negative"]
        question = scenario.format(a=a if a >= 0 else abs(a), b_abs=b_abs, result=result)
    else:
        # Fallback
        question = f"Calculate: {a} + {b}"

    steps.append(f"**Identify the numbers:** Starting value = {a}, Change = {'+' if b >= 0 else ''}{b}")
    steps.append(f"**Set up the equation:** ${a} + ({b})$")

    return question, steps


def generate_integers_operations(difficulty: int = 1) -> Dict[str, Any]:
    """
    Generate an integer operations problem (addition, subtraction, multiplication, division).

    Args:
        difficulty:
            1 (easy - simple addition/subtraction)
            2 (medium - multiplication and division)
            3 (hard - mixed operations with negatives)

    Returns:
        Dict with question, answer, and solution steps
    """
    steps = []

    # Decide whether to use a word problem (40% chance for difficulty 1-2)
    use_word_problem = difficulty <= 2 and random.random() < 0.4

    if difficulty == 1:
        # Easy: Simple addition or subtraction with positive and negative integers
        operation = random.choice(['add', 'subtract'])

        if operation == 'add':
            a = random.randint(-20, 20)
            b = random.randint(-20, 20)

            # Generate word problem version
            if use_word_problem:
                question, word_steps = generate_word_problem(a, b, 'add')
                steps.extend(word_steps)
                answer = a + b
                steps.append("**Rule:** When adding integers:")
                if (a >= 0 and b >= 0) or (a < 0 and b < 0):
                    steps.append("- Same signs: add absolute values, keep the sign")
                else:
                    steps.append("- Different signs: subtract absolute values, keep sign of larger absolute value")
                steps.append(f"**Calculate:** ${a} + ({b}) = {answer}$")
                steps.append(f"**Final Answer:** ${answer}$")

                return {
                    "question": question,
                    "answer": str(answer),
                    "answer_numeric": answer,
                    "steps": steps,
                    "difficulty": difficulty,
                }

            if a >= 0 and b >= 0:
                expression = f"{a} + {b}"
            elif a >= 0 and b < 0:
                expression = f"{a} + ({b})"
            elif a < 0 and b >= 0:
                expression = f"({a}) + {b}"
            else:
                expression = f"({a}) + ({b})"

            steps.append(f"Calculate: ${expression}$")
            steps.append("**Rule:** When adding integers:")
            if a >= 0 and b >= 0:
                steps.append("- Both numbers are positive, so simply add them")
                answer = a + b
            elif (a < 0 and b < 0):
                steps.append("- Both numbers are negative, so add their absolute values and keep the negative sign")
                steps.append(f"$|{a}| + |{b}| = {abs(a)} + {abs(b)} = {abs(a) + abs(b)}$")
                steps.append(f"Since both are negative: $-{abs(a) + abs(b)}$")
                answer = a + b
            else:
                steps.append("- Numbers have different signs, so subtract the smaller absolute value from the larger")
                steps.append(f"$|{a}| = {abs(a)}$ and $|{b}| = {abs(b)}$")
                if abs(a) > abs(b):
                    steps.append(f"Larger absolute value: $|{a}| = {abs(a)}$, so result has sign of {a}")
                    steps.append(f"${abs(a)} - {abs(b)} = {abs(a) - abs(b)}$")
                else:
                    steps.append(f"Larger absolute value: $|{b}| = {abs(b)}$, so result has sign of {b}")
                    steps.append(f"${abs(b)} - {abs(a)} = {abs(b) - abs(a)}$")
                answer = a + b
        else:  # subtract
            a = random.randint(-15, 15)
            b = random.randint(-15, 15)

            if a >= 0 and b >= 0:
                expression = f"{a} - {b}"
            elif a >= 0 and b < 0:
                expression = f"{a} - ({b})"
            elif a < 0 and b >= 0:
                expression = f"({a}) - {b}"
            else:
                expression = f"({a}) - ({b})"

            steps.append(f"Calculate: ${expression}$")
            steps.append("**Rule:** Subtracting is the same as adding the opposite")
            steps.append(f"Rewrite as: ${a} + ({-b})$")

            answer = a - b
            if b < 0:
                steps.append(f"Subtracting a negative means adding a positive: ${a} + {abs(b)}$")
            steps.append(f"Calculate: ${answer}$")

    elif difficulty == 2:
        # Medium: Multiplication and division
        operation = random.choice(['multiply', 'divide'])

        if operation == 'multiply':
            a = random.randint(-12, 12)
            while a == 0:
                a = random.randint(-12, 12)
            b = random.randint(-10, 10)
            while b == 0:
                b = random.randint(-10, 10)

            expression = f"{a} \\times {b}"
            steps.append(f"Calculate: ${expression}$")
            steps.append("**Rule:** When multiplying integers:")
            steps.append("- Same signs → positive result")
            steps.append("- Different signs → negative result")

            if (a > 0 and b > 0) or (a < 0 and b < 0):
                steps.append(f"Both numbers have the same sign")
                steps.append(f"Multiply absolute values: ${abs(a)} \\times {abs(b)} = {abs(a) * abs(b)}$")
                steps.append(f"Result is positive: ${a * b}$")
            else:
                steps.append(f"Numbers have different signs")
                steps.append(f"Multiply absolute values: ${abs(a)} \\times {abs(b)} = {abs(a) * abs(b)}$")
                steps.append(f"Result is negative: ${a * b}$")

            answer = a * b
        else:  # divide
            # Ensure clean division
            b = random.randint(-8, 8)
            while b == 0:
                b = random.randint(-8, 8)
            quotient = random.randint(-10, 10)
            while quotient == 0:
                quotient = random.randint(-10, 10)
            a = b * quotient

            expression = f"{a} \\div {b}"
            steps.append(f"Calculate: ${expression}$")
            steps.append("**Rule:** When dividing integers:")
            steps.append("- Same signs → positive result")
            steps.append("- Different signs → negative result")

            if (a > 0 and b > 0) or (a < 0 and b < 0):
                steps.append(f"Both numbers have the same sign")
                steps.append(f"Divide absolute values: ${abs(a)} \\div {abs(b)} = {abs(a) // abs(b)}$")
                steps.append(f"Result is positive: ${a // b}$")
            else:
                steps.append(f"Numbers have different signs")
                steps.append(f"Divide absolute values: ${abs(a)} \\div {abs(b)} = {abs(a) // abs(b)}$")
                steps.append(f"Result is negative: ${a // b}$")

            answer = a // b

    else:  # difficulty == 3
        # Hard: Mixed operations with multiple steps
        a = random.randint(-10, 10)
        b = random.randint(-8, 8)
        c = random.randint(-6, 6)

        # Format: a * b + c or a + b * c
        if random.choice([True, False]):
            expression = f"{a} \\times {b} + {c}"
            steps.append(f"Calculate: ${expression}$")
            steps.append("**Rule:** Follow order of operations (multiplication before addition)")

            mult_result = a * b
            steps.append(f"**Step 1:** Multiply first: ${a} \\times {b}$")
            if (a > 0 and b > 0) or (a < 0 and b < 0):
                steps.append(f"Same signs → positive: ${mult_result}$")
            else:
                steps.append(f"Different signs → negative: ${mult_result}$")

            steps.append(f"**Step 2:** Add: ${mult_result} + {c}$")
            answer = mult_result + c
            steps.append(f"Result: ${answer}$")
        else:
            expression = f"{a} + {b} \\times {c}"
            steps.append(f"Calculate: ${expression}$")
            steps.append("**Rule:** Follow order of operations (multiplication before addition)")

            mult_result = b * c
            steps.append(f"**Step 1:** Multiply first: ${b} \\times {c}$")
            if (b > 0 and c > 0) or (b < 0 and c < 0):
                steps.append(f"Same signs → positive: ${mult_result}$")
            else:
                steps.append(f"Different signs → negative: ${mult_result}$")

            steps.append(f"**Step 2:** Add: ${a} + {mult_result}$")
            answer = a + mult_result
            steps.append(f"Result: ${answer}$")

    steps.append(f"**Final Answer:** ${answer}$")

    return {
        "question": f"Calculate: ${expression}$",
        "answer": str(answer),
        "answer_numeric": answer,
        "steps": steps,
        "difficulty": difficulty,
    }
